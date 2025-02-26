import numpy as np

def regra_1terco_simpson(f, a, b, intervalo=["quantidade de intervalos", 1]):
    """
    Implementa a Regra de Simpson de 1/3 para aproximar integrais definidas.
    
    Parâmetros:
        f: função a ser integrada
        a: limite inferior da integral
        b: limite superior da integral
        tam_int: tamanho dos intervalos (opcional)
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
    
    # Aplica a Regra de Simpson de 1/3
    h = x[1] - x[0]
    soma_pontos_finais = y[0] + y[-1]
    soma_pontos_medios = np.sum(y[1:-1:2]) * 4  # Pontos ímpares multiplicados por 4
    soma_pontos_pares = np.sum(y[2:-1:2]) * 2   # Pontos pares multiplicados por 2
    
    integral = (h/3) * (soma_pontos_finais + soma_pontos_medios + soma_pontos_pares)
    
    return integral

def f(x):
    """Função teste: x*e^x"""
    return np.e**x

# Exemplo de uso
resultado = regra_1terco_simpson(f, 1.6, 2.0)
print(f"Resultado da integral: {resultado:.06f}")