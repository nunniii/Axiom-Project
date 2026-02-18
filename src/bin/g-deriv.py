
import matplotlib
matplotlib.use("TkAgg")
import sys
import numpy as np
import matplotlib.pyplot as plt
import math

from expr_parser import normalize_expression
from matplotlib.widgets import Slider



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
    print("g-deriv <x0> <expressao>")
    print("Exemplo:")
    print('g-deriv 1 "sin x"')


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


# 🔥 Derivada  
def derivative(expr, x, h=1e-6):
    return (
        safe_eval(expr, x + h) - safe_eval(expr, x - h)
    ) / (2 * h)



def plot_tangent(x0_initial, expr):
    xs = np.linspace(x0_initial - 5, x0_initial + 5, 2000)

    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.25)

    ax = setup_cartesian()

    ys = np.array([safe_eval(expr, x) for x in xs])
    function_line, = ax.plot(xs, ys, linewidth=2.5, label="f(x)")

    # Linha tangente inicial
    y0 = safe_eval(expr, x0_initial)
    slope = derivative(expr, x0_initial)
    tangent = y0 + slope * (xs - x0_initial)

    tangent_line, = ax.plot(xs, tangent, linestyle="--", linewidth=2, label="Tangente")

    point = ax.scatter([x0_initial], [y0], zorder=5)

    ax.legend()

    # Slider
    ax_slider = plt.axes([0.2, 0.1, 0.6, 0.03])
    slider = Slider(ax_slider, "x0", xs.min(), xs.max(), valinit=x0_initial)

    def update(val):
        x0 = slider.val
        y0 = safe_eval(expr, x0)
        slope = derivative(expr, x0)
        tangent = y0 + slope * (xs - x0)

        tangent_line.set_ydata(tangent)
        point.set_offsets([[x0, y0]])

        fig.canvas.draw_idle()

    slider.on_changed(update)

    plt.title(f"Reta tangente de {expr}")
    plt.xlabel("x")
    plt.ylabel("y")

    plt.show()

def main():
    args = sys.argv

    if len(args) != 3:
        print_usage()
        return

    x0_raw = args[1]
    expr_raw = args[2]

    expr = normalize_expression(expr_raw)

    try:
        x0 = float(eval(x0_raw, {"__builtins__": {}}, {"pi": math.pi}))

        slope = derivative(expr, x0)
        print(f"f'({x0}) ≈ {slope}")

        plot_tangent(x0, expr)

    except Exception as e:
        print("Erro:", e)


if __name__ == "__main__":
    main()
