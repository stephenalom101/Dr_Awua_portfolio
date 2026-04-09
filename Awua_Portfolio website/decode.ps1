$ErrorActionPreference = 'Stop'

try {
    $b64_seplat = Get-Content -Path "tmp_seplat_b64.txt" -Raw
    $b64_seplat = $b64_seplat -replace '\s+', ''
    $bytes_seplat = [Convert]::FromBase64String($b64_seplat)
    [IO.File]::WriteAllBytes("logo_seplat.png", $bytes_seplat)
    Write-Output "Successfully decoded logo_seplat.png"
} catch {
    Write-Error "Failed to decode logo_seplat.png: $_"
}

try {
    $b64_shell = Get-Content -Path "tmp_shell_b64.txt" -Raw
    $b64_shell = $b64_shell -replace '\s+', ''
    $bytes_shell = [Convert]::FromBase64String($b64_shell)
    [IO.File]::WriteAllBytes("logo_shell.png", $bytes_shell)
    Write-Output "Successfully decoded logo_shell.png"
} catch {
    Write-Error "Failed to decode logo_shell.png: $_"
}
