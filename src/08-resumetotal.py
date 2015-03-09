__author__ = 'esther'

import os

finput = open("config.txt")
parent = finput.readline().rstrip("\n")
folder = parent+'TOTAL/undersampling/'

foutput = open(folder+'sumario_total_complete.csv','w')
foutput.write('Algorithm,Butland,Babu\n')

def getroc(f):
    roc='0'
    line = f.readline()
    while "Error on test data" not in line:
        line = f.readline()
    for i in range(17):
        rocline = f.readline()
    roc = rocline[67:77].strip()
    return roc

dicbabu={}
dicbutland={}
for b in ["result_j48","result_meta"]:
    for i in range(1,101):
        finputbabu = open(folder+"babu/"+b+"/"+str(i)+'_result.txt')
        finputbutland = open(folder+"butland/"+b+"/"+str(i)+'_result.txt')
        rocbabu = getroc(finputbabu)
        rocbutland = getroc(finputbutland)
        dicbabu[(i,b)]=rocbabu
        dicbutland[(i,b)]=rocbutland

for i in range(1,101):
    foutput.write("%s,%s,%s\n" % ("J48",dicbutland[(i,"result_j48")],dicbabu[(i,"result_j48")]))
    foutput.write("%s,%s,%s\n" % ("Meta_Vote",dicbutland[(i,"result_meta")],dicbabu[(i,"result_meta")]))




