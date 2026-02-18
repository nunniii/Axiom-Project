## 📐 Expressões Suportadas

A expressão deve:

- Usar `*` para multiplicação (ex: `2*x`)
- Usar `^` para potência (ex: `x^3`)
- Estar entre aspas
- Utilizar `x` como variável

### 🔢 Operadores

| Operador | Significado |
|-----------|------------|
| `+` | Soma |
| `-` | Subtração |
| `*` | Multiplicação |
| `/` | Divisão |
| `^` | Potência |

---

### 📚 Funções Matemáticas Disponíveis

| Função | Descrição |
|--------|------------|
| `sqrt(x)` | Raiz quadrada |
| `sin(x)` | Seno (em radianos) |
| `cos(x)` | Cosseno |
| `tan(x)` | Tangente |
| `ln(x)` | Logaritmo natural |
| `exp(x)` | Exponencial (e^x) |

Constantes suportadas:

- `pi`

---

### 🧪 Exemplos de Uso

```bash
cargo run --bin newton 0 1 "2*x^3"
cargo run --bin newton 0 pi "sin(x)"
cargo run --bin newton 0 4 "sqrt(x)"
cargo run --bin newton 1 2 "ln(x)"



Importante

- Multiplicação implícita não é suportada (2x não funciona).

- Use sempre * (ex: 2*x).

- Os ângulos das funções trigonométricas estão em radianos.