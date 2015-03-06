__author__ = 'esther'


import os

finput = open("config.txt")
folder = finput.readline().rstrip("\n")

l1 = ['100', '95', '90', '85']
l2 = ['ppi', 'reg', 'met', 'int']


foutputbutland = open(folder+'sumario_butland.csv','w')
foutputbabu = open(folder+'sumario_babu.csv','w')
foutputbutland.write('Percent,int,ppi,reg,met,roc\n')
foutputbabu.write('Percent,int,ppi,reg,met,roc\n')

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
for a in l1:
    for b in l2:
        listababu = []
        listabutland = []
        for i in range(1,101):
            finputbabu = open(folder+a+'/'+b+'/babu/complete/cold/result/'+str(i)+'_result.txt')
            finputbutland = open(folder+a+'/'+b+'/butland/complete/cold/result/'+str(i)+'_result.txt')
            rocbabu = getroc(finputbabu)
            rocbutland = getroc(finputbutland)
            listababu.append(rocbabu)
            listabutland.append(rocbutland)
        dicbabu[(a,b)]=listababu
        dicbutland[(a,b)]=listabutland

g = ['100', '95', '90', '85']

def save(dic,output):
    for p in g:
        int = dic[(p,"int")]
        ppi = dic[(p,"ppi")]
        reg = dic[(p,"reg")]
        met = dic[(p,"met")]
        for i in range(1,100):
            output.write("%s,%s,%s,%s,%s\n" % (p,int[i],ppi[i],reg[i],met[i]))

save(dicbabu,foutputbabu)
save(dicbutland,foutputbutland)
