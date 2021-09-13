<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis version="3.18.3-Zürich" minScale="1e+08" styleCategories="AllStyleCategories" maxScale="0" hasScaleBasedVisibilityFlag="0">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
    <Private>0</Private>
  </flags>
  <temporal fetchMode="0" mode="0" enabled="0">
    <fixedRange>
      <start></start>
      <end></end>
    </fixedRange>
  </temporal>
  <customproperties>
    <property key="WMSBackgroundLayer" value="false"/>
    <property key="WMSPublishDataSourceUrl" value="false"/>
    <property key="ee-image" value="MEM"/>
    <property key="ee-image-b_max" value="100"/>
    <property key="ee-image-b_min" value="0"/>
    <property key="ee-image-bands" value="treecover2000"/>
    <property key="ee-image-date"/>
    <property key="ee-image-id" value="UMD/hansen/global_forest_change_2020_v1_8"/>
    <property key="ee-image-palette"/>
    <property key="ee-image-qml"/>
    <property key="ee-image-scale" value="926"/>
    <property key="ee-image-wkt" value="POLYGON((-20037508.34278924390673637 -20037508.34278925508260727,&#xa;                            20037508.34278924390673637 -20037508.34278925508260727, &#xa;                            20037508.34278924390673637 20037508.34278924390673637, &#xa;                            -20037508.34278924390673637 20037508.34278924390673637, &#xa;                            -20037508.34278924390673637 -20037508.34278925508260727))"/>
    <property key="embeddedWidgets/count" value="0"/>
    <property key="identify/format" value="Value"/>
  </customproperties>
  <pipe>
    <provider>
      <resampling maxOversampling="2" zoomedOutResamplingMethod="nearestNeighbour" zoomedInResamplingMethod="nearestNeighbour" enabled="false"/>
    </provider>
    <rasterrenderer alphaBand="2" type="singlebandpseudocolor" nodataColor="" opacity="1" band="1" classificationMin="0" classificationMax="20">
      <rasterTransparency/>
      <minMaxOrigin>
        <limits>None</limits>
        <extent>WholeRaster</extent>
        <statAccuracy>Estimated</statAccuracy>
        <cumulativeCutLower>0.02</cumulativeCutLower>
        <cumulativeCutUpper>0.98</cumulativeCutUpper>
        <stdDevFactor>2</stdDevFactor>
      </minMaxOrigin>
      <rastershader>
        <colorrampshader maximumValue="20" minimumValue="0" labelPrecision="0" colorRampType="INTERPOLATED" classificationMode="2" clip="0">
          <colorramp name="[source]" type="gradient">
            <Option type="Map">
              <Option name="color1" type="QString" value="43,131,186,255"/>
              <Option name="color2" type="QString" value="215,25,28,255"/>
              <Option name="discrete" type="QString" value="0"/>
              <Option name="rampType" type="QString" value="gradient"/>
              <Option name="stops" type="QString" value="0.25;171,221,164,255:0.5;255,255,191,255:0.75;253,174,97,255"/>
            </Option>
            <prop v="43,131,186,255" k="color1"/>
            <prop v="215,25,28,255" k="color2"/>
            <prop v="0" k="discrete"/>
            <prop v="gradient" k="rampType"/>
            <prop v="0.25;171,221,164,255:0.5;255,255,191,255:0.75;253,174,97,255" k="stops"/>
          </colorramp>
          <item alpha="255" label="0" color="#2b83ba" value="0"/>
          <item alpha="255" label="1" color="#4696b6" value="1.052631578947368"/>
          <item alpha="255" label="2" color="#61a9b1" value="2.105263157894737"/>
          <item alpha="255" label="3" color="#7cbcac" value="3.157894736842105"/>
          <item alpha="255" label="4" color="#97cfa8" value="4.2105263157894735"/>
          <item alpha="255" label="5" color="#b0dfa6" value="5.263157894736842"/>
          <item alpha="255" label="6" color="#c1e6ab" value="6.315789473684211"/>
          <item alpha="255" label="7" color="#d3eeb1" value="7.36842105263158"/>
          <item alpha="255" label="8" color="#e5f5b7" value="8.421052631578947"/>
          <item alpha="255" label="9" color="#f7fcbc" value="9.473684210526315"/>
          <item alpha="255" label="11" color="#fff7b5" value="10.526315789473683"/>
          <item alpha="255" label="12" color="#ffe6a1" value="11.578947368421051"/>
          <item alpha="255" label="13" color="#fed58e" value="12.631578947368421"/>
          <item alpha="255" label="14" color="#fec47a" value="13.68421052631579"/>
          <item alpha="255" label="15" color="#feb266" value="14.736842105263158"/>
          <item alpha="255" label="16" color="#f79756" value="15.789473684210526"/>
          <item alpha="255" label="17" color="#ef7747" value="16.842105263157894"/>
          <item alpha="255" label="18" color="#e75839" value="17.894736842105264"/>
          <item alpha="255" label="19" color="#df382a" value="18.94736842105263"/>
          <item alpha="255" label="20" color="#d7191c" value="20"/>
          <rampLegendSettings prefix="" orientation="2" useContinuousLegend="1" minimumLabel="" suffix="" direction="0" maximumLabel="">
            <numericFormat id="basic">
              <Option type="Map">
                <Option name="decimal_separator" type="QChar" value=""/>
                <Option name="decimals" type="int" value="6"/>
                <Option name="rounding_type" type="int" value="0"/>
                <Option name="show_plus" type="bool" value="false"/>
                <Option name="show_thousand_separator" type="bool" value="true"/>
                <Option name="show_trailing_zeros" type="bool" value="false"/>
                <Option name="thousand_separator" type="QChar" value=""/>
              </Option>
            </numericFormat>
          </rampLegendSettings>
        </colorrampshader>
      </rastershader>
    </rasterrenderer>
    <brightnesscontrast brightness="0" contrast="0" gamma="1"/>
    <huesaturation saturation="0" colorizeRed="255" colorizeOn="0" grayscaleMode="0" colorizeStrength="100" colorizeGreen="128" colorizeBlue="128"/>
    <rasterresampler maxOversampling="2"/>
    <resamplingStage>resamplingFilter</resamplingStage>
  </pipe>
  <blendMode>0</blendMode>
</qgis>
