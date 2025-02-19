# OBS: CORRIGIR ERRO 2.00e+00 NO GRÁFICO

import numpy as np
import matplotlib.pyplot as plt

def FormaDeNewton(x_tab, y_tab):
    """
    Calcula o polinômio interpolador usando a forma de Newton
    
    Parâmetros:
    x_tab -- array numpy com os pontos x de interpolação
    y_tab -- array numpy com os valores correspondentes y
    
    Retorna:
    coeficientes -- array com os coeficientes do polinômio de Newton
    """
    n = len(x_tab)
    coeficientes = np.zeros(n)
    diferenças = y_tab.copy()  # Inicializa com os valores y
    
    # Calcula as diferenças divididas iterativamente
    for ordem in range(1, n):
        for i in range(n - ordem):
            # Calcula a diferença dividida de ordem atual
            diferenças[i] = (diferenças[i + 1] - diferenças[i]) / (x_tab[i + ordem] - x_tab[i])
        coeficientes[ordem] = diferenças[0]
    
    return coeficientes

def avalia_newton(x, x_tab, coeficientes):
    """
    Avalia o polinômio de Newton em um ponto x
    
    Parâmetros:
    x -- ponto onde avaliar o polinômio
    x_tab -- array com os pontos x originais
    coeficientes -- array com os coeficientes calculados
    
    Retorna:
    valor do polinômio em x
    """
    resultado = coeficientes[0]
    for i in range(1, len(coeficientes)):
        termo = coeficientes[i]
        for j in range(i):
            termo *= (x - x_tab[j])
        resultado += termo
    return resultado

# Exemplo de uso
x_tab = np.array([1., 2., 3., 4.])
y_tab = np.array([2., 3., 5., 7.])

# Calcula os coeficientes
coeficientes = FormaDeNewton(x_tab, y_tab)

# Cria pontos para plotagem suave
x_plot = np.linspace(min(x_tab)-0.5, max(x_tab)+0.5, 1000)
y_plot = np.array([avalia_newton(x, x_tab, coeficientes) for x in x_plot])

# Plotagem
plt.figure(figsize=(10, 6))
plt.plot(x_plot, y_plot, 'b-', label='Polinômio de Newton')
plt.scatter(x_tab, y_tab, color='red', marker='o', s=100, 
           label='Pontos de Interpolação')
plt.grid(True)
plt.legend()
plt.title('Interpolação Polinomial de Newton')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

print("Coeficientes do polinômio de Newton:")
print(coeficientes)