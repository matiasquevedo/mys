import sympy as s
from sympy.geometry.util import idiff

from sympy.integrals.manualintegrate import integral_steps

t,alpha, beta, C1, x_0 = s.symbols("t alpha beta C1 x_0")
f = s.Function("f")
dfdt = s.diff(f(t),t)

# Definimos la ecuación:
ecuacion = s.Eq( dfdt , alpha * f(t) + beta * (f(t)**2))
print(" ")
print("la ecuacion es: " + str(ecuacion))

# Buscamos la solucion general, resolviendo la ecuación con s.dsolve():
solucion_ecuacion = s.dsolve(ecuacion)

# La funcion .rsh devuelve el segundo miembro de la ecuación:
solucion_general = solucion_ecuacion.rhs

# Evaluamos las condiciones de contorno: t=0, x(t)=x_0 ,
	# 1) Primero haciendo t=0:
solucion_general_t0 = solucion_general.subs(t,0)

	# 2) Segundo, por la población incial, cuando t=0, la 
	# 	función responde a la población inicial;
condicion_inicial = s.Eq(solucion_general_t0, x_0)

# Para encontrar la solución particular a las condiciones de contorno, debemos
# despejar la constante C1. Resolvemos con s.solve();
lista_soluciones = s.solve(condicion_inicial, C1)

# s.solve() devuelve una lista de soluciones:
# Tomando la primer solución:
valor_C1 = lista_soluciones[0]

# Reemplazamos el valor de la constante C1 en la solución general encontrada:
solucion_particular = solucion_general.subs(C1, valor_C1)

# s.simplify(), simplifica la ecuación de la solución particular.
solucion_particular_simplificada = s.simplify(solucion_particular) 

# Para asegurar la igualdad entre la solución particular y la solución paricular simplificada,
# hacemos la diferencia entre ellas:
dff_soluciones_particulares = s.simplify(solucion_particular_simplificada - solucion_particular)

# Si la diferencia es igual a cero, es decir que las ecuaciones son equivalentes,
# imprimimos la solución:
if(dff_soluciones_particulares == 0):
	print(" ")
	print("La solucion particular simplificada es : ")
	print("		"+str(solucion_particular_simplificada))
	print(" ")



