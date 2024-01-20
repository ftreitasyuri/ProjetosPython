$exclude = @("venv", "MyFirstBot.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "MyFirstBot.zip" -Force