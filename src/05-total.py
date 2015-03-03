__author__ = 'esther'

import os

finput = open("config.txt")
folder = finput.readline().rstrip("\n")

def getdic(f):
    dic = {}
    for line in f:
        d = line.split(',')
        dic[(d[0],d[1])]= d[2:]
    return dic

#babu

f1=open(folder+'100/ppi/babu/complete/training.csv')
dicbabuppi = getdic(f1)
f2=open(folder+'100/reg/babu/complete/training.csv')
dicbabureg = getdic(f2)
f3=open(folder+'100/met/babu/complete/training.csv')
dicbabumet = getdic(f3)
f4=folder+'100/int/babu/complete/training.csv'
dicbabuint = getdic(f4)

#butland

g1=open(folder+'100/ppi/butland/complete/training.csv')
dicbutppi = getdic(g1)
g2=open(folder+'100/reg/butland/complete/training.csv')
dicbutreg = getdic(g2)
g3=open(folder+'100/met/butland/complete/training.csv')
dicbutmet = getdic(g3)
g4=open(folder+'100/int/butland/complete/training.csv')
dicbutint= getdic(g4)


for k in dicbutint.keys():
    try:
        novalinha = dicbutint[k][0:-1]+dicbutppi[k][0:-1]+dicbutreg[k][0:-1]+dicbutmet[k]
        print 'para'
    except:
        pass
