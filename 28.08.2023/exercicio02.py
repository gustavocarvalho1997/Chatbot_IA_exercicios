# 2) Faça uma função em Python para calcular a média ponderada. Ela deve receber dois vetores (listas) como entrada.
valores = [39, 38, 27, 22, 20, 17, 10, 10, 10, 10, 7, 7, 7, 7, 6]
pesos =  [113, 88, 58, 65, 71, 46, 36, 33, 37, 40, 24, 21, 20, 15, 20]

def mediaPonderada(valores, pesos):
    soma = 0
    for i in range(len(valores)):
        soma += valores[i]*pesos[i]
    return soma/sum(pesos)

print("Média Ponderada: ", mediaPonderada(valores, pesos))