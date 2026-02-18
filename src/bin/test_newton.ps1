Write-Host "==============================="
Write-Host "Testes do binário NEWTON"
Write-Host "==============================="

function Run-Test {
    param (
        [string]$Description,
        [string]$Command
    )

    Write-Host ""
    Write-Host "Teste: $Description"
    Write-Host "Comando: $Command"
    Write-Host "--------------------------------"

    Invoke-Expression $Command
}





Run-Test "Polinômio simples" `
    'cargo run --bin newton 0 1 "2*x^3"'

Run-Test "Potência x^2" `
    'cargo run --bin newton 0 2 "x^2"'

Run-Test "Raiz quadrada" `
    'cargo run --bin newton 0 4 "sqrt(x)"'

Run-Test "Trigonométrica sin(x) de 0 a pi" `
    'cargo run --bin newton 0 pi "sin(x)"'

Run-Test "Logaritmo natural ln(x)" `
    'cargo run --bin newton 1 2 "ln(x)"'

Run-Test "Função composta" `
    'cargo run --bin newton 0 1 "x^2 + 3*x + 1"'

Run-Test "Exponencial" `
    'cargo run --bin newton 0 1 "exp(x)"'

Run-Test "Intervalo simétrico (-1,1)" `
    'cargo run --bin newton -1 1 "x^2"'

Write-Host ""
Write-Host "==============================="
Write-Host "Fim dos testes"
Write-Host "==============================="
