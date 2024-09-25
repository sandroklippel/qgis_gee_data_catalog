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
from os.path import isfile

from osgeo import gdal
from qgis.core import Qgis, QgsMessageLog, QgsMapLayerType, QgsProject, QgsRasterLayer, QgsRectangle
from qgis.PyQt.QtCore import QCoreApplication, QDate, QSettings, QTranslator
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction, QFileDialog, QMenu

from .read_datasets import GEE_DATASETS
from .ee_interface import (
    add_ee_image_layer,
    download_ee_image_layer,
    search_ee_collection,
    update_ee_image,
    get_ee_image_tms
)
from .iface_utils import get_canvas_extent, get_canvas_proj
from .misc_utils import get_gdal_xml, tms_to_gdalurl, write_xmlfile
from .qgis_gee_data_catalog_dialog import GeeDataCatalogDialog
from .resources import *

try:
    import ee
    MISSINGAPI = False
except ImportError:
    MISSINGAPI = True

GLOBAL_EXTENT = """POLYGON((-20037508.34278924390673637 -20037508.34278925508260727,
                            20037508.34278924390673637 -20037508.34278925508260727, 
                            20037508.34278924390673637 20037508.34278924390673637, 
                            -20037508.34278924390673637 20037508.34278924390673637, 
                            -20037508.34278924390673637 -20037508.34278925508260727))"""


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
        locale = QSettings().value("locale/userLocale")[0:2]
        locale_path = os.path.join(
            self.plugin_dir, "i18n", "GeeDataCatalog_{}.qm".format(locale)
        )

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)
            QCoreApplication.installTranslator(self.translator)

        # Declare instance attributes
        self.dlg = None
        self.actions = []
        self.menu = self.tr("&Google Earth Engine Data Catalog")

        # Check if plugin was started the first time in current QGIS session
        # Must be set in initGui() to survive plugin reloads
        self.first_start = None
        
        # Earth Engine Cloud Project
        self.ee_project = os.getenv('GOOGLE_CLOUD_PROJECT')
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
        return QCoreApplication.translate("GeeDataCatalog", message)

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
        parent=None,
    ):
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
            self.iface.addPluginToMenu(self.menu, action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""
        # change icon here !
        # icon_path = ':/images/themes/default/mActionAddGeoPackageLayer.svg'
        icon_path = ":/plugins/qgis_gee_data_catalog/icon.svg"
        icon_renew_xml = QIcon(":/images/themes/default/mActionRefresh.svg")
        icon_save_xml = QIcon(":/images/themes/default/mActionFileSave.svg")
        self.add_action(
            icon_path,
            text=self.tr("Google Earth Engine Data Catalog"),
            callback=self.run,
            parent=self.iface.mainWindow(),
        )

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

        self.layerActionDownloadFull = QAction(
            "Full image extent", self.iface.mainWindow()
        )
        self.layerActionDownloadFull.setObjectName("geeLayerFullDownload")
        self.layerActionDownloadFull.triggered.connect(self.gee_layer_full_download)

        self.layerActionDownloadCanvas = QAction(
            "Canvas extent", self.iface.mainWindow()
        )
        self.layerActionDownloadCanvas.setObjectName("geeLayerCanvasDownload")
        self.layerActionDownloadCanvas.triggered.connect(self.gee_layer_canvas_download)

        # define action to Make a permanent XML file

        self.layerActionMakeXmlFile = QAction(
            icon_save_xml, "Save the XML definition file", self.iface.mainWindow()
        )
        self.layerActionMakeXmlFile.setObjectName("geeLayerMakeXml")
        self.layerActionMakeXmlFile.triggered.connect(self.gee_layer_make_xml)

        # define action to Renew the XML file

        self.layerActionRenewXmlFile = QAction(
            icon_renew_xml, "Renew the XML definition file", self.iface.mainWindow()
        )
        self.layerActionRenewXmlFile.setObjectName("geeLayerRenewXml")
        self.layerActionRenewXmlFile.triggered.connect(self.gee_layer_renew_xml)

        download_gdrive = "Download GeoTiff to Google Drive"

        # add custom actions for all raster layers - further will be required to set up an action for each layer
        self.iface.addCustomActionForLayerType(
            self.layerActionMakeXmlFile, None, QgsMapLayerType.RasterLayer, False
        )
        self.iface.addCustomActionForLayerType(
            self.layerActionRenewXmlFile, None, QgsMapLayerType.RasterLayer, False
        )
        self.iface.addCustomActionForLayerType(
            self.layerActionDownloadFull,
            download_gdrive,
            QgsMapLayerType.RasterLayer,
            False,
        )
        self.iface.addCustomActionForLayerType(
            self.layerActionDownloadCanvas,
            download_gdrive,
            QgsMapLayerType.RasterLayer,
            False,
        )

        # add custom actions for already load layers
        for l in list(QgsProject.instance().mapLayers().values()):
            self.on_layer_was_added(l)

        # connect method to signal when layer was added
        QgsProject.instance().layerWasAdded.connect(self.on_layer_was_added)

        # Register signal to rebuild xml from EE layers on project load
        self.iface.projectRead.connect(self.update_ee_image_layers)

    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""

        self.iface.removeCustomActionForLayerType(self.layerActionMakeXmlFile)
        self.iface.removeCustomActionForLayerType(self.layerActionRenewXmlFile)
        self.iface.removeCustomActionForLayerType(self.layerActionDownloadFull)
        self.iface.removeCustomActionForLayerType(self.layerActionDownloadCanvas)
        self.iface.projectRead.disconnect(self.update_ee_image_layers)
        QgsProject.instance().layerWasAdded.disconnect(self.on_layer_was_added)

        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr("&Google Earth Engine Data Catalog"), action
            )
            self.iface.removeToolBarIcon(action)

    def on_layer_was_added(
        self, map_layer
    ):  # change to add actions on add_layer (ee_interface)
        if map_layer.customProperty("ee-image"):
            if map_layer.customProperty("ee-image") == "MEM":
                self.iface.addCustomActionForLayer(
                    self.layerActionMakeXmlFile, map_layer
                )
            else:
                self.iface.addCustomActionForLayer(
                    self.layerActionRenewXmlFile, map_layer
                )
            if map_layer.customProperty("ee-image-wkt") == GLOBAL_EXTENT:
                self.iface.addCustomActionForLayer(
                    self.layerActionDownloadCanvas, map_layer
                )
            else:
                self.iface.addCustomActionForLayer(
                    self.layerActionDownloadFull, map_layer
                )
                self.iface.addCustomActionForLayer(
                    self.layerActionDownloadCanvas, map_layer
                )

    def gee_layer_renew_xml(self):
        eelayer = self.iface.activeLayer()
        self.update_ee_image_layer(eelayer)
        self.iface.mapCanvas().refresh()

    def gee_layer_make_xml(self):
        eelayer = self.iface.activeLayer()
        dest_dir = QgsProject.instance().absolutePath() or os.getcwd()
        dest_name = eelayer.name().replace("/", "_") + ".xml"
        dest_file = os.path.join(dest_dir, dest_name)
        source_xml = eelayer.dataProvider().dataSourceUri()
        dest_xml, _ = QFileDialog.getSaveFileName(
            self.dlg, "Select output file", dest_file, "XML files (*.xml)"
        )
        if dest_xml:
            shutil.copyfile(source_xml, dest_xml)
            newname = os.path.splitext(os.path.basename(dest_xml))[0]
            newlayer = QgsRasterLayer(dest_xml, newname)

            if newlayer.isValid():
                imageid = eelayer.customProperty("ee-image-id")
                date = eelayer.customProperty("ee-image-date")
                bands = eelayer.customProperty("ee-image-bands")
                qml = eelayer.customProperty("ee-image-qml")
                extent = eelayer.customProperty("ee-image-wkt")
                # load qml must be first since this clean all custom properties
                if qml is not None:
                    if isfile(
                        qml + "_" + QSettings().value("locale/userLocale") + ".qml"
                    ):
                        newlayer.loadNamedStyle(
                            qml + "_" + QSettings().value("locale/userLocale") + ".qml"
                        )
                    else:
                        newlayer.loadNamedStyle(qml + ".qml")
                newlayer.setCustomProperty("ee-image", "XML")
                newlayer.setCustomProperty("ee-image-id", imageid)
                newlayer.setCustomProperty("ee-image-date", date)
                newlayer.setCustomProperty("ee-image-bands", bands)
                newlayer.setCustomProperty(
                    "ee-image-scale", eelayer.customProperty("ee-image-scale")
                )
                newlayer.setCustomProperty(
                    "ee-image-b_min", eelayer.customProperty("ee-image-b_min")
                )
                newlayer.setCustomProperty(
                    "ee-image-b_max", eelayer.customProperty("ee-image-b_max")
                )
                newlayer.setCustomProperty(
                    "ee-image-palette", eelayer.customProperty("ee-image-palette")
                )
                newlayer.setCustomProperty(
                    "ee-image-expression", eelayer.customProperty("ee-image-expression")
                )
                newlayer.setCustomProperty("ee-image-qml", qml)
                newlayer.setCustomProperty("ee-image-wkt", extent)

                fmt_bands = '-'.join(bands)
                if date is not None:
                    newlayer.setAbstract(f"Image: {imageid}\n Bands:{fmt_bands}\nDate: {date}")
                else:
                    newlayer.setAbstract(f"Image: {imageid}\n Bands:{fmt_bands}")

                bb = QgsRectangle.fromWkt(extent)
                newlayer.setExtent(bb)
                QgsProject.instance().addMapLayer(newlayer)
                QgsProject.instance().layerTreeRoot().findLayer(
                    newlayer.id()
                ).setItemVisibilityChecked(False)

    def gee_layer_full_download(self):
        eelayer = self.iface.activeLayer()
        name = eelayer.name()
        if MISSINGAPI:
            QgsMessageLog.logMessage('Error to download the layer {}: The EE Python API (earthengine-api) must be installed and authenticated.'.format(name), 'GEE Data Catalog', level=Qgis.Critical)
            return
        imageid = eelayer.customProperty("ee-image-id")
        bands = eelayer.customProperty("ee-image-bands")
        scale = eelayer.customProperty("ee-image-scale")
        expression = eelayer.customProperty("ee-image-expression")
        proj = get_canvas_proj(self.iface)
        download_ee_image_layer(self.iface, name, imageid, bands, scale, proj, None, expression)

    def gee_layer_canvas_download(self):
        eelayer = self.iface.activeLayer()
        name = eelayer.name()
        if MISSINGAPI:
            QgsMessageLog.logMessage('Error to download the layer {}: The EE Python API (earthengine-api) must be installed and authenticated.'.format(name), 'GEE Data Catalog', level=Qgis.Critical)
            return
        imageid = eelayer.customProperty("ee-image-id")
        bands = eelayer.customProperty("ee-image-bands")
        scale = eelayer.customProperty("ee-image-scale")
        expression = eelayer.customProperty("ee-image-expression")
        extent = get_canvas_extent(self.iface)
        proj = get_canvas_proj(self.iface)
        download_ee_image_layer(self.iface, name, imageid, bands, scale, proj, extent, expression)

    def update_ee_image_layer(self, eelayer):
        if MISSINGAPI:
            QgsMessageLog.logMessage('Error updating the {} layer: The EE Python API (earthengine-api) must be installed and authenticated.'.format(eelayer.name()), 'GEE Data Catalog', level=Qgis.Critical)
            return
        extent = eelayer.customProperty("ee-image-wkt")
        bb = QgsRectangle.fromWkt(extent)
        eelayer.setExtent(bb)
        xml_file = eelayer.dataProvider().dataSourceUri()
        # ds = gdal.Open(xml_file)
        # if ds.ReadAsArray(xsize=1, ysize=1) is None:
        imageid = eelayer.customProperty("ee-image-id")
        bands = eelayer.customProperty("ee-image-bands")
        b_min = eelayer.customProperty("ee-image-b_min")
        b_max = eelayer.customProperty("ee-image-b_max")
        qml = eelayer.customProperty("ee-image-qml")
        palette = eelayer.customProperty("ee-image-palette")
        expression = eelayer.customProperty("ee-image-expression")
        # if b_min is not None:
        #     b_min = list(map(int, b_min))
        # if b_max is not None:
        #     b_max = list(map(int, b_max))
        nbands = len(bands) if palette is None else 3
        if self.ee_uninitialized:
            try:
                if self.ee_project is None:
                    QgsMessageLog.logMessage('About to initialize the earthengine API without a cloud project. Please assign it to the GOOGLE_CLOUD_PROJECT environment variable and restart QGIS.', 'EE Python API', level=Qgis.Critical)
                else:
                    QgsMessageLog.logMessage(f'About to initialize the earthengine API with the {self.ee_project} cloud project.', 'EE Python API', level=Qgis.Info)
                ee.Initialize(project=self.ee_project)
                self.ee_uninitialized = False
            except ee.ee_exception.EEException as e:
                QgsMessageLog.logMessage('Error updating the {} layer: {}'.format(eelayer.name(), e), 'EE Python API', level=Qgis.Critical)
                return
        rgb = update_ee_image(imageid, bands, b_min, b_max, palette, expression, qml)
        tms = get_ee_image_tms(rgb)
        url = tms_to_gdalurl(tms)
        new_xml = get_gdal_xml(url, nbands+1)
        write_xmlfile(new_xml, name=None, dest=xml_file)
        eelayer.dataProvider().reloadData()
        eelayer.triggerRepaint()
        eelayer.reload()

    def update_ee_image_layers(self):
        layers = QgsProject.instance().mapLayers().values()
        for eelayer in filter(
            lambda layer: layer.customProperty("ee-image") == "XML", layers
        ):
            self.update_ee_image_layer(eelayer)
        self.iface.mapCanvas().refresh()

    def update_dlg_fields(self, new_collection):
        """Update list of band combinations and availability from selected collection"""

        self.dlg.bands.clear()  # This will remove all previous items
        self.dlg.bands.addItems(GEE_DATASETS[new_collection]["bandcombinations"].keys())
        self.dlg.infotext.setPlainText(GEE_DATASETS[new_collection]["description"])
        if "cloudfield" in GEE_DATASETS[new_collection]:
            self.dlg.cloudcover.setEnabled(True)
        else:
            self.dlg.cloudcover.setEnabled(False)
        # date availability
        if "availability" in GEE_DATASETS[new_collection]:
            self.dlg.startdate.setEnabled(True)
            self.dlg.enddate.setEnabled(True)
            mindate = GEE_DATASETS[new_collection]["availability"][0].split("-")
            year, month, day = int(mindate[0]), int(mindate[1]), int(mindate[2])
            self.dlg.startdate.setMinimumDate(QDate(year, month, day))
            self.dlg.enddate.setMinimumDate(QDate(year, month, day))
            if GEE_DATASETS[new_collection]["availability"][1] is None:
                self.dlg.startdate.setMaximumDate(QDate.currentDate())
                self.dlg.enddate.setMaximumDate(QDate.currentDate().addDays(1))
                self.dlg.startdate.setDate(
                    QDate.currentDate().addDays(-3)
                )  # to fill default date
            else:
                maxdate = GEE_DATASETS[new_collection]["availability"][1].split("-")
                year, month, day = int(maxdate[0]), int(maxdate[1]), int(maxdate[2])
                self.dlg.startdate.setMaximumDate(QDate(year, month, day))
                self.dlg.enddate.setMaximumDate(QDate(year, month, day).addDays(1))
                self.dlg.startdate.setDate(
                    QDate(year, month, day).addDays(-3)
                )  # to fill default date
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
            self.dlg.finished.connect(self.result)  # connects with result function.

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
        # self.dlg.destination_folder.setText( "Temporary Output" )
        self.dlg.default_folder = QgsProject.instance().absolutePath() or os.getcwd()
        self.dlg.open()

    def result(self, result):
        
        # See if OK was pressed
        if result:

            if MISSINGAPI:
                self.iface.messageBar().pushMessage("The EE Python API (earthengine-api) must be installed and authenticated. Please see the instructions in https://github.com/sandroklippel/qgis_gee_data_catalog.", Qgis.Critical, 0)
                return
            elif self.ee_uninitialized:
                try:
                    if self.ee_project is None:
                        QgsMessageLog.logMessage('About to initialize the earthengine API without a cloud project. Please assign it to the GOOGLE_CLOUD_PROJECT environment variable and restart QGIS.', 'EE Python API', level=Qgis.Critical)
                    else:
                        QgsMessageLog.logMessage(f'About to initialize the earthengine API with the {self.ee_project} cloud project.', 'EE Python API', level=Qgis.Info)
                    ee.Initialize(project=self.ee_project)
                    self.ee_uninitialized = False
                except ee.ee_exception.EEException as e:
                    self.iface.messageBar().pushMessage(title="EE Python API Error", text=str(e), level=Qgis.Critical, duration=0)
                    return
                except OSError:
                    self.iface.messageBar().pushMessage(text="Fail to establish connection with the earthengine server", level=Qgis.Critical, duration=-1)
                    return

            # search ee images
            collection = self.dlg.collection.currentText()
            startdate = (
                self.dlg.startdate.date().toString("yyyy-MM-dd")
                if "availability" in GEE_DATASETS[collection]
                else None
            )
            enddate = (
                self.dlg.enddate.date().toString("yyyy-MM-dd")
                if "availability" in GEE_DATASETS[collection]
                else None
            )
            cloudcover = (
                int(self.dlg.cloudcover.cleanText())
                if "cloudfield" in GEE_DATASETS[collection]
                else None
            )
            destination_folder = str(self.dlg.destination_folder.text())
            limit = int(self.dlg.limit.cleanText())
            addlayer = self.dlg.addlayer.isChecked()

            vis_params = GEE_DATASETS[collection]["bandcombinations"][
                self.dlg.bands.currentText()
            ]
            bands = vis_params["bands"]
            scale = vis_params["scale"]
            suffix = vis_params.get("suffix", "")
            b_min = vis_params.get("min", None)
            b_max = vis_params.get("max", None)
            palette = vis_params.get("palette", None)
            expression = vis_params.get("expression", None)
            qml = (
                os.path.join(self.plugin_dir, vis_params["qml"])
                if "qml" in vis_params
                else None
            )


            # need to test if it is a valid epsg proj
            # if someone else, set to 4326
            # QgsProject.instance().setCrs(QgsCoordinateReferenceSystem(4326)) <- qgis.core

            if "namefield" in GEE_DATASETS[collection]:
                images_list = search_ee_collection(
                    collection=GEE_DATASETS[collection].get("id", collection),
                    extent=get_canvas_extent(self.iface),
                    proj=get_canvas_proj(self.iface),
                    startdate=startdate,
                    enddate=enddate,
                    cloudfield=GEE_DATASETS[collection].get("cloudfield", None),
                    cloudcover=cloudcover,
                    namefield=GEE_DATASETS[collection]["namefield"],
                    bands=bands,
                    limit=limit,
                )
            else:
                images_list = [
                    [GEE_DATASETS[collection].get("id", collection), collection, None]
                ]

            if images_list and addlayer:
                for imageid, name, date in images_list:
                    add_ee_image_layer(
                        imageid=imageid,
                        name=name + suffix,
                        date=date,
                        bands=bands,
                        scale=scale,
                        b_min=b_min,
                        b_max=b_max,
                        palette=palette,
                        expression=expression,
                        qml=qml,
                        extent=GEE_DATASETS[collection].get("extent", None),
                        destination=destination_folder,
                    )
            elif not images_list:
                self.iface.messageBar().pushMessage("Search did not return any image")
            else:
                images_number = len(images_list)
                images_text = "images" if images_number > 1 else "image"
                self.iface.messageBar().pushMessage(
                    f"Search returned {images_number} {images_text}"
                )
