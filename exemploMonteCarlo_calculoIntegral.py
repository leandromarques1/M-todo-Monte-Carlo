import random
import math

#definir a função a ser integrada 
def f(x):
    #return math.pow(x,2) + 1
    return math.exp(x)

#definir o intervalo de integração
a=1     #valor minimo no eixo X
b=5     #valor máximo no eixo Y
M=f(b)  #valor superior



#declaração de parâmetros
Npontos_total = 1000
Npontos_integral = 0

acumulador = 1
while acumulador<=Npontos_total:
    #definindo numeros aleatorios que serão utilizados
    random1 = random.random()
    random2 = random.random()
    #definir coordenadas do ponto aleatório
    Px = a + random1*(b-a)
    Py = random2*M
    #para um ponto estar dentro da integral, 
    #devemos ter que: 
    #  Py<=f(Px)
    if Py<=f(Px):
        Npontos_integral = Npontos_integral + 1
    acumulador = acumulador + 1

Area_int = ((b-a)*M*(Npontos_integral/Npontos_total))

print (Area_int)

