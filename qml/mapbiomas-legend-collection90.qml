<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis maxScale="0" styleCategories="AllStyleCategories" hasScaleBasedVisibilityFlag="0" minScale="1e+08" version="3.28.3-Firenze">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
    <Private>0</Private>
  </flags>
  <temporal enabled="0" mode="0" fetchMode="0">
    <fixedRange>
      <start></start>
      <end></end>
    </fixedRange>
  </temporal>
  <elevation enabled="0" symbology="Line" zoffset="0" band="1" zscale="1">
    <data-defined-properties>
      <Option type="Map">
        <Option value="" type="QString" name="name"/>
        <Option name="properties"/>
        <Option value="collection" type="QString" name="type"/>
      </Option>
    </data-defined-properties>
    <profileLineSymbol>
      <symbol frame_rate="10" clip_to_extent="1" force_rhr="0" type="line" name="" alpha="1" is_animated="0">
        <data_defined_properties>
          <Option type="Map">
            <Option value="" type="QString" name="name"/>
            <Option name="properties"/>
            <Option value="collection" type="QString" name="type"/>
          </Option>
        </data_defined_properties>
        <layer pass="0" enabled="1" class="SimpleLine" locked="0">
          <Option type="Map">
            <Option value="0" type="QString" name="align_dash_pattern"/>
            <Option value="square" type="QString" name="capstyle"/>
            <Option value="5;2" type="QString" name="customdash"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="customdash_map_unit_scale"/>
            <Option value="MM" type="QString" name="customdash_unit"/>
            <Option value="0" type="QString" name="dash_pattern_offset"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="dash_pattern_offset_map_unit_scale"/>
            <Option value="MM" type="QString" name="dash_pattern_offset_unit"/>
            <Option value="0" type="QString" name="draw_inside_polygon"/>
            <Option value="bevel" type="QString" name="joinstyle"/>
            <Option value="133,182,111,255" type="QString" name="line_color"/>
            <Option value="solid" type="QString" name="line_style"/>
            <Option value="0.6" type="QString" name="line_width"/>
            <Option value="MM" type="QString" name="line_width_unit"/>
            <Option value="0" type="QString" name="offset"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="offset_map_unit_scale"/>
            <Option value="MM" type="QString" name="offset_unit"/>
            <Option value="0" type="QString" name="ring_filter"/>
            <Option value="0" type="QString" name="trim_distance_end"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="trim_distance_end_map_unit_scale"/>
            <Option value="MM" type="QString" name="trim_distance_end_unit"/>
            <Option value="0" type="QString" name="trim_distance_start"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="trim_distance_start_map_unit_scale"/>
            <Option value="MM" type="QString" name="trim_distance_start_unit"/>
            <Option value="0" type="QString" name="tweak_dash_pattern_on_corners"/>
            <Option value="0" type="QString" name="use_custom_dash"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="width_map_unit_scale"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </profileLineSymbol>
    <profileFillSymbol>
      <symbol frame_rate="10" clip_to_extent="1" force_rhr="0" type="fill" name="" alpha="1" is_animated="0">
        <data_defined_properties>
          <Option type="Map">
            <Option value="" type="QString" name="name"/>
            <Option name="properties"/>
            <Option value="collection" type="QString" name="type"/>
          </Option>
        </data_defined_properties>
        <layer pass="0" enabled="1" class="SimpleFill" locked="0">
          <Option type="Map">
            <Option value="3x:0,0,0,0,0,0" type="QString" name="border_width_map_unit_scale"/>
            <Option value="133,182,111,255" type="QString" name="color"/>
            <Option value="bevel" type="QString" name="joinstyle"/>
            <Option value="0,0" type="QString" name="offset"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="offset_map_unit_scale"/>
            <Option value="MM" type="QString" name="offset_unit"/>
            <Option value="35,35,35,255" type="QString" name="outline_color"/>
            <Option value="no" type="QString" name="outline_style"/>
            <Option value="0.26" type="QString" name="outline_width"/>
            <Option value="MM" type="QString" name="outline_width_unit"/>
            <Option value="solid" type="QString" name="style"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </profileFillSymbol>
  </elevation>
  <customproperties>
    <Option type="Map">
      <Option value="false" type="bool" name="WMSBackgroundLayer"/>
      <Option value="false" type="bool" name="WMSPublishDataSourceUrl"/>
      <Option value="0" type="int" name="embeddedWidgets/count"/>
      <Option value="Value" type="QString" name="identify/format"/>
    </Option>
  </customproperties>
  <pipe-data-defined-properties>
    <Option type="Map">
      <Option value="" type="QString" name="name"/>
      <Option name="properties"/>
      <Option value="collection" type="QString" name="type"/>
    </Option>
  </pipe-data-defined-properties>
  <pipe>
    <provider>
      <resampling enabled="false" zoomedInResamplingMethod="nearestNeighbour" zoomedOutResamplingMethod="nearestNeighbour" maxOversampling="2"/>
    </provider>
    <rasterrenderer opacity="1" alphaBand="-1" band="1" type="paletted" nodataColor="">
      <rasterTransparency/>
      <minMaxOrigin>
        <limits>None</limits>
        <extent>WholeRaster</extent>
        <statAccuracy>Estimated</statAccuracy>
        <cumulativeCutLower>0.02</cumulativeCutLower>
        <cumulativeCutUpper>0.98</cumulativeCutUpper>
        <stdDevFactor>2</stdDevFactor>
      </minMaxOrigin>
      <colorPalette>
        <paletteEntry value="3" color="#1f8d49" alpha="255" label="3 - Forest Formation"/>
        <paletteEntry value="4" color="#7dc975" alpha="255" label="4 - Savanna Formation"/>
        <paletteEntry value="5" color="#04381d" alpha="255" label="5 - Mangrove"/>
        <paletteEntry value="6" color="#007785" alpha="255" label="6 - Floodable Forest"/>
        <paletteEntry value="9" color="#7a5900" alpha="255" label="9 - Forest Plantation"/>
        <paletteEntry value="11" color="#519799" alpha="255" label="11 - Wetland"/>
        <paletteEntry value="12" color="#d6bc74" alpha="255" label="12 - Grassland"/>
        <paletteEntry value="15" color="#edde8e" alpha="255" label="15 - Pasture"/>
        <paletteEntry value="20" color="#db7093" alpha="255" label="20 - Sugar Cane"/>
        <paletteEntry value="21" color="#ffefc3" alpha="255" label="21 - Mosaic of Uses"/>
        <paletteEntry value="23" color="#ffa07a" alpha="255" label="23 - Beach, Dune and Sand Spot"/>
        <paletteEntry value="24" color="#d4271e" alpha="255" label="24 - Urban Area"/>
        <paletteEntry value="25" color="#db4d4f" alpha="255" label="25 - Other non Vegetated Areas"/>
        <paletteEntry value="29" color="#ffaa5f" alpha="255" label="29 - Rocky Outcrop"/>
        <paletteEntry value="30" color="#9c0027" alpha="255" label="30 - Mining"/>
        <paletteEntry value="31" color="#091077" alpha="255" label="31 - Aquaculture"/>
        <paletteEntry value="32" color="#fc8114" alpha="255" label="32 - Hypersaline Tidal Flat"/>
        <paletteEntry value="33" color="#2532e4" alpha="255" label="33 - River, Lake and Ocean"/>
        <paletteEntry value="35" color="#9065d0" alpha="255" label="35 - Palm Oil"/>
        <paletteEntry value="39" color="#f5b3c8" alpha="255" label="39 - Soybean"/>
        <paletteEntry value="40" color="#c71585" alpha="255" label="40 - Rice"/>
        <paletteEntry value="41" color="#f54ca9" alpha="255" label="41 - Other Temporary Crops"/>
        <paletteEntry value="46" color="#d68fe2" alpha="255" label="46 - Coffee"/>
        <paletteEntry value="47" color="#9932cc" alpha="255" label="47 - Citrus"/>
        <paletteEntry value="48" color="#e6ccff" alpha="255" label="48 - Other Perennial Crops"/>
        <paletteEntry value="49" color="#02d659" alpha="255" label="49 - Wooded Sandbank Vegetation"/>
        <paletteEntry value="50" color="#ad5100" alpha="255" label="50 - Herbaceous Sandbank Vegetation"/>
        <paletteEntry value="62" color="#ff69b4" alpha="255" label="62 - Cotton"/>
      </colorPalette>
      <colorramp type="randomcolors" name="[source]">
        <Option/>
      </colorramp>
    </rasterrenderer>
    <brightnesscontrast gamma="1" brightness="0" contrast="0"/>
    <huesaturation colorizeOn="0" colorizeGreen="128" grayscaleMode="0" colorizeRed="255" colorizeStrength="100" invertColors="0" colorizeBlue="128" saturation="0"/>
    <rasterresampler maxOversampling="2"/>
    <resamplingStage>resamplingFilter</resamplingStage>
  </pipe>
  <blendMode>0</blendMode>
</qgis>
