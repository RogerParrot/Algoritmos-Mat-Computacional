import numpy as np
import matplotlib.pyplot as plt

def newton_cotes(a, b, n, f):
    x = np.linspace(a, b, n + 1)  # Divisão do intervalo em n subintervalos
    h = (b - a) / n  # Espaçamento entre pontos

    # Coeficientes de Newton-Cotes para regras simples (exemplo: Trapézio)
    if n == 1:  
        A = np.array([1, 1]) * (h / 2)  # Regra do Trapézio
    elif n == 2:
        A = np.array([1, 4, 1]) * (h / 3)  # Regra de Simpson 1/3
    elif n == 3:
        A = np.array([1, 3, 3, 1]) * (3 * h / 8)  # Regra de Simpson 3/8
    else:
        raise ValueError("Apenas regras de grau até 3 são suportadas no momento.")

    integral = np.sum(A * f(x))  # Aplicação da fórmula de Newton-Cotes

    # Gráfico da função e dos pontos usados na quadratura
    plt.plot(x, f(x), 'bo-', label="Amostras da função")
    plt.fill_between(x, f(x), alpha=0.3, color="gray")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Integração por Newton-Cotes")
    plt.legend()
    plt.show()

    return integral

# Exemplo de uso com uma função simples
f = lambda x: np.sin(x)  # Função a ser integrada
resultado = newton_cotes(0, np.pi, 2, f)
print("Valor da integral aproximada:", resultado)
