# open-from-ssh.ps1
param([string]$LinuxPath)

# mappings.json already exists
$mappingPath = "C:\Users\jacob\source\repos\convert-windows-paths-to-linux\mappings.json"
$mappings = Get-Content $mappingPath | ConvertFrom-Json

# find mapping
foreach ($drive in $mappings.PSObject.Properties.Name) {
    $linuxRoot = $mappings.$drive.TrimEnd('/')
    if ($LinuxPath.StartsWith($linuxRoot)) {
        $relative = $LinuxPath.Substring($linuxRoot.Length).TrimStart('/') -replace "/", "\"
        explorer.exe "$drive:\$relative"
        exit 0
    }
}

Write-Error "No mapping found for $LinuxPath"
exit 1
