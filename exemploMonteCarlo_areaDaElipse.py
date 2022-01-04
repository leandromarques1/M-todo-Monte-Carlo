#Cálculo da área de uma elipse usando o Método de Monte Carlo
#Caso 1: eixo focal paralelo ao Eixo X

import math
import random

#informando os maiores e menores valores em cada Eixo
r=12    #maior valor no Eixo X
L=2     #menor valor no Eixo X
u=8     #maior valor no Eixo Y
d=2     #menor valor no Eixo Y

#Novos valores das medidas dos eixos maior e menor da Elipse
a=(r-L)/2                       #2a --> eixo maior da Elipse
b=(u-d)/2                       #2b --> eixo menor da Elipse
c=math.sqrt(pow(a,2)-pow(b,2))  #2c --> distancia focal da Elipse

#Coordenada dos Foco F1
F1x=((r+L)/2)-c
F1y=(u+d)/2

#Coordenada dos Foco F2
F2x=((r+L)/2)+c
F2y=(u+d)/2

#Contador de Pontos
Npontos_retan = 100000      #numero de pontos no retangulo
Npontos_elip = 0            #numero de pontos na elipse
acumulador = 1

while acumulador<=Npontos_retan:
    #definindo numeros aleatorios que serão utilizados
    random1=random.random()
    random2=random.random()
    #definir coordenadas do Ponto aleatório P=(Px,Py)
    Px = L + random1*(r-L)
    Py = d + random2*(u-d)
    # condição para estar dentro da Elipse
    #  PF1 + PF2 <= 2a
    deltaX1 = Px-F1x
    deltaX2 = Px-F2x
    deltaY1 = Py-F1y
    deltaY2 = Py-F2y
    PF1 = math.sqrt(pow(deltaX1,2)+pow(deltaY1,2))
    PF2 = math.sqrt(pow(deltaX2,2)+pow(deltaY2,2))
    res = PF1+PF2
    if res<=(r-L):
        Npontos_elip = Npontos_elip + 1
    acumulador = acumulador + 1

#Após todas as oprações, a área da Elipse será
Area_elip = (Npontos_elip/Npontos_retan)*(r-L)*(u-d)

#Fórmula da Elipse (método "piaba")
Area_elip_trad = math.pi*a*b
 
print ("A area da elipse é %.5f" %Area_elip)  
print ("A área calculada pelo método tradicional é %.5f" %Area_elip_trad)
    