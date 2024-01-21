$exclude = @("venv", "ContosoFaturas.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "ContosoFaturas.zip" -Force