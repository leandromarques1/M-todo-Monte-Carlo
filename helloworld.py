import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D # <--- This is important for 3d plotting 



A = 1
x0 = 0
y0 = 0

sigma_X = 2
sigma_Y = 2

xg = np.linspace(-5,5,num=100)
yg = np.linspace(-5,5,num=100)
'''
x0 = -5.92
y0 = -35.2
sigma_X = 1
sigma_Y = 1

tresSigmaX = 3*sigma_X
tresSigmaY = 3*sigma_Y 

xg = np.linspace(x0 - 3*sigma_X, x0 + 3*sigma_X, num=100)
yg = np.linspace(y0 - 3*sigma_Y, y0 + 3*sigma_Y, num=100)
'''
theta= np.pi

X, Y = np.meshgrid(xg,yg)

a = np.cos(theta)**2/(2*sigma_X**2) + np.sin(theta)**2/(2*sigma_Y**2);
b = -np.sin(2*theta)/(4*sigma_X**2) + np.sin(2*theta)/(4*sigma_Y**2);
c = np.sin(theta)**2/(2*sigma_X**2) + np.cos(theta)**2/(2*sigma_Y**2);

aXXdet = np.array([a*(Xi-x0)**2 for Xi in X],float)
bbXYdet = np.array([2*b*(Xi-x0)*(Y[ii]-y0) for ii,Xi in enumerate(X)],float)
cYYdet = np.array([c*(Yi-y0)**2 for Yi in Y],float)
Z = np.array([A*np.exp( - (ai + bbXYdet[i] + cYYdet[i])) for i,ai in enumerate(aXXdet)],float);

# plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap=cm.coolwarm)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()

'''
import math
import random
import numpy as np
import matplotlib.pyplot as plt


p1=60
m1=3.5
cont=0
arrayX = np.array([])

for i in range(1,201,1):
    x1 = random.random()    #gera um numero aleatório entre 0 e 1
    x2 = random.random()    #gera um outro numero aleatório entre 0 e 1, diferente do primeiro
    x3 = x1 + x2            #gera um número aleatório entre 0 e 2, a partir da soma dos dois primeiros aleatórios
    x4 = x3 - 1             #ao subtrair 1, geramos um novo intervalo para o meu aleatório, que será entre -1 e 1
    x5 = m1*x4              #pode receber qualquer numero, mesmo que float, e surge um intervalo entre -m1 e m1
    x6 = p1 + x5            #chegamos assim ao intervalo que eu quero, entre (p1-m1) e (p1+m1) 
    #print(x1,"/",x2,"/",x3,"/",x4)
    
    #if x6<=57:
    #    cont= cont + 1
    arrayX = np.append(arrayX, x6)
    print(x6)

'''



'''
nome = input ("Digite o nome do Estudante: ")
idade = int(input("Digite a idade do Estudante: "))
sexo = input("Digite o Sexo do Estudante: ")
curso = input("Digite o Curso do Estudante: ")
rendaMensal = float(input("Digite a Renda Mensal: "))
matricula = int(input("Digite o Matricula do Estudante: "))
cpf = input("Digite o CPF do Estudante: ")
telefone = input("Digite o Telefone para contato: ")
email = input ("Digite e-mail para contato: ")

print("Nome:", nome)
print("Idade:",idade)
print("Sexo:", sexo)
print("Curso:", curso)
print("Renda Mensal:",rendaMensal)
print("Matrícula:", matricula)
print("CPF:",cpf)
print("Telefone",telefone)
print("E-mail",email)

'''
'''
import math

#valor do raio
r = int(input ("Digite valor do raio do circulo: "))

area = (math.pi)*(r**r) #area do círculo
print ("A área do circulo é", area, "centímetros quadrados")
'''
'''
import math

print(math.sqrt(9))
print(math.sqrt(16))
print(math.sqrt(20))
print(math.sqrt(25))
print(math.sqrt(42))
'''
'''
import math

print("Calcular a hipotenusa para os triangulos retangulos")
cateto1 = int(input("Valor do Cateto 1: "))
cateto2 = int(input("Valor do Cateto 2: "))

hipotenusa = math.sqrt(math.pow(cateto1,2) + math.pow(cateto2,2))

print("O valor da hipotenusa será:", hipotenusa)

#area do triangulo = (base*altura)/2
area = (cateto1*cateto2)/2

print("Area do triangulo:", area)
'''
'''
import math

R = 6
H = 5

areaBase = (math.pi)*(math.pow(R,2))
areaLateral = 2*math.pi*(R)*(H)
areaTotal = 2*areaBase + areaLateral
volumeCilindro = (math.pi)*(math.pow(R,2))*H

print ("Area total do Cilindro:", areaTotal)
print ("Volume do Cilindro:", volumeCilindro)
'''

