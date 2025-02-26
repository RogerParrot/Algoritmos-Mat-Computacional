import numpy as np
import matplotlib.pyplot as plt

def minimos_quadrados(f, x, y, tipo_func):
    """
    Função para calcular os coeficientes da reta que melhor se ajusta aos dados
    usando o método dos mínimos quadrados.

    Parâmetros:
    x (numpy array): Valores do eixo x (variável independente).
    y (numpy array): Valores do eixo y (variável dependente).

    Retorna:
    a (float): Coeficiente angular da reta.
    b (float): Coeficiente linear da reta.
    """
        
    n = len(x)
    
    # Cálculo dos coeficientes a e b
    a = (n * np.sum(x * y) - np.sum(x) * np.sum(y)) / (n * np.sum(x**2) - (np.sum(x))**2)
    b = (np.sum(y) - a * np.sum(x)) / n
    
    return a, b

# Dados de exemplo
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

# Calculando os coeficientes da reta
a, b = minimos_quadrados(x, y)
print(f"Coeficiente angular (a): {a}")
print(f"Coeficiente linear (b): {b}")

# Plotando os dados
plt.scatter(x, y, color='blue', label='Dados')

# Plotando a reta ajustada
y_ajustado = a * x + b
plt.plot(x, y_ajustado, color='red', label='Reta Ajustada')

# Adicionando legendas e título
plt.xlabel('x')
plt.ylabel('y')
plt.title('Método dos Mínimos Quadrados')
plt.legend()

# Mostrando o gráfico
plt.show()