# Teste 4

def multiplos(limite):
    soma = 0
    
    for i in range(1, limite + 1):
        if i % 3 == 0 or i % 5 == 0:
            soma += i
            
    return soma


try:
    limite = int(input("Digite o valor para a soma dos múltiplos de 3 e 5: "))
    resultado = multiplos(limite)
    print(f"A soma dos múltiplos de 3 ou 5 até {limite} é: {resultado}")
    
except ValueError:
    print("Por favor, digite um número inteiro!")
 
