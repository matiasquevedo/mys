import pandas as pd
import numpy as np
import statistics
import random


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

df = pd.read_csv('datosPracticaMontecarlo.txt', header=None, delimiter=r"\s+")
lst = df.iloc[:, 1].tolist()
lstOrder = sorted(lst, reverse=True)
# lstOrder = sorted(lst)
suma = sum(lstOrder)
varianza = np.var(lstOrder)
media = statistics.mean(lstOrder)
print(' \n')
print('--------------------------------')
print('Datos observados')
print('--------------------------------')

print(lstOrder)
print(' \n')
print('Suma')
print(suma)
print(' \n')
print('Varianza')
print(varianza)
print(' \n')
print('Media')
print(media)
print(' \n')
probabilidad = list(map(lambda x: x / suma, lstOrder))


np_array = np.array(probabilidad)

np_round_to_tenths = np.around(np_array, 5)

round_to_tenths = list(np_round_to_tenths)

print(' \n')
print('Probabilidad')
print(round_to_tenths)

probabilidadAcumulada = np.cumsum(round_to_tenths)

print(' \n')
print('Probabilidad Acumulada')
print(probabilidadAcumulada)
print(len(probabilidadAcumulada))

sumaProbabilidad = sum(round_to_tenths)
print(' \n')
print('Suma Probabilidad')
print(sumaProbabilidad)

res = list(np.random.random_sample(size=100))
print('aleatorios')
print(res)

# intervalos = list(chunks(probabilidadAcumulada, 1))

intervalos = np.searchsorted(probabilidadAcumulada, res, side='left')

print(' \n')
print('Intervalos')
print(intervalos)

T = [lstOrder[i] for i in intervalos]
print(T)

varianzaDatos = np.var(T)
mediaDatos = statistics.mean(T)

print('varianzaDatos')
print(varianzaDatos)
print(' \n')
print('mediaDatos')
print(mediaDatos)





