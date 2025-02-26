import numpy as np

def regra_1terco_simpson(f, a, b, tam_div=1):
    """
    Implementa a Regra de Simpson de 1/3 para aproximar integrais definidas.
    
    Parâmetros:
        f: função de dentro da integral a ser integrada
        a: limite inferior da integral
        b: limite superior da integral
        tam_div: tamanho de cada subdivisão do intervalo [a, b]
        
    Retorna:
        Aproximação da integral usando a Regra de Simpson de 1/3
    """
    # Verifica se o tamanho da divisão é válido
    if tam_div <= 0:
        raise ValueError("O tamanho da divisão (tam_div) deve ser maior que zero.")
    
    # Calcula o número de subintervalos
    num_subintervalos = int((b - a) / tam_div)
    
    # Ajusta o tamanho da divisão para garantir que o intervalo seja coberto corretamente
    h = (b - a) / num_subintervalos
    
    # Inicializa a integral
    integral = 0.0
    
    # Aplica a Regra de Simpson de 1/3 em cada subintervalo
    for i in range(num_subintervalos):
        # Define os limites do subintervalo
        x0 = a + i * h
        x1 = x0 + h
        
        # Ponto médio do subintervalo
        pt_medio = (x0 + x1) / 2
        
        # Aplica a fórmula da Regra de Simpson de 1/3 no subintervalo
        integral += h * (f(x0) + 4 * f(pt_medio) + f(x1)) / 6
    
    return integral

def f(x):
    """
    Caso de teste: x*e^x
    Função que está dentro da integral
    """
    return np.e**x

# Exemplo de uso
a, b = 1, 2  # Limites de integração
tam_div = 0.1    # Tamanho de cada subdivisão

resultado = regra_1terco_simpson(f, a, b)
print(f"Resultado da regra de Simpson: {resultado:.06f}")