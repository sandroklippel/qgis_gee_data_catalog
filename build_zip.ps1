# plugin files
$filesToInclude = @(
    ".\__init__.py",
    ".\datasets.json",
    ".\ee_interface.py",
    ".\icon.svg",
    ".\icon.png",
    ".\iface_utils.py",
    ".\LICENSE",
    ".\metadata.txt",
    ".\misc_utils.py",
    ".\qgis_gee_data_catalog.py",
    ".\qgis_gee_data_catalog_dialog.py",
    ".\qgis_gee_data_catalog_dialog_base.py",
    ".\qgis_gee_data_catalog_dialog_base.ui",
    ".\read_datasets.py",
    ".\README.md",
    ".\resources.py"
    ".\qml\lossyear.qml",
    ".\qml\mapbiomas-legend-collection90.qml",
    ".\qml\mapbiomas-legend-collection90_pt_BR.qml",
    ".\qml\palsar_fnf.qml",
    ".\qml\palsar_fnf4.qml",
    ".\qml\sentinel2_scl.qml",
    ".\qml\treecover2000.qml"
)

# target dir
$buildDirectory = "qgis_gee_data_catalog" 

# output zip file
$zipFilePath = "qgis_gee_data_catalog.zip"

# current dir
$scriptDirectory = Split-Path -Parent $MyInvocation.MyCommand.Definition

# relative to absolute paths
$filesToInclude = $filesToInclude | ForEach-Object { Join-Path $scriptDirectory $_ }
$buildDirectory = Join-Path $scriptDirectory $buildDirectory
$zipFilePath = Join-Path $scriptDirectory $zipFilePath

# remove old zip and target dir
if (Test-Path $buildDirectory) {
    Remove-Item $buildDirectory -Recurse -Force
}
if (Test-Path $zipFilePath) {
    Remove-Item $zipFilePath -Force
}

# new target dir
New-Item -ItemType Directory -Path $buildDirectory | Out-Null

# copy files
foreach ($file in $filesToInclude) {
    Copy-Item $file -Destination $buildDirectory
}


Compress-Archive -Path $buildDirectory -DestinationPath $zipFilePath


# remove target dir
Remove-Item $buildDirectory -Recurse -Force

Write-Output "Plug-in ZIP file '$zipFilePath' successfully created!"