# Teste 2

vetor = [5, 3, 2, 4, 7, 1, 0, 6]

def bubble_sort(vetor):
    n = len(vetor)
    for i in range(n):
        for j in range(0, n - i - 1):
            if vetor[j] > vetor[j + 1]:
                vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]


bubble_sort(vetor)

print("Vetor ordenado:", vetor)

# utilizando o método (sorted) nativo do python, podemos realizar ordenação de maneira mais rapida e eficiente.

# Ordenando utilizando "sorted"
def ordenacao_sorted(vetor):    
    return sorted(vetor)

print("Vetor ordenado com 'sorted':", ordenacao_sorted(vetor))