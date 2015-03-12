__author__ = 'esther'

import os
import random as rm

finput = open("config.txt")
folder = finput.readline().rstrip("\n")

perc = ['100']

def makedir(namedir):
    if not os.path.exists(folder+namedir):
        os.makedirs(folder+namedir)

for p in perc:
    makedir(p+'/csv')
    makedir(p+'/result_j48')
    makedir(p+'/result_meta')
    makedir(p+'/arff')

    f = open(folder+p+'/training.csv')
    h = f.readline()
    #dicnames = h.rstrip('\n').split(',')
    #last = len(dicnames)
    #initialize dictionaries
    #for d in dicnames[2:]:
    #    exec(d+ "= { } ")

    # for l in f:
    #     a = l.rstrip('\n').split(',')
    #     for i in range(2,last):
    #         command = '%s[("%s","%s")]=a[%s]' % (dicnames[i],a[0],a[1],i)
    #         exec(command)

    agg=[]
    all=[]
    for l in f:
        d = l.rstrip('\n').split(',')
        scr = float(d[-1])
        if scr < 0:
            novalinha = ','.join(d[0:-1])+',AGG\n'
            agg.append(novalinha)
        else:
            novalinha = ','.join(d[0:-1])+',ALL\n'
            all.append(novalinha)

    size = len(all)

    for i in range(100):
        output = open(folder+p+"/csv/" + str(i + 1) + ".csv", "w")
        output.write(h)
        rm.shuffle(agg)
        for i in range(size):
            output.write(agg[i])
            output.write(all[i])

