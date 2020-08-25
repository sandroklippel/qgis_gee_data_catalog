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

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

# import os

# from qgis.PyQt import uic
from qgis.PyQt import QtWidgets

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
# FORM_CLASS, _ = uic.loadUiType(os.path.join(
#     os.path.dirname(__file__), 'qgis_gee_data_catalog_dialog_base.ui'))

from .qgis_gee_data_catalog_dialog_base import Ui_GeeDataCatalogDialogBase


class GeeDataCatalogDialog(QtWidgets.QDialog, Ui_GeeDataCatalogDialogBase):
    def __init__(self, parent=None):
        """Constructor."""
        super(GeeDataCatalogDialog, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
