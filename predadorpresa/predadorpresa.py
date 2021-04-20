import sys
from modsim import *
from matplotlib import pyplot
def main():
	print('hola')

	semanas = 100
	liebres = 5000
	zorros = 100

	tasa_liebres = 0.08
	tasa_zorros = 0.2

	capacidad_terreno = 100
	ciclo(semanas,liebres,zorros,tasa_liebres,tasa_zorros,capacidad_terreno)

def ciclo(semanas,liebres,zorros,tasa_liebres,tasa_zorros,capacidad_terreno):
	sweep_liebres = modsim.SweepSeries()
	sweep_zorros = modsim.SweepSeries()
	for semana in range(
		semanas):
		if (liebres>=0 and zorros >=0 ):
			capacidad_activa = capacidad_terreno - liebres
			inc_liebres = (capacidad_activa/capacidad_terreno)*tasa_liebres*liebres
			disponibilidad_zorros = tasa_zorros*zorros

			caza = zorros*liebres

			liebres = liebres + semana*(inc_liebres-0.002*caza)
			zorros = zorros + semana * (0.0004*caza - disponibilidad_zorros)

			sweep_liebres[semana] = liebres
			sweep_zorros[semana] = zorros

	pyplot.clf()
	mockData(sweep_liebres, sweep_zorros)

def mockData(sweep_liebres, sweep_zorros):
	fig, ax1 = pyplot.subplots(sharex=True, sharey=True)
	color = 'tab:red'
	ax1.set_xlabel('Semanas')
	ax1.set_ylabel('Liebres', color=color)
	ax1.set_ylim(0,5000)
	ax1.plot(sweep_liebres, color=color)
	ax1.tick_params(axis='y', labelcolor=color)

	ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

	color = 'tab:blue'
	ax2.set_ylabel('Zorros', color=color)  # we already handled the x-label with ax1
	ax2.set_ylim(0,5000)
	ax2.invert_yaxis()
	ax2.plot(sweep_zorros, color=color)
	ax2.tick_params(axis='y', labelcolor=color)

	fig.tight_layout()  # otherwise the right y-label is slightly clipped
	savefig('/tmp/sweep.jpg')
	pyplot.show()



if __name__ == '__main__':
	main()












