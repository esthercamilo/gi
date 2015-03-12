__author__ = 'esther'

import numpy as np
import os

finput = open("config.txt")
folder = finput.readline().rstrip("\n")

l1 = ['100', '95', '90', '85']

foutput = open(folder+'sumario.csv','w')
foutput.write('Percent,J48,Meta-vote\n')

def getroc(f):
    roc='0'
    line = f.readline()

    while "Stratified cross-validation" not in line:
        line = f.readline()
    for i in range(17):
        rocline = f.readline()
    roc = rocline[67:77].strip()

    return roc

dicj48={}
dicmeta={}
for a in l1:
    for i in range(1,101):
        finputmeta = open(folder+a+'/result_meta/'+str(i)+'.txt')
        finputj48 = open(folder+a+'/result_j48/'+str(i)+'.txt')
        rocmeta = getroc(finputmeta)
        rocj48 = getroc(finputj48)
        dicj48[(a,i)]=rocj48
        dicmeta[(a,i)]=rocmeta

for k in dicj48:
    foutput.write('%sA,%s,%s\n' % (k[0], dicj48[k], dicmeta[k]))




