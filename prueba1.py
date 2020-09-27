#Universidad del Valle de Guatemala
#Modelacion y simulacion
#Juan Guillermo Sandoval Lacayo - 17577
#Hector Javier Carpio Garcia - 17077
#Miniproyecto3

#Imports
import numpy
import random
import math

#Variables
#Generales
tiempos = []
tiempo = 3600
lambda_max = 2400
#Gorilla
solicitudes_Gorilla = 100
servidores_Gorilla = 1
#Ants
solicitudes_Ants = solicitudes_Gorilla/10
servidores_Ants = 10



#Code
def simulacion(T, lambda_max, solicitudes, servidores):
    #Tiempo inicial
    t = 0
    ta = t
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
    #Tiempos de salida de cada servidor
    NTD = numpy.zeros(servidores)

    while t<= T:
        if ta == min(ta, min(td)):
            t = ta
            Na += 1
            u = random.random()
            ta = t-((math.log(u)/lambda_max))
            A[Na] = t
            n += 1
            if n <= servidores:
                for i in range(0, servidores):
                    if (ni[i] == 0):
                        ni[i] = Na
                        NTs = NTs.append(t-A[Na])
                        td[i] = t + numpy.random.exponential(solicitudes)
                        NTD[i] += td[i]-t
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
                NTs = NTs.append(t-A[index])
                td[nts] = t + numpy.random.exponential(solicitudes)
                NTD[nts] += td[nts] - t

            n -= 1


    return A, D, Na, Nd, n, ta, td, NTs, NTD


simulacion(tiempo, lambda_max, solicitudes_Gorilla, servidores_Gorilla)
    
