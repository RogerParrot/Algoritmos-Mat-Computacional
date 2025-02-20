import numpy as np
import matplotlib.pyplot as plt

def criando_matriz_vandermonde(x, grau):
    """
    Cria uma matriz de Vandermonde para interpolação polinomial
    Args:
        x: Array com os pontos x
        grau: Grau do polinômio desejado
    Returns:
        Matriz de Vandermonde
    """
    n = len(x)
    V = np.zeros((n, grau + 1))
    for i in range(n):
        for j in range(grau + 1):
            V[i][j] = pow(x[i], j)
    return V

def eliminacao_numpy(A, b):
    """
    Implementação da eliminação gaussiana usando numpy arrays
    Args:
        A: Matriz do sistema (numpy array)
        b: Vetor de termos independentes (numpy array)
    Returns:
        Matriz triangular superior e vetor modificado
    """
    n = len(A)
    A = A.copy()
    b = b.copy()
    for k in range(min(n, A.shape[1])):
        if A[k][k] == 0:
            raise ValueError("Matriz singular, não é possível continuar.")
        for i in range(k+1, n):
            m = A[i][k] / A[k][k]
            A[i] -= m * A[k]
            b[i] -= m * b[k]
    return A, b

def resolucao_sistema_numpy(A, b):
    """
    Resolve o sistema triangular superior usando numpy arrays
    Args:
        A: Matriz triangular superior (numpy array)
        b: Vetor modificado (numpy array)
    Returns:
        Solução do sistema
    """
    n = len(A)
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        if i < A.shape[1] and A[i][i] != 0:
            j_max = min(i+1, A.shape[1])
            s = np.sum(A[i][i+1:j_max] * x[i+1:j_max])
            x[i] = (b[i] - s) / A[i][i]
    return x

def interpolacao_vandermonde(x, y, grau):
    """
    Realiza interpolação polinomial usando matriz de Vandermonde
    Args:
        x: Array com os pontos x
        y: Array com os valores correspondentes
        grau: Grau do polinômio desejado
    Returns:
        Coeficientes do polinômio
    """
    V = criando_matriz_vandermonde(x, grau)
    
    # Criar visualização da matriz de Vandermonde
    plt.figure(figsize=(12, 4))
    plt.subplot(131)
    plt.imshow(V, cmap='viridis')
    plt.colorbar(label='Valor')
    plt.title('Matriz de Vandermonde\nVisualização Heatmap')
    
    # Adicionar valores na matriz
    for i in range(V.shape[0]):
        for j in range(V.shape[1]):
            plt.text(j, i, f'{V[i,j]:.2f}', ha='center', va='center')
            
    print("\nMatriz de Vandermonde:")
    print(V)
    print("\nDimensões da matriz:", V.shape)
    print("Dimensões do vetor y:", y.shape)
    
    A, b = eliminacao_numpy(V, y)
    
    # Plotar matriz após eliminação gaussiana
    plt.subplot(132)
    plt.imshow(A, cmap='viridis')
    plt.colorbar(label='Valor')
    plt.title('Matriz Após Eliminação Gaussiana\nVisualização Heatmap')
    
    # Adicionar valores na matriz
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            plt.text(j, i, f'{A[i,j]:.2f}', ha='center', va='center')
            
    print("\nMatriz após eliminação gaussiana:")
    print(A)
    print("\nDimensões da matriz após eliminação:", A.shape)
    
    coeficientes = resolucao_sistema_numpy(A, b)
    return coeficientes

def avalia_polinomio(coeficientes, x):
    """
    Avalia o polinômio nos pontos x
    Args:
        coeficientes: Lista com os coeficientes do polinômio
        x: Pontos onde avaliar o polinômio
    Returns:
        Valores do polinômio nos pontos x
    """
    resultado = np.zeros_like(x)
    for i, coef in enumerate(coeficientes):
        resultado += coef * np.power(x, i)
    return resultado

# Exemplo de uso
x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 2, 4, 6, 8])

# Calcular coeficientes
coeficientes = interpolacao_vandermonde(x, y, len(x)-1)

# Criar pontos para plotagem suave
x_plot = np.linspace(min(x)-0.5, max(x)+0.5, 1000)
y_plot = avalia_polinomio(coeficientes, x_plot)

# Plotar o gráfico final
plt.figure(figsize=(10, 6))
plt.plot(x_plot, y_plot, 'b-', label='Polinômio Interpolador')
plt.scatter(x, y, color='red', marker='o', s=100,
           label='Pontos de Interpolação')
plt.grid(True)
plt.legend()
plt.title('Interpolação Polinomial de Vandermonde')
plt.xlabel('x')
plt.ylabel('y')

print("\nCoeficientes do polinômio:")
print(coeficientes)

plt.show()