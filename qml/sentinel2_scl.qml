<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis version="3.12.3-București" minScale="1e+08" hasScaleBasedVisibilityFlag="0" maxScale="0" styleCategories="AllStyleCategories">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <pipe>
    <rasterrenderer alphaBand="2" classificationMax="11" type="singlebandpseudocolor" nodataColor="" band="1" opacity="1" classificationMin="1">
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
        <colorrampshader classificationMode="1" clip="0" colorRampType="EXACT">
          <colorramp name="[source]" type="gradient">
            <prop k="color1" v="215,25,28,255"/>
            <prop k="color2" v="43,131,186,255"/>
            <prop k="discrete" v="0"/>
            <prop k="rampType" v="gradient"/>
            <prop k="stops" v="0.25;253,174,97,255:0.5;255,255,191,255:0.75;171,221,164,255"/>
          </colorramp>
          <item value="1" alpha="255" label="Saturated or defective" color="#ff0004"/>
          <item value="2" alpha="255" label="Dark Area Pixels" color="#868686"/>
          <item value="3" alpha="255" label="Cloud Shadows" color="#774b0a"/>
          <item value="4" alpha="255" label="Vegetation" color="#10d22c"/>
          <item value="5" alpha="255" label="Bare Soils" color="#ffff52"/>
          <item value="6" alpha="255" label="Water" color="#0000ff"/>
          <item value="7" alpha="255" label="Clouds Low Probability / Unclassified" color="#818181"/>
          <item value="8" alpha="255" label="Clouds Medium Probability" color="#c0c0c0"/>
          <item value="9" alpha="255" label="Clouds High Probability" color="#f1f1f1"/>
          <item value="10" alpha="255" label="Cirrus" color="#bac5eb"/>
          <item value="11" alpha="255" label="Snow / Ice" color="#52fff9"/>
        </colorrampshader>
      </rastershader>
    </rasterrenderer>
    <brightnesscontrast brightness="0" contrast="0"/>
    <huesaturation grayscaleMode="0" colorizeStrength="100" colorizeRed="255" colorizeOn="0" colorizeBlue="128" saturation="0" colorizeGreen="128"/>
    <rasterresampler maxOversampling="2"/>
  </pipe>
  <blendMode>0</blendMode>
</qgis>
