#!/usr/bin/env python
# brew install python-tk@3.9
import sys
from modsim import *
from matplotlib import pyplot
import numpy as np
import random
# tkinter._test()

animal = ['🦊','🐇','🐇','🦊']


def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '-', printEnd = "\r"):

    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    if iteration == total: 
        print()

def main():

	print('Caso Presa-predador')

	dt=1
	semanas = int(input("Ingrese la Duración de la Simulación(semanas): "))
	liebres = int(input("Ingrese la Cantidad de Liebres: "))
	zorros = int(input("Ingrese la Cantidad de Zorros: "))

	tasa_liebres = float(input("Ingrese la Tasa de Nacimiento de Liebres[0.08]: ") or "0.08")
	tasa_zorros = float(input("Ingrese la Tasa de Mortalidad de Zorros[0.2]: ") or "0.2")

	capacidad_terreno = int(input("Ingrese El tamaño del terreno["+str(liebres)+"]:") or str(liebres))
	ciclo(semanas,dt,liebres,zorros,tasa_liebres,tasa_zorros,capacidad_terreno)

def ciclo(semanas,dt,liebres,zorros,tasa_liebres,tasa_zorros,capacidad_terreno):
	print('Calculando poblaciones:')
	sweep_liebres = modsim.SweepSeries()
	sweep_zorros = modsim.SweepSeries()
	printProgressBar(0, semanas, prefix = 'Semanas:', suffix = 'Simuladas', length = 15, fill = random.choice(animal))
	for semana in range(1,
		semanas,dt):
		capacidad_activa = capacidad_terreno - liebres
		inc_liebres = (1/capacidad_terreno)*capacidad_activa*tasa_liebres*liebres
		disponibilidad_zorros = tasa_zorros*zorros

		caza = zorros*liebres

		liebres = liebres + dt*(inc_liebres-0.002*caza)
		zorros = zorros +  dt* (0.0004*caza - disponibilidad_zorros)

		sweep_liebres[semana] = liebres
		sweep_zorros[semana] = zorros
		
		printProgressBar(semana + 1, semanas, prefix = 'Semanas:', suffix = 'Simuladas', length = 15, fill = random.choice(animal))
			
	pyplot.clf()
	mockData(sweep_liebres, sweep_zorros, semanas, liebres, zorros)


def mockData(sweep_liebres, sweep_zorros, semanas, liebres, zorros):
	fig, ax1 = pyplot.subplots(sharex=True, sharey=True)
	color = 'tab:red'
	ax1.set_xlabel('Semanas')
	ax1.set_ylabel('Liebres', color=color)
	# ax1.set_ylim(0,5000)
	ax1.plot(sweep_liebres, color=color)
	ax1.tick_params(axis='y', labelcolor=color)

	ax2 = ax1.twinx()

	color = 'tab:blue'
	ax2.set_ylabel('Zorros', color=color)
	# ax2.set_ylim(0,5000)
	# ax2.invert_yaxis()
	ax2.plot(sweep_zorros, color=color)
	ax2.tick_params(axis='y', labelcolor=color)

	fig.tight_layout()
	savefig('/tmp/sweep.jpg')
	# pyplot.show()

	
	f2 = pyplot.figure()
	X, Y = np.meshgrid (liebres, zorros)
	pyplot.title('Diagrama de Fases')
	Q = pyplot.quiver(sweep_zorros, sweep_liebres, sweep_zorros.index, sweep_liebres.index)
	pyplot.xlabel('Número de Liebres')
	pyplot.ylabel('Número de Zorros')
	# pyplot.legend()
	pyplot.grid()
	f2.savefig('/tmp/fase.png')




if __name__ == '__main__':
	main()












