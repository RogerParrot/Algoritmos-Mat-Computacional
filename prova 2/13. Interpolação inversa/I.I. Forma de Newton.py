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
    
    # O primeiro coeficiente é simplesmente y[0]
    coeficientes[0] = y_tab[0]
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

def newton_inverso(y_alvo, x_tab, y_tab, tol=1e-6, max_iter=100):
    """
    Encontra o valor de x correspondente a um valor específico de y usando
    interpolação de Newton inversa
    """
    # Calcula os coeficientes do polinômio de Newton
    coeficientes = FormaDeNewton(x_tab, y_tab)
    
    # Criar intervalo inicial baseado nos pontos disponíveis
    x_min, x_max = min(x_tab), max(x_tab)
    
    for _ in range(max_iter):
        # Dividir o intervalo ao meio
        x_test = (x_min + x_max) / 2
        y_atual = avalia_newton(x_test, x_tab, coeficientes)
        
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
x_tab = np.array([1., 2., 4.])
y_tab = np.array([2., 3., 5.])

# Calcula os coeficientes
coeficientes = FormaDeNewton(x_tab, y_tab)

# Cria pontos para plotagem suave
x_plot = np.linspace(min(x_tab)-0.5, max(x_tab)+0.5, 1000)
y_plot = np.array([avalia_newton(x, x_tab, coeficientes) for x in x_plot])

# Exemplos de valores y para encontrar seus xs correspondentes
valores_y = [2.5, 3.5, 4.5]
print("Buscando valores x para diferentes valores y:")
for y_alvo in valores_y:
    x_encontrado = newton_inverso(y_alvo, x_tab, y_tab)
    print(f"y = {y_alvo:.2f}: x ≈ {x_encontrado:.4f}")

# Plotagem
plt.figure(figsize=(10, 6))
plt.plot(x_plot, y_plot, 'b-', label='Polinômio de Newton')
plt.scatter(x_tab, y_tab, color='red', marker='o', s=100,
           label='Pontos de Interpolação')

# Marcar os pontos encontrados
for y_alvo in valores_y:
    x_encontrado = newton_inverso(y_alvo, x_tab, y_tab)
    plt.scatter(x_encontrado, y_alvo, color='green', marker='*', s=150,
               label=f'y = {y_alvo}')

plt.grid(True)
plt.legend()
plt.title('Interpolação Polinomial de Newton')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

print("\nVerificação dos pontos originais:")
for i in range(len(x_tab)):
    valor_calculado = avalia_newton(x_tab[i], x_tab, coeficientes)
    print(f"Ponto ({x_tab[i]}, {y_tab[i]}): valor calculado = {valor_calculado:.2f}")

print("\nCoeficientes do polinômio de Newton:")
print(coeficientes)