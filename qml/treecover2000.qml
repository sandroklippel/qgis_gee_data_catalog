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
    <rasterrenderer alphaBand="2" type="singlebandpseudocolor" nodataColor="" opacity="1" band="1" classificationMin="0" classificationMax="100">
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
        <colorrampshader maximumValue="100" minimumValue="0" labelPrecision="0" colorRampType="INTERPOLATED" classificationMode="2" clip="0">
          <colorramp name="[source]" type="gradient">
            <Option type="Map">
              <Option name="color1" type="QString" value="255,255,204,255"/>
              <Option name="color2" type="QString" value="0,104,55,255"/>
              <Option name="discrete" type="QString" value="0"/>
              <Option name="rampType" type="QString" value="gradient"/>
              <Option name="stops" type="QString" value="0.25;194,230,153,255:0.5;120,198,121,255:0.75;49,163,84,255"/>
            </Option>
            <prop v="255,255,204,255" k="color1"/>
            <prop v="0,104,55,255" k="color2"/>
            <prop v="0" k="discrete"/>
            <prop v="gradient" k="rampType"/>
            <prop v="0.25;194,230,153,255:0.5;120,198,121,255:0.75;49,163,84,255" k="stops"/>
          </colorramp>
          <item alpha="255" label="0%" color="#ffffcc" value="0"/>
          <item alpha="255" label="1%" color="#fdfeca" value="1.01010101010101"/>
          <item alpha="255" label="2%" color="#fbfdc8" value="2.02020202020202"/>
          <item alpha="255" label="3%" color="#f8fcc6" value="3.03030303030303"/>
          <item alpha="255" label="4%" color="#f6fbc4" value="4.040404040404041"/>
          <item alpha="255" label="5%" color="#f3fac2" value="5.050505050505051"/>
          <item alpha="255" label="6%" color="#f1f9c0" value="6.060606060606061"/>
          <item alpha="255" label="7%" color="#eef8be" value="7.070707070707071"/>
          <item alpha="255" label="8%" color="#ecf7bc" value="8.080808080808081"/>
          <item alpha="255" label="9%" color="#e9f6ba" value="9.090909090909092"/>
          <item alpha="255" label="10%" color="#e7f5b8" value="10.101010101010102"/>
          <item alpha="255" label="11%" color="#e4f4b6" value="11.111111111111112"/>
          <item alpha="255" label="12%" color="#e2f3b3" value="12.121212121212121"/>
          <item alpha="255" label="13%" color="#dff2b1" value="13.131313131313131"/>
          <item alpha="255" label="14%" color="#ddf1af" value="14.141414141414142"/>
          <item alpha="255" label="15%" color="#daf0ad" value="15.151515151515152"/>
          <item alpha="255" label="16%" color="#d8efab" value="16.161616161616163"/>
          <item alpha="255" label="17%" color="#d5eea9" value="17.171717171717173"/>
          <item alpha="255" label="18%" color="#d3eda7" value="18.181818181818183"/>
          <item alpha="255" label="19%" color="#d0eca5" value="19.191919191919194"/>
          <item alpha="255" label="20%" color="#ceeba3" value="20.202020202020204"/>
          <item alpha="255" label="21%" color="#cceaa1" value="21.212121212121215"/>
          <item alpha="255" label="22%" color="#c9e99f" value="22.222222222222225"/>
          <item alpha="255" label="23%" color="#c7e89d" value="23.232323232323235"/>
          <item alpha="255" label="24%" color="#c4e79b" value="24.242424242424242"/>
          <item alpha="255" label="25%" color="#c2e699" value="25.252525252525253"/>
          <item alpha="255" label="26%" color="#bfe597" value="26.262626262626263"/>
          <item alpha="255" label="27%" color="#bce396" value="27.272727272727273"/>
          <item alpha="255" label="28%" color="#b9e295" value="28.282828282828284"/>
          <item alpha="255" label="29%" color="#b6e194" value="29.292929292929294"/>
          <item alpha="255" label="30%" color="#b3e092" value="30.303030303030305"/>
          <item alpha="255" label="31%" color="#afde91" value="31.313131313131315"/>
          <item alpha="255" label="32%" color="#acdd90" value="32.323232323232325"/>
          <item alpha="255" label="33%" color="#a9dc8e" value="33.333333333333336"/>
          <item alpha="255" label="34%" color="#a6da8d" value="34.343434343434346"/>
          <item alpha="255" label="35%" color="#a3d98c" value="35.35353535353536"/>
          <item alpha="255" label="36%" color="#a0d88a" value="36.36363636363637"/>
          <item alpha="255" label="37%" color="#9dd789" value="37.37373737373738"/>
          <item alpha="255" label="38%" color="#9ad588" value="38.38383838383839"/>
          <item alpha="255" label="39%" color="#97d487" value="39.3939393939394"/>
          <item alpha="255" label="40%" color="#94d385" value="40.40404040404041"/>
          <item alpha="255" label="41%" color="#91d184" value="41.41414141414142"/>
          <item alpha="255" label="42%" color="#8ed083" value="42.42424242424243"/>
          <item alpha="255" label="43%" color="#8bcf81" value="43.43434343434344"/>
          <item alpha="255" label="44%" color="#88cd80" value="44.44444444444445"/>
          <item alpha="255" label="45%" color="#85cc7f" value="45.45454545454546"/>
          <item alpha="255" label="46%" color="#82cb7e" value="46.46464646464647"/>
          <item alpha="255" label="47%" color="#7fca7c" value="47.47474747474748"/>
          <item alpha="255" label="48%" color="#7cc87b" value="48.484848484848484"/>
          <item alpha="255" label="49%" color="#79c77a" value="49.494949494949495"/>
          <item alpha="255" label="51%" color="#77c678" value="50.505050505050505"/>
          <item alpha="255" label="52%" color="#74c477" value="51.515151515151516"/>
          <item alpha="255" label="53%" color="#71c375" value="52.525252525252526"/>
          <item alpha="255" label="54%" color="#6ec174" value="53.535353535353536"/>
          <item alpha="255" label="55%" color="#6bc072" value="54.54545454545455"/>
          <item alpha="255" label="56%" color="#68be71" value="55.55555555555556"/>
          <item alpha="255" label="57%" color="#65bd6f" value="56.56565656565657"/>
          <item alpha="255" label="58%" color="#62bc6e" value="57.57575757575758"/>
          <item alpha="255" label="59%" color="#5fba6c" value="58.58585858585859"/>
          <item alpha="255" label="60%" color="#5db96b" value="59.5959595959596"/>
          <item alpha="255" label="61%" color="#5ab769" value="60.60606060606061"/>
          <item alpha="255" label="62%" color="#57b668" value="61.61616161616162"/>
          <item alpha="255" label="63%" color="#54b566" value="62.62626262626263"/>
          <item alpha="255" label="64%" color="#51b365" value="63.63636363636364"/>
          <item alpha="255" label="65%" color="#4eb263" value="64.64646464646465"/>
          <item alpha="255" label="66%" color="#4bb062" value="65.65656565656566"/>
          <item alpha="255" label="67%" color="#48af60" value="66.66666666666667"/>
          <item alpha="255" label="68%" color="#46ad5f" value="67.67676767676768"/>
          <item alpha="255" label="69%" color="#43ac5d" value="68.68686868686869"/>
          <item alpha="255" label="70%" color="#40ab5c" value="69.6969696969697"/>
          <item alpha="255" label="71%" color="#3da95a" value="70.70707070707071"/>
          <item alpha="255" label="72%" color="#3aa859" value="71.71717171717172"/>
          <item alpha="255" label="73%" color="#37a657" value="72.72727272727273"/>
          <item alpha="255" label="74%" color="#34a556" value="73.73737373737374"/>
          <item alpha="255" label="75%" color="#31a354" value="74.74747474747475"/>
          <item alpha="255" label="76%" color="#2fa153" value="75.75757575757576"/>
          <item alpha="255" label="77%" color="#2d9f52" value="76.76767676767678"/>
          <item alpha="255" label="78%" color="#2b9d51" value="77.77777777777779"/>
          <item alpha="255" label="79%" color="#299a4f" value="78.7878787878788"/>
          <item alpha="255" label="80%" color="#27984e" value="79.7979797979798"/>
          <item alpha="255" label="81%" color="#25954d" value="80.80808080808082"/>
          <item alpha="255" label="82%" color="#23934c" value="81.81818181818183"/>
          <item alpha="255" label="83%" color="#21914b" value="82.82828282828284"/>
          <item alpha="255" label="84%" color="#1f8e4a" value="83.83838383838385"/>
          <item alpha="255" label="85%" color="#1d8c48" value="84.84848484848486"/>
          <item alpha="255" label="86%" color="#1b8947" value="85.85858585858587"/>
          <item alpha="255" label="87%" color="#198746" value="86.86868686868688"/>
          <item alpha="255" label="88%" color="#178545" value="87.87878787878789"/>
          <item alpha="255" label="89%" color="#158244" value="88.8888888888889"/>
          <item alpha="255" label="90%" color="#138042" value="89.89898989898991"/>
          <item alpha="255" label="91%" color="#117d41" value="90.90909090909092"/>
          <item alpha="255" label="92%" color="#0f7b40" value="91.91919191919193"/>
          <item alpha="255" label="93%" color="#0d793f" value="92.92929292929294"/>
          <item alpha="255" label="94%" color="#0b763e" value="93.93939393939395"/>
          <item alpha="255" label="95%" color="#09743d" value="94.94949494949496"/>
          <item alpha="255" label="96%" color="#07713b" value="95.95959595959597"/>
          <item alpha="255" label="97%" color="#056f3a" value="96.96969696969697"/>
          <item alpha="255" label="98%" color="#036d39" value="97.97979797979798"/>
          <item alpha="255" label="99%" color="#016a38" value="98.98989898989899"/>
          <item alpha="255" label="100%" color="#006837" value="100"/>
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
