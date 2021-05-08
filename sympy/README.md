
Analizando las predicciones de Paul Erlich, pudimos realizar un modelo poblacional contemplando datos desde la decada de 1950 y utilizarlo para "predecir" el estado poblacional a futuro.

Partimos de un modelo lineal, definido por:
	model[t + 1] = model[t] + annual_growth		ó

	xn+1 = xn + c

	Donde xn es la población en el año n, x0 es la población inicial, y c es la constante de crecimiento anual.

Aplicando métodos algebraicos podemos obtener una progresión geométrica que se puede escribir como
un modelo cuadrático:

	xn+1 = xn + αxn + βx2n

	No hay solución analítica para este modelo. 

Mediante este código podemos aproximarla con una ecuación diferencial.

python3 ecuacion.py
