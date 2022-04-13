# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

### Added

### Changed

### Deprecated

### Removed

### Fixed

### Security

## [0.4.3] - 2022-04-12

### Added

  - Landsat 9 OLI-2 datasets.

### Changed

  - Updated Landsat to collection 2.

## [0.4.2] - 2021-09-12

### Added

  - Planet & NICFI Basemaps for Tropical Forest Monitoring datasets.
  - Hansen Global Forest Change v1.8 (2000-2020) dataset.

## [0.4.1] - 2020-10-13

### Fixed

 - No longer restart the output directory, closing issue #3.
 - Single band dataset min/max conf.
 - Signal disconnect on plugin unload.

## [0.4.0] - 2020-10-01

### Added

 - On search, save the xml files in an output directory instead of the temporary folder  (thanks to @roya0045).
 - Option in context menu to renew XML file.
 - If available, load translated qml file

### Changed

 - Updated to Mapbiomas collection 5.0.

### Fixed

 - Palsar_fnf and sentinel2_scl qml files.
 - Rewrite xml files on project load.

## [0.3.0] - 2020-08-10

### Changed

- Icon.
- Save the XML definition file.
- Update layers on project read.
- Initialized ee library only once and after plugin loading.
- ALOS/PALSAR/FNF dataset availability until 2018-01-01.

## [0.2.1] - 2020-06-29

### Fixed

- UI bug, closing issue #1.

### Changed

- Removed some plugin-builder stuff. 
- Using compiled Python code rather than load the user interface description file. 

## [0.2.0] - 2020-06-23

### Added

- Handle exception error when internet connection fails on ee.Initialize (OSError).
- Dict format description on datasets.py.
- Band combination Shortwave infrared 3 (B12-B8A-B2) in Sentinel2 datasets.
- Scene Classification Map band for Sentinel 2 SR dataset.
- Global extent datasets: ALOS DEM, PALSAR FNF, Global Forest Canopy Height.
- ASTER radiance and ALOS/AVNIR-2 datasets.
- MapBiomas datasets (Annual Land Use Land Cover Maps of Brazil).
- Loading qml for singleband/palleted pseudo color datasets (qml dir).
- TOA and raw datasets for Landsat 8 and 5.
- HSV Pan-sharpened images for TOA Landsat 8 and 5 datasets. 
- Landsat 7 and 4 datasets (SR, TOA and raw).
- MSS for Landsat 4 and 5.
- Contrast enhancement to full ee.image layer before loaded.
- Set layer abstract with info about image date.
- Sentinel as tag and ee_plugin as dependency in metadata.txt.

### Changed

- Fields in GEE_DATASETS (datasets.py).
- Can add single layers datasets too.
- Split utils.py into iface_utils.py and misc_utils.py

### Removed

- Layers rebuilding on project read, since it does not work with the qgis bad layers handler mechanism.

## [0.1.0] - 2020-05-31

### Added

- Search images collections by canvas extent, date and cloud cover.
- Add image layers as WMS/TMS by GDAL XML in memory.
- Add custom properties to layers to save with project file
- Rebuild XML in memory by project read. **It still not working properly**. Some working in qgis bad layers handler mechanism will be needed.
- Download to GDrive by options in context menu (full image and clip to canvas extent).
- Sentinel-2 collections (SR and TOA) and Landsat 8 Tier 1 and 2
