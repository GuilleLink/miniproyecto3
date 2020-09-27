#Universidad del Valle de Guatemala
#Modelacion y simulacion
#Juan Guillermo Sandoval Lacayo - 17577
#Hector Javier Carpio Garcia - 17077
#Miniproyecto3

#Imports
import numpy
import random
import math

#Code
def simulacion(T, lambda_max, solicitudes, servidores):
    #Tiempo inicial
    t = 0
    
    u = random.random()
    ta = t-((math.log(u)/lambda_max))

    td = numpy.zeros(servidores) + numpy.infty
    A = {}
    D = {}


    #Numero de clientes
    n = 0 
    #Numero de cliente en el servidor (0 libre)
    ni = numpy.zeros(servidores)
    #Numero de entradas
    Na = 0
    #Numero de salidas
    Nd = numpy.zeros(servidores)
    #Numero de tiempos de ocurrencia
    NTs = []
    #Tiempos ocupado de cada servidor
    NTD = numpy.zeros(servidores)

    while t < T:
        # print(ta, td, min(ta, min(td)))
        if ta == min(ta, min(td)):
            t = ta
            Na += 1
            u = random.random()
            ta = t-((math.log(u)/lambda_max))
            A[Na] = t
            if n < servidores:
                for i in range(0, servidores):
                    if (ni[i] == 0):
                        ni[i] = Na
                        NTs.append(t-A[Na])
                        td[i] = t + numpy.random.exponential(solicitudes)
                        NTD[i] += td[i]-t
                        break
            n += 1
        else:
            #Next TimeStamp
            nts = numpy.argmin(td)
            t = td[nts]
            Nd[nts] += 1
            D[ni[nts]] = t
            if (n <= servidores):
                ni[nts] = 0
                td[nts] = numpy.infty
            else:
                index = max(ni) + 1
                ni[nts] = index
                NTs.append(t - A[index])
                td[nts] = t + numpy.random.exponential(solicitudes)
                NTD[nts] += td[nts] - t

            n -= 1
    return A, D, Na, Nd, n, ta, td, NTs, NTD