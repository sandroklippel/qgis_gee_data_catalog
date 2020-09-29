# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GeeDataCatalog
 QGIS Plugin to search, view and download satellite imagery and
 geospatial datasets from Google Earth Engine.
        begin                : 2020-05-24
        git sha              : $Format:%H$
        copyright            : (C) 2020 by Sandro Klippel
        email                : sandroklippel at gmail.com
 ***************************************************************************/
"""

import os
import os.path
import shutil

from qgis.core import QgsMapLayerType, QgsProject, QgsRasterLayer, QgsRectangle
from qgis.PyQt.QtCore import QCoreApplication, QDate, QSettings, QTranslator
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction, QFileDialog, QMenu

from osgeo import gdal

from .datasets import GEE_DATASETS, GLOBAL_EXTENT
from .ee_interface import search_ee_collection, update_ee_image_layer
from .ee_interface import add_ee_image_layer, download_ee_image_layer
from .iface_utils import get_canvas_extent, get_canvas_proj
from .misc_utils import write_xmlfile
from .qgis_gee_data_catalog_dialog import GeeDataCatalogDialog
from .resources import *

try:
    import ee
    MISSINGAPI = False
except ImportError:
    MISSINGAPI = True

class GeeDataCatalog:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'GeeDataCatalog_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)
            QCoreApplication.installTranslator(self.translator)

        # Declare instance attributes
        self.dlg = None
        self.actions = []
        self.menu = self.tr(u'&Google Earth Engine Data Catalog')

        # Check if plugin was started the first time in current QGIS session
        # Must be set in initGui() to survive plugin reloads
        self.first_start = None

        # set if ee.Initialize was run
        self.ee_uninitialized = True

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('GeeDataCatalog', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            # Adds plugin icon to Plugins toolbar
            self.iface.addToolBarIcon(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""
        # change icon here !
        # icon_path = ':/images/themes/default/mActionAddGeoPackageLayer.svg'
        icon_path = ':/plugins/qgis_gee_data_catalog/icon.svg'
        # icon_gdrive = QIcon(':/images/themes/default/downloading_svg.svg')
        icon_save_xml = QIcon(':/images/themes/default/mActionFileSave.svg')
        self.add_action(
            icon_path,
            text=self.tr(u'Google Earth Engine Data Catalog'),
            callback=self.run,
            parent=self.iface.mainWindow())

        # update layers action in toolbar
        # self.add_action(
        #     icon_path,
        #     text=self.tr(u'Rebuild GEE Layers'),
        #     callback=self.update_ee_image_layers,
        #     add_to_menu=False,
        #     add_to_toolbar=True,
        #     status_tip='Status tip',
        #     whats_this='Whats tip',
        #     parent=self.iface.mainWindow())

        # will be set False in run()
        self.first_start = True

        # define action for download ee layers to google drive

        self.layerActionDownloadFull = QAction("Full image extent", self.iface.mainWindow())
        self.layerActionDownloadFull.setObjectName("geeLayerFullDownload")
        self.layerActionDownloadFull.triggered.connect(self.gee_layer_full_download)

        self.layerActionDownloadCanvas = QAction("Canvas extent", self.iface.mainWindow())
        self.layerActionDownloadCanvas.setObjectName("geeLayerCanvasDownload")
        self.layerActionDownloadCanvas.triggered.connect(self.gee_layer_canvas_download)

        # define action to Make a permanent XML file

        self.layerActionMakeXmlFile = QAction(icon_save_xml, "Save the XML definition file", self.iface.mainWindow())
        self.layerActionMakeXmlFile.setObjectName("geeLayerMakeXml")
        self.layerActionMakeXmlFile.triggered.connect(self.gee_layer_make_xml)

        download_gdrive = "Download GeoTiff to Google Drive"

        # add custom actions for all raster layers - further will be required to set up an action for each layer
        self.iface.addCustomActionForLayerType(self.layerActionMakeXmlFile, None, QgsMapLayerType.RasterLayer, False)
        self.iface.addCustomActionForLayerType(self.layerActionDownloadFull, download_gdrive, QgsMapLayerType.RasterLayer, False)
        self.iface.addCustomActionForLayerType(self.layerActionDownloadCanvas, download_gdrive, QgsMapLayerType.RasterLayer, False)

        # add custom actions for already load layers
        for l in list(QgsProject.instance().mapLayers().values()):
            self.on_layer_was_added(l)
        
        # connect method to signal when layer was added
        QgsProject.instance().layerWasAdded.connect(self.on_layer_was_added)

        # Register signal to rebuild xml from EE layers on project load
        self.iface.projectRead.connect(self.update_ee_image_layers)


    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""

        # self.iface.projectRead.disconnect(self.update_ee_image_layers)
        self.iface.removeCustomActionForLayerType(self.layerActionMakeXmlFile)
        self.iface.removeCustomActionForLayerType(self.layerActionDownloadFull)
        self.iface.removeCustomActionForLayerType(self.layerActionDownloadCanvas)
        QgsProject.instance().layerWasAdded.disconnect(self.on_layer_was_added)

        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&Google Earth Engine Data Catalog'),
                action)
            self.iface.removeToolBarIcon(action)

    def on_layer_was_added(self, map_layer):
        if map_layer.customProperty('ee-image'):
            if map_layer.customProperty('ee-image') == 'MEM':
                self.iface.addCustomActionForLayer(self.layerActionMakeXmlFile, map_layer)
            if map_layer.customProperty('ee-image-wkt') == GLOBAL_EXTENT:
                self.iface.addCustomActionForLayer(self.layerActionDownloadCanvas, map_layer)
            else:
                self.iface.addCustomActionForLayer(self.layerActionDownloadFull, map_layer)
                self.iface.addCustomActionForLayer(self.layerActionDownloadCanvas, map_layer)
    
    def gee_layer_make_xml(self):
        eelayer = self.iface.activeLayer()
        dest_dir = QgsProject.instance().absolutePath() or os.getcwd()
        dest_name = eelayer.name().replace('/', '_') + '.xml'
        dest_file = os.path.join(dest_dir, dest_name)
        source_xml = eelayer.dataProvider().dataSourceUri()
        dest_xml, _ = QFileDialog.getSaveFileName(self.dlg, 'Select output file', dest_file, 'XML files (*.xml)')
        if dest_xml:
            shutil.copyfile(source_xml, dest_xml)
            newname = os.path.splitext(os.path.basename(dest_xml))[0]
            newlayer = QgsRasterLayer(dest_xml, newname)
            
            if newlayer.isValid():
                imageid = eelayer.customProperty('ee-image-id')
                date = eelayer.customProperty('ee-image-date')
                qml = eelayer.customProperty('ee-image-qml')
                extent = eelayer.customProperty('ee-image-wkt')
                if qml is not None:
                    newlayer.loadNamedStyle(qml) # load qml must be first since this clean all custom properties
                newlayer.setCustomProperty('ee-image', 'XML')
                newlayer.setCustomProperty('ee-image-id', imageid)
                newlayer.setCustomProperty('ee-image-date', date)
                newlayer.setCustomProperty('ee-image-bands', eelayer.customProperty('ee-image-bands'))
                newlayer.setCustomProperty('ee-image-scale', eelayer.customProperty('ee-image-scale'))
                newlayer.setCustomProperty('ee-image-b_min', eelayer.customProperty('ee-image-b_min'))
                newlayer.setCustomProperty('ee-image-b_max', eelayer.customProperty('ee-image-b_max'))
                newlayer.setCustomProperty('ee-image-palette', eelayer.customProperty('ee-image-palette'))
                newlayer.setCustomProperty('ee-image-qml', qml)
                newlayer.setCustomProperty('ee-image-wkt', extent)
                if date is not None:
                    newlayer.setAbstract(f"ee.Image('{imageid}') \n\nDate: {date}")
                else:
                    newlayer.setAbstract(f"ee.Image('{imageid}')")
                bb = QgsRectangle.fromWkt(extent)
                newlayer.setExtent(bb)
                QgsProject.instance().addMapLayer(newlayer)
                QgsProject.instance().layerTreeRoot().findLayer(newlayer.id()).setItemVisibilityChecked(False)

    def gee_layer_full_download(self):
        eelayer = self.iface.activeLayer()
        name = eelayer.name()
        imageid = eelayer.customProperty('ee-image-id')
        bands = eelayer.customProperty('ee-image-bands')
        scale = eelayer.customProperty('ee-image-scale')
        proj = get_canvas_proj(self.iface)
        download_ee_image_layer(self.iface, name, imageid, bands, scale, proj)

    def gee_layer_canvas_download(self):
        eelayer = self.iface.activeLayer()
        name = eelayer.name()
        imageid = eelayer.customProperty('ee-image-id')
        bands = eelayer.customProperty('ee-image-bands')
        scale = eelayer.customProperty('ee-image-scale')
        extent = get_canvas_extent(self.iface)
        proj = get_canvas_proj(self.iface)
        download_ee_image_layer(self.iface, name, imageid, bands, scale, proj, extent)

    def update_ee_image_layers(self):
        layers = QgsProject.instance().mapLayers().values()
        for eelayer in filter(lambda layer: layer.customProperty('ee-image') == 'XML', layers):
            extent = eelayer.customProperty('ee-image-wkt')
            bb = QgsRectangle.fromWkt(extent)
            eelayer.setExtent(bb)
            xml_file = eelayer.dataProvider().dataSourceUri()
            # ds = gdal.Open(xml_file)
            # if ds.ReadAsArray(xsize=1, ysize=1) is None:
            imageid = eelayer.customProperty('ee-image-id')
            bands = eelayer.customProperty('ee-image-bands')
            qml = eelayer.customProperty('ee-image-qml')
            palette = eelayer.customProperty('ee-image-palette')
            if not qml:
                b_min = list(map(int, eelayer.customProperty('ee-image-b_min')))
                b_max = list(map(int, eelayer.customProperty('ee-image-b_max')))
            else:
                b_min = None
                b_max = None
            if self.ee_uninitialized:
                ee.Initialize()
            new_xml = update_ee_image_layer(imageid, bands, b_min, b_max, palette)
            write_xmlfile(new_xml, name=None, dest=xml_file)
            eelayer.dataProvider().reloadData()
            eelayer.triggerRepaint()
            eelayer.reload()
        self.iface.mapCanvas().refresh()

    def update_dlg_fields(self, new_collection):
        """Update list of band combinations and availability from selected collection"""

        self.dlg.bands.clear()        #This will remove all previous items
        self.dlg.bands.addItems(GEE_DATASETS[new_collection]['bandcombinations'].keys())
        self.dlg.infotext.setPlainText(GEE_DATASETS[new_collection]['description'])
        if 'cloudfield' in GEE_DATASETS[new_collection]:
            self.dlg.cloudcover.setEnabled(True)
        else:
            self.dlg.cloudcover.setEnabled(False)
        # date availability
        if 'availability' in GEE_DATASETS[new_collection]:
            self.dlg.startdate.setEnabled(True)
            self.dlg.enddate.setEnabled(True)
            mindate = GEE_DATASETS[new_collection]['availability'][0].split('-')
            year, month, day = int(mindate[0]), int(mindate[1]), int(mindate[2])
            self.dlg.startdate.setMinimumDate(QDate(year, month, day))
            self.dlg.enddate.setMinimumDate(QDate(year, month, day))
            if GEE_DATASETS[new_collection]['availability'][1] is None:
                self.dlg.startdate.setMaximumDate(QDate.currentDate())
                self.dlg.enddate.setMaximumDate(QDate.currentDate().addDays(1))
                self.dlg.startdate.setDate(QDate.currentDate().addDays(-3)) # to fill default date
            else:
                maxdate = GEE_DATASETS[new_collection]['availability'][1].split('-')
                year, month, day = int(maxdate[0]), int(maxdate[1]), int(maxdate[2])
                self.dlg.startdate.setMaximumDate(QDate(year, month, day))
                self.dlg.enddate.setMaximumDate(QDate(year, month, day).addDays(1))
                self.dlg.startdate.setDate(QDate(year, month, day).addDays(-3)) # to fill default date
        else:
            self.dlg.startdate.setEnabled(False)
            self.dlg.enddate.setEnabled(False)

    def update_dlg_enddate(self, new_date):
        self.dlg.enddate.setDate(new_date.addDays(4))

    def update_dlg_startdate(self, end_date):
        if end_date <= self.dlg.startdate.date():
            self.dlg.startdate.setDate(end_date.addDays(-1))
    

    def run(self):
        """Run method that performs all the real work"""

        # Create the dialog with elements (after translation) and keep reference
        # Only create GUI ONCE in callback, so that it will only load when the plugin is started
        if self.first_start:

            self.first_start = False
            self.dlg = GeeDataCatalogDialog()
            self.dlg.finished.connect(self.result) # connects with result function.

            # date check
            self.dlg.startdate.dateChanged.connect(self.update_dlg_enddate)
            self.dlg.enddate.dateChanged.connect(self.update_dlg_startdate)

            # fill dialog with datasets
            self.dlg.collection.currentTextChanged.connect(self.update_dlg_fields)
            self.dlg.collection.addItems(GEE_DATASETS.keys())

            # self.dlg.startdate.setDate(QDate.currentDate().addDays(-3))
            # already setting in UI file
            # self.dlg.startdate.setCalendarPopup(True)
            # self.dlg.enddate.setCalendarPopup(True)

        # show the dialog
        # self.dlg.show()
        # Run the dialog event loop
        # result = self.dlg.exec_()

        # update destination and default folder for output directory
        self.dlg.destination_folder.setText( "Temporary Output" )
        self.dlg.default_folder = QgsProject.instance().absolutePath() or os.getcwd()
        self.dlg.open()
        
    def result(self, result):
        # See if OK was pressed
        if result:

            if MISSINGAPI:
                raise ImportError('Dependency error: earthengine-api must be installed')

            elif self.ee_uninitialized:
                try:
                    ee.Initialize()
                    self.ee_uninitialized = False
                except OSError:
                    raise OSError('Fail to establish connection with the earthengine server')

            # search ee images
            collection = self.dlg.collection.currentText()
            startdate = self.dlg.startdate.date().toString('yyyy-MM-dd') if 'availability' in GEE_DATASETS[collection] else None
            enddate = self.dlg.enddate.date().toString('yyyy-MM-dd') if 'availability' in GEE_DATASETS[collection] else None
            cloudcover = int(self.dlg.cloudcover.cleanText()) if 'cloudfield' in GEE_DATASETS[collection] else None
            destination_folder = str(self.dlg.destination_folder.text())
            limit = int(self.dlg.limit.cleanText())
            addlayer = self.dlg.addlayer.isChecked()

            vis_params = GEE_DATASETS[collection]['bandcombinations'][self.dlg.bands.currentText()]
            bands = vis_params['bands']
            scale = vis_params['scale']
            suffix = vis_params.get('suffix', '')
            b_min = vis_params.get('min', None)
            b_max = vis_params.get('max', None)
            palette = vis_params.get('palette', None)
            qml = os.path.join(self.plugin_dir, 'qml', vis_params['qml'] + '.qml') if 'qml' in vis_params else None

            # need to test if it is a valid epsg proj
            # if someone else, set to 4326
            # QgsProject.instance().setCrs(QgsCoordinateReferenceSystem(4326)) <- qgis.core

            if 'namefield' in GEE_DATASETS[collection]:
                images_list = search_ee_collection(collection=GEE_DATASETS[collection].get('id', collection),
                                                   extent=get_canvas_extent(self.iface),
                                                   proj=get_canvas_proj(self.iface),
                                                   startdate=startdate,
                                                   enddate=enddate,
                                                   cloudfield=GEE_DATASETS[collection].get('cloudfield', None),
                                                   cloudcover=cloudcover,
                                                   namefield=GEE_DATASETS[collection]['namefield'],
                                                   bands=bands,
                                                   limit=limit)
            else:
                images_list = [[GEE_DATASETS[collection].get('id', collection), collection, None]]

            if images_list and addlayer:
                for imageid, name, date in images_list:
                    add_ee_image_layer(imageid=imageid,
                                       name=name + suffix,
                                       date=date,
                                       bands=bands,
                                       scale=scale,
                                       b_min=b_min,
                                       b_max=b_max,
                                       palette=palette,
                                       qml=qml,
                                       extent=GEE_DATASETS[collection].get('extent', None),
                                       destination=destination_folder)
            elif not images_list:
                self.iface.messageBar().pushMessage('Search did not return any image')
            else:
                images_number = len(images_list)
                images_text = 'images' if images_number > 1 else 'image'
                self.iface.messageBar().pushMessage(f'Search returned {images_number} {images_text}')
