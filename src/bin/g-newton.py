import sys
import subprocess
import numpy as np
import matplotlib.pyplot as plt
import math

from expr_parser import normalize_expression

# estilo
plt.style.use("seaborn-v0_8-whitegrid")
plt.rcParams.update({
    "figure.figsize": (10, 6),
    "axes.edgecolor": "#333333",
    "axes.linewidth": 1.2,
    "axes.labelsize": 12,
    "axes.titlesize": 14,
    "font.size": 11
})


def setup_cartesian():
    ax = plt.gca()

    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")

    ax.spines["right"].set_color("none")
    ax.spines["top"].set_color("none")

    ax.grid(True, linestyle="--", alpha=0.4)

    return ax


def print_usage():
    print("Uso:")
    print("python newton.py <a> <b> <expressao>")
    print('Exemplo: python newton.py 0 1 "2*x**3"')


# Compila expressão 
def compile_expression(expr):
    """
    usa as funções de numpy em vez de math para permitir arrays
    """

    allowed = {
        "sin": np.sin,
        "cos": np.cos,
        "tan": np.tan,
        "sqrt": np.sqrt,
        "ln": np.log,
        "log": np.log,
        "exp": np.exp,
        "pi": np.pi,
        "e": np.e,
        "abs": np.abs
    }

    code = compile(expr, "<string>", "eval")

    def f(x):
        return eval(code, {"__builtins__": {}}, {**allowed, "x": x})

    return f


def plot_defined(a, b, expr):
    xs = np.linspace(a, b, 2000)

    f = compile_expression(expr)

    # Avaliação vetorizada
    ys = f(xs)

    plt.figure()
    ax = setup_cartesian()

    ax.plot(xs, ys, linewidth=2.5)
    ax.fill_between(xs, ys, alpha=0.35)

    plt.title(f"∫ de {expr} de {a} até {b}")
    plt.xlabel("x")
    plt.ylabel("f(x)")

    plt.show()


def main():
    args = sys.argv

    if len(args) != 4:
        print_usage()
        return

    a = args[1]
    b = args[2]
    expr = normalize_expression(args[3])

    try:
        result = subprocess.run(
            ["newton.exe", a, b, expr],
            capture_output=True,
            text=True
        )

        print(result.stdout)

        a_val = float(eval(a, {"__builtins__": {}}, {"pi": math.pi}))
        b_val = float(eval(b, {"__builtins__": {}}, {"pi": math.pi}))

        plot_defined(a_val, b_val, expr)

    except Exception as e:
        print("Erro:", e)


if __name__ == "__main__":
    main()
