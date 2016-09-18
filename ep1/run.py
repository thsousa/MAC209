"""
MAC209 - Modelagem e Simulação
BCC - IMEUSP - 2016
EP1 - TRAVESSIA

Larissa de Oliveira Penteado
Lucas de Carvalho Dias
Raul Reis
Thais Lima Sousa
   
"""

# plota figura com dados do acelerômetro
# cells[0] é o tempo decorrido e cells[3] é a direção do movimento
# modificar para salvar a imagem

# uma ideia: fazer a média dos dados antes de plotar a travessia

import csv
import matplotlib.pyplot as plt


def parser(filename):
    time = []
    y = []
    title = 'travessia ' + filename
    f = open( filename, 'rU' )
    f.readline()
    for line in f:
        cells = line.split( ";" )
        time.append(cells[0])
        y.append(cells[3])
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(time, y)
    ax.set_title(title, fontsize=20)
    ax.set_xlabel('Tempo')
    ax.set_ylabel('aceleração')
    plt.show()
    f.close()
    

parser('MU1-lari.csv')
