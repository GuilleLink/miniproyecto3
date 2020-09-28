#Universidad del Valle de Guatemala
#Modelacion y simulacion
#Juan Guillermo Sandoval Lacayo - 17577
#Hector Javier Carpio Garcia - 17077
#Miniproyecto3

#Imports
import numpy as np
import random
import math

#Code
def simulacion(T, lambda_max, solicitudes, servidores):
    #Tiempo inicial
    t = 0
    
    #Numero de clientes
    n = 0 

    #Numero de entradas
    Na = 0
    #Numero de salidas
    Nd = np.zeros(servidores)
    #Tiempos ocupado de cada servidor
    NTD = np.zeros(servidores)

    A = {}
    D = {}
    #Numero de tiempos de ocurrencia
    NTs = []

    u = np.random.uniform()
    ta = t-((np.log(u)/lambda_max))

    td = np.zeros(servidores) + np.infty
    #Numero de cliente en el servidor (0 libre)
    ni = np.zeros(servidores)

    while t < T:
        if ta == min(ta, min(td)):
            t = ta
            Na += 1

            u = np.random.uniform()
            ta = t - ((np.log(u)/lambda_max))
            
            A[Na] = t
            if n < servidores:
                for i in range(servidores):
                    if ni[i] == 0:
                        ni[i] = Na
                        NTs.append(t - A[Na])
                        td[i] = t + np.random.exponential(solicitudes)
                        NTD[i] += td[i] - t
                        break
            n += 1
        else:
            #Next TimeStamp
            nts = np.argmin(td)
            t = td[nts]
            Nd[nts] += 1
            D[ni[nts]] = t
            if n <= servidores:
                ni[nts] = 0
                td[nts] = np.infty
            else:
                index = max(ni) + 1
                ni[nts] = index
                NTs.append(t - A[Na])
                td[nts] = t + np.random.exponential(solicitudes)
                NTD[nts] += td[nts] - t

            n -= 1
    return A, D, Na, Nd, n, ta, td, NTs, NTD