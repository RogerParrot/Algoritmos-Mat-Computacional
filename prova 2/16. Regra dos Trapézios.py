import numpy as np

def regra_dos_trapezios(f, a, b, intervalo=["quantidade de intervalos", 1]):
    """
    Implementa a regra dos trapézios para aproximar uma integral.
    
    Parâmetros:
        f: função a ser integrada
        a: limite inferior de integração
        b: limite superior de integração
        h: tamanho do intervalo (opcional)
        quant_interv: número de intervalos (opcional)
    """
    # Calcula o número de pontos baseado na quantidade de intervalos ou no tamanho dos intervalos
    # Quantidade de pontos é 1 a mais do que a quantidade de subintervalos
    if intervalo[0] == "tamanho dos intervalos":
        n = int((b - a)/intervalo[1])
        quant_pts = n + 1
    elif intervalo[0] == "quantidade de intervalos":
        n = intervalo[1]
        quant_pts = n + 1

    # Gera os pontos x
    x = np.linspace(a, b, quant_pts)
    
    # Calcula os valores da função
    y = f(x)
    
    # Aplica a regra dos trapézios
    integral = (x[1] - x[0]) * ((y[0] + y[-1])/2 + np.sum(y[1:-1]))
    
    return integral

def f(x):
    """
    Função exemplo para teste.
    Neste caso, uma função senoidal simples.
    """
    return x*(np.e**x)

# Exemplo de uso com diferentes números de intervalos
print(f"Aproximação da integral: {regra_dos_trapezios(f, 1.6, 2.0, ["quantidade de intervalos", 4])}")