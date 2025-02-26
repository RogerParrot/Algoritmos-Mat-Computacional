import numpy as np
import matplotlib.pyplot as plt

def Lagrange(x, x_tab, y_tab):
    """
    Calcula o valor do polinômio interpolador de Lagrange em um ponto x
    Parâmetros:
        x -- ponto onde calcular o valor do polinômio
        x_tab -- array numpy com os pontos x de interpolação
        y_tab -- array numpy com os valores correspondentes y
    Retorna:
        Valor do polinômio interpolador em x
    """
    n = len(x_tab)
    soma = np.zeros_like(x)  
    for i in range(n):
        l = np.ones_like(x)  
        for j in range(n):
            if i != j:
                l *= (x - x_tab[j]) / (x_tab[i] - x_tab[j])
        soma += y_tab[i] * l
    return soma

def Lagrange_Inverso(y_alvo, x_tab, y_tab, tol=1e-6, max_iter=100):
    """
    Encontra o valor de x correspondente a um valor específico de y usando interpolação de Lagrange inversa
    Parâmetros:
        y_alvo -- valor y alvo para encontrar o x correspondente
        x_tab -- array numpy com os pontos x de interpolação
        y_tab -- array numpy com os valores correspondentes y
        tol -- tolerância para o erro (padrão: 1e-6)
        max_iter -- número máximo de iterações (padrão: 100)
    Retorna:
        Valor aproximado de x que produz o valor y_alvo
    """
    # Criar intervalo inicial baseado nos pontos disponíveis
    x_min, x_max = min(x_tab), max(x_tab)
    
    for _ in range(max_iter):
        # Dividir o intervalo ao meio
        x_test = (x_min + x_max) / 2
        y_atual = Lagrange(x_test, x_tab, y_tab)
        
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
x_tab = np.array([-1., 0., 2.])      # Pontos x de exemplo
y_tab = np.array([4., 1., -1.])      # Valores y correspondentes

# Criar pontos para plotagem suave
x_plot = np.linspace(min(x_tab)-0.5, max(x_tab)+0.5, 1000)
y_plot = Lagrange(x_plot, x_tab, y_tab)

# Exemplos de valores y para encontrar seus xs correspondentes
valores_y = [2.0, 0.0, -0.5]
print("Buscando valores x para diferentes valores y:")
for y_alvo in valores_y:
    x_encontrado = Lagrange_Inverso(y_alvo, x_tab, y_tab)
    print(f"y = {y_alvo:.2f}: x ≈ {x_encontrado:.4f}")

# Plotar o gráfico
plt.figure(figsize=(10, 6))
plt.plot(x_plot, y_plot, 'b-', label='Polinômio Interpolador')
plt.scatter(x_tab, y_tab, color='red', marker='o', s=100,
           label='Pontos de Interpolação')

# Marcar os pontos encontrados
for y_alvo in valores_y:
    x_encontrado = Lagrange_Inverso(y_alvo, x_tab, y_tab)
    plt.scatter(x_encontrado, y_alvo, color='green', marker='*', s=150,
               label=f'y = {y_alvo}')

plt.grid(True)
plt.legend()
plt.title('Interpolação Polinomial de Lagrange')
plt.xlabel('x')
plt.ylabel('y')
plt.show()