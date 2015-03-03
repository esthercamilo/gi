__author__ = 'esther'

import numpy as np
import os

finput = open("config.txt")
folder = finput.readline().rstrip("\n")

l1 = ['100', '95', '90', '85']
l2 = ['ppi', 'reg', 'met', 'int']
l3 = ['butland', 'babu']
l4 = ['deg', 'bet', 'complete']

foutput = open(folder+'sumario.csv','w')
foutput.write('percent,network,source,attribute,meanROC\n')

def getroc(f):
    roc='0'
    line = f.readline()

    while "Error on test data" not in line:
        line = f.readline()
    for i in range(17):
        rocline = f.readline()
    roc = rocline[67:77].strip()

    return roc


for a in l1:
    for b in l2:
        for c in l3:
            for d in l4:
                roclist = []
                for i in range(1,101):
                    filename = folder+a+'/'+b+'/'+c+'/'+d+'/cold/result/'+str(i)+'_result.txt'
                    if os.stat(filename).st_size > 0:
                        finput = open(filename)
                        roc = getroc(finput)
                    else:
                        roc=0
                        print a,b,c,d,' probleminha'
                    roclist.append(float(roc))
                array = np.array(roclist)
                mean = np.mean(array)
                foutput.write(a+','+b+','+c+','+d+','+str(mean)+'\n')



