# Teste 3

def calcular_fatorial(numero):
    if numero < 0:
        return "Números negativos não tem Fatorial!"
    
    fatorial = 1
    
    for i in range(1, numero + 1):
        fatorial *= i
        
    return fatorial


try:
    num = int(input("Digite um número inteiro e positivo para calcular o fatorial: "))
    resultado = calcular_fatorial(num)
    print(f"Fatorial de {num} é: {resultado}")
    
except ValueError:
    print("Por favor, digite um número inteiro.")
    
