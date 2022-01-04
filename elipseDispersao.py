import math
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D # <--- This is important for 3d plotting 

arrLat = np.array([-5.930581470,
                   -5.920010034,
                   -5.937878235,
                   -5.936355375,
                   -5.934312274,
                   -5.931998468,
                   -5.930191937,
                   -5.927214165,
                   -5.924971459,
                   -5.941875666,
                   -5.943379424,
                   -5.944178170,
                   -5.946172686,
                   -5.946580307,
                   -5.948599843,
                   -5.947742383,
                   -5.929668213,
                   -5.933989638,
                   -5.934130905,
                   -5.935621819,
                   -5.938758093,
                   -5.940208620,
                   -5.939734008,
                   -5.937377408,
                   -5.937062842,
                   -5.940826716,
                   -5.939765018,
                   -5.942381385,
                   -5.941658427,
                   -5.943797710,
                   -5.939947710,
                   -5.940701048,
                   -5.939930243,
                   -5.940994022,
                   -5.940365521,
                   -5.939805825,
                   -5.940503968,
                   -5.940010589,
                   -5.939406612,
                   -5.939629017,
                   -5.940781419,
                   -5.939044536,
                   -5.939184908,
                   -5.939380372,
                   -5.941846398,
                   -5.940506968,
                   -5.941875666,
                   -5.927204165,
                   -5.940781819,
                   -5.939044536
                    ])
 

arrLong = np.array([-35.18100990,
                    -35.17193854,
                    -35.17875027,
                    -35.17668979,
                    -35.17525446,
                    -35.17431427,
                    -35.17203600,
                    -35.17313626,
                    -35.17187763,
                    -35.18171260,
                    -35.18370704,
                    -35.18613030,
                    -35.18789103,
                    -35.19043565,
                    -35.19245257,
                    -35.19524266,
                    -35.19047788,
                    -35.18611989,
                    -35.18597994,
                    -35.18447527,
                    -35.18131443,
                    -35.17985235,
                    -35.18046700,
                    -35.18227056,
                    -35.18302596,
                    -35.17922315,
                    -35.18029767,
                    -35.17765630,
                    -35.17838559,
                    -35.17628301,
                    -35.18011285,
                    -35.17935204,
                    -35.18011309,
                    -35.17905765,
                    -35.17969143,
                    -35.18025600,
                    -35.17955183,
                    -35.18005307,
                    -35.18066659,
                    -35.18043828,
                    -35.17928087,
                    -35.18102876,
                    -35.18088730,
                    -35.18069021,
                    -35.17820285,
                    -35.18171260,
                    -35.18370704,
                    -35.17431427,
                    -35.17313626,
                    -35.17985235
                    ])


mediaLat = np.mean(arrLat)              #equivalente ao Y_nominal
desvioPadraoLat = np.std(arrLat)        


mediaLong = np.mean(arrLong)            #equivalente ao X_nominal
desvioPadraoLong = np.std(arrLong)

print("#### IMPRIMINDO PONTO DE IMPACTO NOMINAL ####")
print("X nominal:", mediaLat)
print("Y nominal:", mediaLong)

'''
#Constroi grafico de dispersão, com as coordenadas dos Pontos de Impacto
plt.scatter(arrLong, arrLat)    #plt.scatter -> função que constroi a dispersão
plt.xlabel("Longitude")        
plt.ylabel("Latitude")
plt.title("Mapa")
plt.grid(True)
plt.show()      #plota o grafico de dispersão dos pontos de Impacto
'''

def gaussianaBivariada (Xnominal, Ynominal, stdX, stdY):
        A = 1
        
        x0 = Xnominal
        y0 = Ynominal
        '''
        print("####Imprimindo Ponto de Impacto Nominal####")
        print("X nominal:", x0)
        print("Y nominal:", y0)
        '''
        
        sigma_X = stdX
        sigma_Y = stdY

        #usar o conceito da dispersão 3 Sigma
        #teoricamente, abrangerá 99.7% dos casos
        xg = np.linspace(x0 - 3*sigma_X, x0 + 3*sigma_X, num=100)
        yg = np.linspace(y0 - 3*sigma_Y, y0 + 3*sigma_Y, num=100)
        
        theta= np.pi

        X, Y = np.meshgrid(xg,yg)

        '''
        #Ver a plotagem da malha de pontos
        plt.scatter(X, Y)
        plt.show()
        '''
        
        a = np.cos(theta)**2/(2*sigma_X**2) + np.sin(theta)**2/(2*sigma_Y**2)
        b = -np.sin(2*theta)/(4*sigma_X**2) + np.sin(2*theta)/(4*sigma_Y**2)
        c = np.sin(theta)**2/(2*sigma_X**2) + np.cos(theta)**2/(2*sigma_Y**2)

        aXXdet = np.array([a*(Xi-x0)**2 for Xi in X],float)
        bbXYdet = np.array([2*b*(Xi-x0)*(Y[ii]-y0) for ii,Xi in enumerate(X)],float)
        cYYdet = np.array([c*(Yi-y0)**2 for Yi in Y],float)

        Z = np.array([A*np.exp( - (ai + bbXYdet[i] + cYYdet[i])) for i,ai in enumerate(aXXdet)],float)
        
        '''
        #Plotando o gráfico de Contornos (Famílias de Elipses)
        #plt.contour(X, Y, Z, colors='black')
        plt.contourf(X, Y, Z)           #deixa colorido o gráfico
        contorno1 = plt.contourf(X, Y, Z)
        plt.colorbar(contorno1)
        plt.show()
        '''

        
        #Plotando o gráfico de Contornos (Famílias de Elipses) com as regiões de probabilidades
        contours = plt.contour(X, Y, Z, colors='black')
        plt.clabel(contours, inline=True, fontsize=12)
        contorno1 = plt.contourf(X, Y, Z)              #deixa colorido o gráfico
        plt.colorbar(contorno1)
        plt.show()
        ''''''

        '''
        #Plotando o Grafico 3D da Gaussiana Bimensional
        # plot
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(X, Y, Z, cmap=cm.coolwarm)
        ax.set_xlabel('X Label: Longitude')
        ax.set_ylabel('Y Label: Latitude')
        ax.set_zlabel('Z Label: Densidade de Probabilidade (eu acho)')
        plt.show()
        '''


gaussianaBivariada (mediaLong, mediaLat, desvioPadraoLong, desvioPadraoLat)
