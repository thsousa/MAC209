"""
MAC209 - Modelagem e Simulação
BCC - IMEUSP - 2016
EP1 - TRAVESSIA

Larissa de Oliveira Penteado
Lucas de Carvalho Dias
Raul Reis
Thais Lima Sousa
   
"""

import numpy as np

NMAX = 100
g = np.pi ** 2

def euler_muv(y0, v0):
    y = [None]*NMAX
    v = [None]*NMAX
    y[0] = y0
    v[0] = v0
    for i in range(1, 100):
        y[i] = y[i-1] + v[i-1]
        v[i] = v[i-1] + g*i
        
x = np.linspace(0, 10)

# plot graphics


