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

## [0.1.0] - 2020-05-31

### Added

- Search images collections by canvas extent, date and cloud cover.
- Add image layers as WMS/TMS by GDAL XML in memory.
- Add custom properties to layers to save with project file
- Rebuild XML in memory by project read. **It still not working properly**. Some working in qgis bad layers handler mechanism will be needed.
- Download to GDrive by options in context menu (full image and clip to canvas extent).
- Sentinel-2 collections (SR and TOA) and Landsat 8 Tier 1 and 2
