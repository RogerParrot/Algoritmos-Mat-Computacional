def Lagrange(x, x_tab, y_tab):
    n = len(x_tab)
    soma = 0
    
    for i in range(n):
        l = 1  # Inicializa o polinômio base L_k(x)
        
        for j in range(n):
            if i != j:  # Evita divisão por zero
                l *= (x - x_tab[j]) / (x_tab[i] - x_tab[j])
        
        soma += y_tab[i] * l  # Soma ponderada pelos valores y
    
    return soma
