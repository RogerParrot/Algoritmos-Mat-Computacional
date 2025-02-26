import numpy as np
import matplotlib.pyplot as plt

def minimos_quadrados(x, y):
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

def linearizar(f, x, y, tipo_func):
    """
    Função para linearizar uma função não linear.

    Parâmetros:
    f (function): Função não linear.
    x (numpy array): Valores do eixo x (variável independente).
    y (numpy array): Valores do eixo y (variável dependente).
    tipo_func (str): Indica o tipo da função não linear de entrada ('quadratica', 'exponencial', 'logaritmica', etc.).

    Retorna:
    x_lin (numpy array): Valores de x transformados.
    y_lin (numpy array): Valores de y transformados.
    """

    # Parte onde ocorre a linearização:
    if tipo_func == 'quadratica':
        # Transformação para função quadrática: y = ax^2 + bx + c
        x_lin = x**2
        y_lin = y
    elif tipo_func == 'exponencial':
        # Transformação para função exponencial: y = ae^(bx)
        y_lin = np.log(y)
        x_lin = x
    elif tipo_func == 'logaritmica':
        # Transformação para função logarítmica: y = a ln(x) + b
        x_lin = np.log(x)
        y_lin = y
    else:
        raise ValueError("Tipo de função não suportado.")
    
    return x_lin, y_lin

# Dados de exemplo (função quadrática)
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

# Tipo de função não linear
tipo_func = 'quadratica'

# Linearizando os dados
x_lin, y_lin = linearizar(None, x, y, tipo_func)

# Calculando os coeficientes da reta ajustada
a, b = minimos_quadrados(x_lin, y_lin)
print(f"Coeficiente angular (a): {a}")
print(f"Coeficiente linear (b): {b}")

# Plotando os dados originais
plt.scatter(x, y, color='blue', label='Dados Originais')

# Plotando a curva ajustada
if tipo_func == 'quadratica':
    y_ajustado = a * x**2 + b
elif tipo_func == 'exponencial':
    y_ajustado = np.exp(a * x + b)
elif tipo_func == 'logaritmica':
    y_ajustado = a * np.log(x) + b

plt.plot(x, y_ajustado, color='red', label='Curva Ajustada')

# Adicionando legendas e título
plt.xlabel('x')
plt.ylabel('y')
plt.title(f'Ajuste de Função {tipo_func.capitalize()}')
plt.legend()

# Mostrando o gráfico
plt.show()