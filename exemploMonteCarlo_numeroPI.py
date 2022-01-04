import math
import random

#Declaração dos Parâmetros
Npontos_quad = 10000  #numero de jogadas total, caracteristicas bag-of-task
Npontos_circ = 0

acumulador = 1    #define a rodada de jogadas
while acumulador <= Npontos_quad:
    Px = random.random()
    Py = random.random()
    deltaX = math.pow((Px-0.5),2)
    deltaY = math.pow((Py-0.5),2)
    DistE = math.sqrt(deltaX-deltaY) #distancia do ponto aleatório ao centro do circulo
    if DistE<0.5:
        Npontos_circ = Npontos_circ + 1
    acumulador = acumulador + 1

ValorPi = 4*(float(Npontos_circ)/float(Npontos_quad))

print ("O valor de Pi eh aproximadamente %.3f" %ValorPi)