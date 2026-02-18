import re


def normalize_expression(expr: str) -> str:
    """
    Converte notação matemática informal para sintaxe python válida.

    Suportado:
        2x          -> 2*x
        2(x+1)      -> 2*(x+1)
        (x+1)(x-1)  -> (x+1)*(x-1)
        3pi         -> 3*pi
        pi x        -> pi*x
        sin x       -> sin(x)
        x^2         -> x**2
    """

    expr = expr.strip()

    #  potência
    expr = expr.replace("^", "**")

    # Converter sin x -> sin(x)
    expr = re.sub(r"\b(sin|cos|tan|sqrt|ln|log|exp)\s+([a-zA-Z0-9\(]+)",
                  r"\1(\2)", expr)

    # Remover espaços extras
    expr = re.sub(r"\s+", "", expr)

    ###
    # Inserir multiplicação implícita
    ###
    # número seguido de variável ou (
    expr = re.sub(r"(\d)([a-zA-Z(])", r"\1*\2", expr)
    # variável ou constante seguido de número
    expr = re.sub(r"([a-zA-Z\)])(\d)", r"\1*\2", expr)
    # ) seguido de (
    expr = re.sub(r"\)\(", r")*(", expr)
    # ) seguido de variável
    expr = re.sub(r"\)([a-zA-Z])", r")*\1", expr)
    # variável seguida de (
    expr = re.sub(r"([a-zA-Z])\(", r"\1*(", expr)

    
    # Corrigir funções quebradas (sin*(...)
    expr = re.sub(r"\b(sin|cos|tan|sqrt|ln|log|exp)\*\(",
                  r"\1(", expr)

    return expr
