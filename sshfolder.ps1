$windowsPath = $PWD.Path
$pythonScript = Join-Path -Path $PSScriptRoot -ChildPath "convert.py"
$linuxPath = python $pythonScript $windowsPath

Write-Output "Local Path: $windowsPath"
Write-Output "Linux Path: $linuxPath"

$escapedLinuxPath = $linuxPath -replace "'", "'\''"

ssh -t jacob@192.168.1.193 "cd '$escapedLinuxPath'; bash --login"