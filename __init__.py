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
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load GeeDataCatalog class from file GeeDataCatalog.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .qgis_gee_data_catalog import GeeDataCatalog
    return GeeDataCatalog(iface)
