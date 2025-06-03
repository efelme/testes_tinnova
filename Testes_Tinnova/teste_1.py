# Teste 1

eleitores = 1000
validos = 800
branco = 150
nulos = 50

def votos_validos(eleitores, validos):
    return (validos / eleitores) * 100

def votos_brancos(eleitores, branco):
    return (branco / eleitores) * 100

def votos_nulos(eleitores, nulos):
    return (nulos / eleitores) * 100


print("Votos válidos:", votos_validos(eleitores, validos), "%")
print("Votos em branco:", votos_brancos(eleitores, branco), "%")
print("Votos nulos:", votos_nulos(eleitores, nulos), "%")
