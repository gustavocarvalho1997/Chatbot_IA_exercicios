# criar uma lista com cem mil numeros aleatórios entre 0 e 99

import random
import timeit as tmt
import numpy as np
import statistics as st
from exercicio01 import mediaAritmetica, mediaGeometrica, mediaHarmonica
from exercicio02 import mediaPonderada
from exercicio03 import mediana, moda
from exercicio04 import desvioPadraoAmostral, desvioPadraoPopulacional, incertezaMedia, varianciaAmostral, varianciaPopulacional

lista = []

for i in range(150):
    lista.append(random.randrange(1,99))

#testar função usando timeit
print(f'Tempo de execução exercicio 1 mediaAritmetica: {tmt.timeit(lambda: mediaAritmetica(lista),number=100)}')
print(f'Tempo de execução exercicio 1 mediaGeometrica: {tmt.timeit(lambda: mediaGeometrica(lista),number=100)}')
print(f'Tempo de execução exercicio 1 mediaHarmonica: {tmt.timeit(lambda: mediaHarmonica(lista),number=100)}')

print(f'Tempo de execução exercicio 2 mediaPonderada: {tmt.timeit(lambda: mediaPonderada(lista, lista),number=100)}')

print(f'Tempo de execução exercicio 3 moda: {tmt.timeit(lambda: moda(lista),number=100)}')
print(f'Tempo de execução exercicio 3 mediana: {tmt.timeit(lambda: mediana(lista),number=100)}')

print(f'Tempo de execução exercicio 4 varianciaAmostral: {tmt.timeit(lambda: varianciaAmostral(lista),number=100)}')
print(f'Tempo de execução exercicio 4 varianciaPopulacional: {tmt.timeit(lambda: varianciaPopulacional(lista),number=100)}')
print(f'Tempo de execução exercicio 4 desvioPadraoAmostral: {tmt.timeit(lambda: desvioPadraoAmostral(lista),number=100)}')
print(f'Tempo de execução exercicio 4 desvioPadraoPopulacional: {tmt.timeit(lambda: desvioPadraoPopulacional(lista),number=100)}')
print(f'Tempo de execução exercicio 4 incertezaMedia: {tmt.timeit(lambda: incertezaMedia(lista),number=100)}')

print(f'Tempo de execução exercicio 5 mediaAritmetica Numpy: {tmt.timeit(lambda: np.mean(lista),number=100)}')
print(f'Tempo de execução exercicio 5 mediaGeometrica Statistics: {tmt.timeit(lambda: st.geometric_mean(lista),number=100)}')
print(f'Tempo de execução exercicio 5 mediaHarmonica Statistics: {tmt.timeit(lambda: st.harmonic_mean(lista),number=100)}')
print(f'Tempo de execução exercicio 5 varianciaAmostral Numpy: {tmt.timeit(lambda: np.var(lista, ddof=1),number=100)}')
print(f'Tempo de execução exercicio 5 varianciaPopulacional Numpy: {tmt.timeit(lambda: np.var(lista),number=100)}')
print(f'Tempo de execução exercicio 5 desvioPadraoAmostral Numpy: {tmt.timeit(lambda: np.std(lista, ddof=1),number=100)}')
print(f'Tempo de execução exercicio 5 desvioPadraoPopulacional Numpy: {tmt.timeit(lambda: np.std(lista),number=100)}')
print(f'Tempo de execução exercicio 5 Incerteza Numpy: {tmt.timeit(lambda: np.std(lista, ddof=1)/(len(lista)**(1/2)),number=100)}')
print(f'Tempo de execução exercicio 5 Moda Statistics: {tmt.timeit(lambda: st.multimode(lista),number=100)}')
print(f'Tempo de execução exercicio 5 Mediana Statistics: {tmt.timeit(lambda: np.median(lista),number=100)}')
print(f'Tempo de execução exercicio 5 Media Ponderada Numpy: {tmt.timeit(lambda: np.average(lista, weights=lista),number=100)}')