'''
ELIPSE DE CONFIANÇA - TEORIA

A técnica de elipse de confiança permite que a interpretação dos resultados
seja feita por meio de uma visualização rápida e simples.  
É uma técnica  gráfica baseada na elaboração de um diagrama de dispersão dos resultados,
associados a uma região de confiança (elipse). A elipse de confiança é realizada
por meio do estudo estatístico entre variáveis aleatórias.
A elipse de confiança é traçada de modo que qualquer ponto tenha a mesma probabilidade P 
de se situar dentro da elipse. A probabilidade P é dada pelo nível de significância adotado.

A Tabela 6.1 relaciona o intervalo de confiança com nível de significância e nível de 
confiança.

Intervalo de confiança 		Nível de Confiança % 	Nível de Significância
		3.30						99.9 					0.1
		3 							99.7 					0.3            ==> dispersão 3-sigma
		2.57 						99.0 					1.0	
		2 							95.4 					4.6			   ==> dispersão 2-sigma
		1.96 						95.0 					5.0
		1.65 						90.0 					10.0
		1 							68.3 					31.7		   ==> dispersão 1-sigma


A elipse de confiança é traçada de tal modo que QUALQUER PONTO TEM A MESMA PROBABILIDADE
DE ESTAR DENTRO DA ELIPSE e, em geral, é estabelecido o grau de 95% de confiança.

Geralmente, os pontos se situam dentro de uma elipse, cujo eixo maior faz um ângulo 
de aproximadamente 45 graus com o eixo da horizontal. Portanto, a inclinação maior da 
elipse está próxima de +1 e a do eixo menor, de -1.  
A dispersão dos pontos ao longo do eixo maior está associada aos erros sistemáticos,  
enquanto que, ao longo do eixo menor, está associada aos erros aleatórios.

A elipse de confiança fornece algumas características importantes, as quais estão 
relacionadas abaixo:
•Os pontos que fazem parte do contorno da elipse, estão a uma distância quadrática C 
constante;
•Os eixos da elipse são orientados pelo seus autovetores, em que a direção do eixo maior 
é dado pelo 1º autovetor e a direção do eixo menor é dado pelo 2º autovetor;
•O semi-eixo maior da elipse é dado por +-C*(sqrt(λ1)) e o semi-eixo menor é dado 
por +-C*(sqrt(λ2)), onde λ1 e λ2 são os autovalores da amostra e λ1>λ2

Para implementação da elipse de confiança, é interessante termos conhecidos os valores:
-min			-mean			-std
-max			-median			-range
para cada vetor de dados
'''






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


mediaLat = np.mean(arrLat)
medianaLat = np.median(arrLat)
desvioPadraoLat = np.std(arrLat)
minLat = np.min(arrLat)
maxLat = np.max(arrLat)
intervaloLat =  minLat - maxLat
#print(intervaloLat)

mediaLong = np.mean(arrLong)
medianaLong = np.median(arrLong)
desvioPadraoLong = np.std(arrLong)
minLong = np.min(arrLong)
maxLong = np.max(arrLong)
intervaloLong =  minLong - maxLong
#print(intervaloLong)

a = np.meshgrid(arrLong, arrLat)
print(a)
'''

autovalor = np.linalg.eigvals(xmesh, ymesh)
print(autovalor)
'''