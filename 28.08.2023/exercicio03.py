# 3) Faça funções em Python para calcular a moda e a mediana?
lista = [39, 38, 27, 22, 20, 17, 10, 10, 10, 10, 7, 7, 7, 7, 6]

# a) Moda
def moda(lista):
    frequencia = {}
    for i in lista:
        if i in frequencia:
            frequencia[i] += 1
        else:
            frequencia[i] = 1
    moda = []
    maior = max(frequencia.values())
    for i in frequencia:
        if frequencia[i] == maior:
            moda.append(i)
    return moda

# b) Mediana
def mediana(lista):
    lista.sort()
    if len(lista)%2 == 0:
        return (lista[len(lista)//2]+lista[len(lista)//2-1])/2
    else:
        return lista[len(lista)//2]
    
# printar resultados
print("Moda: ", moda(lista))
print("Mediana: ", mediana(lista))

