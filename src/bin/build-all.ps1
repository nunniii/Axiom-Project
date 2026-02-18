# build-all.ps1
# Build de todos os executáveis Python/ cargo não foi incluso

$scripts = @(
    "deriv.py",
    "g-deriv.py",
    "newton.py"
    "g-newton.py"
)

$binDir = ".\bin"

Write-Host "`n[CLEAN] Removendo builds antigos..."

if (Test-Path ".\build") { Remove-Item ".\build" -Recurse -Force }
if (Test-Path ".\dist") { Remove-Item ".\dist" -Recurse -Force }
Get-ChildItem -Filter "*.spec" | Remove-Item -Force

if (!(Test-Path $binDir)) {
    New-Item -ItemType Directory -Path $binDir | Out-Null
}

foreach ($script in $scripts) {

    if (Test-Path $script) {

        Write-Host "`n[BUILD] Gerando $script ..."

        python -m PyInstaller `
            --onefile `
            --clean `
            --hidden-import expr_parser `
            $script

        $exeName = [System.IO.Path]::GetFileNameWithoutExtension($script) + ".exe"
        $distPath = ".\dist\$exeName"

        if (Test-Path $distPath) {
            Write-Host "[COPY] Copiando $exeName para /bin ..."
            Copy-Item $distPath "$binDir\$exeName" -Force
        }
        else {
            Write-Host "[ERRO] $exeName não encontrado em dist."
        }

    }
    else {
        Write-Host "[ERRO] Arquivo $script não encontrado."
    }
}

Write-Host "[OK] Build finalizada com sucesso!"
