import matplotlib.pyplot as plt 
import numpy as np 
from mpl_toolkits.mplot3d import axes3d

#Fazendo uma trajetória 3d

#dados
t = np.linspace(0,10,101)

#Função da Trajetória 
# s(t) = [sin(t), cos(t), exp(t)]

def s(t):
    return np.array([np.sin(t),
                     np.cos(t),
                     np.exp(t)])
                     
x, y, z = s(t)

fig=plt.figure('Trajetoria')
ax=fig.gca(projection = '3d')
ax.plot(x,y,z,'r.')
plt.show()

'''
#teste: equação de um movimento balistico em 3d

#dados 
t = np.linspace(0,10,101)  #array que contem os valores de tempo

def r(t):
    x0 = 0					    #Posição X de Lançamento
    y0 = 0					    #Posição Y de Lançamento
    z0 = 0						#Posição Z de Lançamento
    g = 9.81					#gravidade (m/s²)
    v0 = 30                     #velocidade inicial de lançamento(m/s)
    angEle = (85*np.pi)/180		#angulo de Elevação
    angAzim = (90*np.pi)/180	#angulo de Azimute
    
    #Instante do impacto (se o z0=0)
    t_final = (2*(v0*np.sin(angEle)))/(g)		
    #print(t_final)
    return np.array([x0 + (v0*np.cos(angEle)*np.cos(angAzim))*t,
    				 y0 + (v0*np.cos(angEle)*np.sin(angAzim))*t, 
    				 z0 + (v0*np.sin(angEle)*t) - g*((t**2)/2)])
                  
x, y, z = r(t)



fig=plt.figure('Trajetoria')
ax=fig.gca(projection = '3d')
ax.plot(x,y,z,'r.')
plt.show()

'''
