# ![icon](icon.svg) Google Earth Engine Data Catalog

Search, view and download satellite imagery and geospatial datasets from Google Earth Engine.
A Google Earth Engine account linked to a Cloud Project is required. 
Additionally, the EE Python API (earthengine-api) must be installed and authenticated.

To install on Windows (OSGeo4W Shell):
```
python -m pip install --upgrade pip
python -m pip install earthengine-api --user
```

To install on Linux (Ubuntu based):
```
sudo apt update
sudo apt upgrade
sudo apt install python3-pip
pip3 install earthengine-api --user
```

To authenticate on QGIS Terminal Python (Ctrl+Alt+P):
```
import ee
ee.Authenticate()
```

The output credentials file will be located in:

Windows: %USERPROFILE%\.config\earthengine 
Linux: $HOME/.config/earthengine 

The Cloud Project name must be assigned to EEPROJECT environment variable. 
This can be done in QGIS (Settings -> Options -> System -> Environment).