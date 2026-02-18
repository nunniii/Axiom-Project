import sys
import math
from expr_parser import normalize_expression


def print_usage():
    print("Uso:")
    print("newton <a> <b> <expressao>")
    print("Exemplo:")
    print('python newton.py 0 1 "2*x**3"')
    print()
    print("⚠️ Integração indefinida não funciona nesta versão.");


def safe_eval(expr, x):
    allowed = {
        "x": x,
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "sqrt": math.sqrt,
        "ln": math.log,
        "log": math.log,
        "exp": math.exp,
        "pi": math.pi,
        "e": math.e,
        "abs": abs
    }

    return eval(expr, {"__builtins__": {}}, allowed)


def integrate_simpson(f, a, b, n=1000):
    if n % 2 != 0:
        n += 1  # exige n par

    h = (b - a) / n
    total = f(a) + f(b)

    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            total += 2 * f(x)
        else:
            total += 4 * f(x)

    return total * h / 3


def main():
    args = sys.argv

    if len(args) != 4:
        print_usage()
        return

    a_raw = args[1]
    b_raw = args[2]
    expr_raw = args[3]

    try:
        # normaliza expressão
        expr = normalize_expression(expr_raw)

        # avalia limites
        a = float(eval(a_raw, {"__builtins__": {}}, {"pi": math.pi}))
        b = float(eval(b_raw, {"__builtins__": {}}, {"pi": math.pi}))

        # Cria função
        def f(x):
            return safe_eval(expr, x)

        result = integrate_simpson(f, a, b, 1000)

        print(
            f"∫[{a}, {b}] {expr} dx ≈ {result}"
        )


    except Exception as e:
        print("Erro:", e)


if __name__ == "__main__":
    main()
