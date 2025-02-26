import numpy as np
import matplotlib.pyplot as plt

def eliminacao(A, b):
    A = A.astype(float)
    b = b.astype(float)
    n = len(A)
    for k in range(n):
        for i in range(k+1, n):
            if A[k, k] == 0:
                raise ValueError("Matriz singular, não é possível continuar.")
            m = A[i, k] / A[k, k]
            for j in range(k, n):
                A[i, j] -= m * A[k, j]
            b[i] -= m * b[k]
    return A, b

def resolucao_sistema(A, b):
    n = len(A)
    x = np.zeros(n)
    x[n-1] = b[n-1] / A[n-1, n-1]
    for k in range(n-2, -1, -1):
        s = sum(A[k, j] * x[j] for j in range(k+1, n))
        x[k] = (b[k] - s) / A[k, k]
    return x

def vandermonde(x_points):
    n = len(x_points)
    V = np.vander(x_points, increasing=True)
    return V

def vandermonde_inverso(y_alvo, x_points, y_points, tol=1e-6, max_iter=100):
    """
    Encontra o valor de x correspondente a um valor específico de y usando
    interpolação de Vandermonde inversa
    """
    # Criar o polinômio interpolador
    V = vandermonde(x_points)
    A_tri, b_tri = eliminacao(V.copy(), y_points.copy())
    coeficientes = resolucao_sistema(A_tri, b_tri)
    p = np.poly1d(coeficientes[::-1])
    
    # Criar intervalo inicial baseado nos pontos disponíveis
    x_min, x_max = min(x_points), max(x_points)
    
    for _ in range(max_iter):
        # Dividir o intervalo ao meio
        x_test = (x_min + x_max) / 2
        y_atual = p(x_test)
        
        # Verificar se encontramos o valor desejado
        if abs(y_atual - y_alvo) < tol:
            return x_test
            
        # Atualizar o intervalo
        if y_atual < y_alvo:
            x_min = x_test
        else:
            x_max = x_test
            
        # Verificar se o intervalo ficou muito pequeno
        if abs(x_max - x_min) < tol:
            break
    
    return (x_min + x_max) / 2

# Exemplo de uso
x_points = np.array([0, 1, 2, 3])
y_points = np.array([0, 1, 4, 9])

# Criar o polinômio interpolador
V = vandermonde(x_points)
A_tri, b_tri = eliminacao(V.copy(), y_points.copy())
coeficientes = resolucao_sistema(A_tri, b_tri)
p = np.poly1d(coeficientes[::-1])

# Criar pontos para plotagem
x_range = np.linspace(min(x_points) - 1, max(x_points) + 1, 100)
y_range = p(x_range)

# Exemplos de valores y para encontrar seus xs correspondentes
valores_y = [2.0, 5.0, 7.0]
print("Buscando valores x para diferentes valores y:")
for y_alvo in valores_y:
    x_encontrado = vandermonde_inverso(y_alvo, x_points, y_points)
    print(f"y = {y_alvo:.2f}: x ≈ {x_encontrado:.4f}")

# Plotar o gráfico
plt.figure(figsize=(10, 6))
plt.scatter(x_points, y_points, color='red', marker='o', s=100,
           label='Pontos de interpolação')
plt.plot(x_range, y_range, 'b-', label='Polinômio interpolador')

# Marcar os pontos encontrados
for y_alvo in valores_y:
    x_encontrado = vandermonde_inverso(y_alvo, x_points, y_points)
    plt.scatter(x_encontrado, y_alvo, color='green', marker='*', s=150,
               label=f'y = {y_alvo}')

plt.grid(True)
plt.legend()
plt.title('Interpolação usando a matriz de Vandermonde')
plt.xlabel('x')
plt.ylabel('y')
plt.show()