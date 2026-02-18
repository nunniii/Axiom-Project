import sys
import sympy as sp


def main():
    args = sys.argv

    if len(args) != 3:
        print_usage()
        return

    # 🔥 Agora primeiro vem o ponto
    try:
        x_value = float(args[1])
    except ValueError:
        print("Erro ao interpretar o ponto numérico.")
        return

    # Depois vem a expressão
    expr_str = args[2].replace("^", "**")

    x = sp.Symbol("x")

    try:
        expr = sp.sympify(expr_str)
    except Exception:
        print("Erro ao interpretar a expressão.")
        return

    # Derivada simbólica
    derivative = sp.diff(expr, x)

    # Avaliação numérica
    result = derivative.subs(x, x_value).evalf()

    print(result)


def print_usage():
    print("Uso:")
    print('deriv <valor-x0> "expressao"')
    print("Exemplo:")
    print('deriv 1.5 "x^3 + 2*x"')


if __name__ == "__main__":
    main()
