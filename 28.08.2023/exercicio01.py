# 1 - Faça funções em Python para calcular a média:
entrada = [39, 38, 27, 22, 20, 17, 10, 10, 10, 10, 7, 7, 7, 7, 6]

# a) Aritmética
def mediaAritmetica(entrada):
    soma = 0
    for i in entrada:
        soma += i
    return soma/len(entrada)

# b) Geométrica
def mediaGeometrica(entrada):
    produto = 1
    for i in entrada:
        produto *= i
    return produto**(1/len(entrada))

# c) Harmônica
def mediaHarmonica(entrada):
    soma = 0
    for i in entrada:
        soma += 1/i
    return len(entrada)/soma

# printar resultados
print("Média Aritmética: ", mediaAritmetica(entrada))
print("Média Geométrica: ", mediaGeometrica(entrada))
print("Média Harmônica: ", mediaHarmonica(entrada))
