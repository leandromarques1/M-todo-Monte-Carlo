import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d

#dados
x=np.linspace(-2,2,11)
y=np.linspace(-2,2,11)

#criar malha de pontos
xmesh, ymesh = np.meshgrid(x,y)
zmesh = np.sin((xmesh**2 + ymesh**2)**0.5)

'''
#Ver a plotagem da malha de pontos
plt.scatter(xmesh, ymesh)
plt.show()
'''

'''
#Gráficos de contorno

#plt.contour(xmesh, ymesh, zmesh) #contornos só com linhas coloridas
#plt.contourf(xmesh, ymesh, zmesh) #contornos com regiões do gráfico coloridas
#plt.contourf(xmesh, ymesh, zmesh, alpha=0.3) #alpha => nível de transparência do gráfico
plt.show()
'''
'''
#Criar gráficos de contorno com barras de cores
contorno1 = plt.contourf(xmesh, ymesh, zmesh)
plt.colorbar(contorno1)
plt.show()
'''

#Gráficos de Superfície
fig = plt.figure()  #capture figura
ax = fig.gca(projection='3d')
ax.plot_surface(xmesh, ymesh, zmesh, cstride = 1, rstride = 1)
#ax.contourf(xmesh, ymesh, zmesh, cstride = 1, rstride = 1)
#ax.contourf(xmesh, ymesh, zmesh, zdir = 'x', offset = -5)

plt.show()




