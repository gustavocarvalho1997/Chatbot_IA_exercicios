import numpy as np
import statistics as st

# 5) Refaça os exercícios anteriores usando as funções prostas de estatística do Numpy
entrada = [39, 38, 27, 22, 20, 17, 10, 10, 10, 10, 7, 7, 7, 7, 6]
pesos =  [113, 88, 58, 65, 71, 46, 36, 33, 37, 40, 24, 21, 20, 15, 20]

# a) Aritmética
print("Média Aritmética: ", np.mean(entrada))

# b) Geométrica
print("Média Geométrica: ", st.geometric_mean(entrada))

# c) Harmônica
print("Média Harmônica: ", st.harmonic_mean(entrada))

# d) Variância amostral
print("Variância Amostral: ", np.var(entrada, ddof=1))

# e) Variância populacional
print("Variância Populacional: ", np.var(entrada))

# f) Desvio padrão amostral
print("Desvio Padrão Amostral: ", np.std(entrada, ddof=1))

# g) Desvio padrão populacional
print("Desvio Padrão Populacional: ", np.std(entrada))

# h) Incerteza da média
print("Incerteza da Média: ", np.std(entrada, ddof=1)/(len(entrada)**(1/2)))

# i) Moda
print("Moda: ", st.multimode(entrada))

# j) Mediana
print("Mediana: ", np.median(entrada))

# k) Média Ponderada
print("Média Ponderada: ", np.average(entrada, weights=pesos))