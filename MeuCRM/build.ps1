$exclude = @("venv", "MeuCRM.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "MeuCRM.zip" -Force