lista = [39, 38, 27, 22, 20, 17, 10, 10, 10, 10, 7, 7, 7, 7, 6]
# 4) Faça funções em Python para calcular a:
# a) Variância amostral
def varianciaAmostral(lista):
    media = sum(lista)/len(lista)
    soma = 0
    for i in lista:
        soma += (i-media)**2
    return soma/(len(lista)-1)

# b) Variância populacional
def varianciaPopulacional(lista):
    media = sum(lista)/len(lista)
    soma = 0
    for i in lista:
        soma += (i-media)**2
    return soma/len(lista)

# c) Desvio padrão amostral
def desvioPadraoAmostral(lista):
    return varianciaAmostral(lista)**(1/2)

# d) Desvio padrão populacional
def desvioPadraoPopulacional(lista):
    return varianciaPopulacional(lista)**(1/2)

# e) Incerteza da média
def incertezaMedia(lista):
    return desvioPadraoAmostral(lista)/(len(lista)**(1/2))

# printar resultados
print("Variância Amostral: ", varianciaAmostral(lista))
print("Variância Populacional: ", varianciaPopulacional(lista))
print("Desvio Padrão Amostral: ", desvioPadraoAmostral(lista))
print("Desvio Padrão Populacional: ", desvioPadraoPopulacional(lista))
print("Incerteza da Média: ", incertezaMedia(lista))