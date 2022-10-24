# ![icon](icon.svg) Google Earth Engine Data Catalog

Search, view and download satellite imagery and geospatial datasets from Google Earth Engine. EE Python API (earthengine-api) must be installed and it is required a Google Earth Engine account, besides authenticate it.
To install on Windows (OSGeo4W Shell):
> python -m pip install --upgrade pip
> python -m pip install earthengine-api --user
To install on Linux (Ubuntu based):
$ sudo apt update
$ sudo apt upgrade
$ sudo apt install python3-pip
To authenticate on python prompt(python/python3):
>>> import ee
>>> ee.Authenticate(auth_mode='notebook')
