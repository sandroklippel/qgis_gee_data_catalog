""" QGIS iface utilities functions
"""

def get_canvas_proj(iface):
    return iface.mapCanvas().mapSettings().destinationCrs().authid()

def get_canvas_extent(iface):
    extent = iface.mapCanvas().extent()
    xmin = extent.xMinimum()
    ymin = extent.yMinimum()
    xmax = extent.xMaximum()
    ymax = extent.yMaximum()
    return [xmin, ymin, xmax, ymax]