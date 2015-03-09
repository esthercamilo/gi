#################################
#AUTHOR: ESTHER CAMILO          #
#e-mail: esthercamilo@gmail.com #
#################################

from string import *
import numpy as np
import os

fcfg = open('config.txt')
folder = fcfg.readline().rstrip('\n')

wekalocation = fcfg.readline().rstrip('\n')

def readOutFile(tipo):
    #firstLine
    saida = open(folder + 'TOTAL/matrix.csv', 'w')

    #check the lenght of any tree
    tempfile = open(folder+'weka/' + tipo + '/out/1.out')
    templines = tempfile.readlines()
    last = int(templines[-2][0:10].strip())
    tempfile.close()

    primer = "inst1"
    for j in range(2, last+1):
        primer = primer + ",inst" + str(j)
    saida.write(primer + "\n")
    inst = []
    for tree in range(100):
        thisTree = []
        file = open(folder+'weka/' + tipo + '/out/' + str(tree + 1) + '.out')
        lines = file.readlines()[5:-1]
        for i in range(len(lines)):
            if "AGG" in lines[i]:
                (thisTree.append(float((lines[i][33:]).strip())))
            else:
                (thisTree.append(1 - float((lines[i][33:]).strip())))
        inst.append(thisTree)

    for elem in inst:
        line = ','.join([str(x) for x in elem])
        saida.write(line + "\n")



for t in types:
    metricas(t,"metrics.txt")
    readOutFile(t)



def clustering():
    os.system('java -cp '+wekalocation+' weka.clusterers.SimpleKMeans -p 0 -N 4 -t '+folder+'weka/' + t + '/matrix.csv > '+folder+'weka/' + t + '/cluster_assign.txt')



#clustering()

t2=[100]#,200,400,600,800,1000]

def clust2():
	for t in t2:
		for i in range(1,11):
			f_in  = folder+'weka/complete/cluster_algorithm/' + str(t) + '/'+str(i)+'/matrix.csv'
			f_out = folder+'weka/complete/cluster_algorithm/' + str(t) + '/'+str(i)+'/cluster_assign.txt'
			os.system('java -cp '+wekalocation+' weka.clusterers.SimpleKMeans -p 0 -N 4 -t '+f_in+' > '+f_out)

clust2()





def dist(x,y):
    return np.sqrt(np.sum((x-y)**2))

def getTree(m):

    #gerar lista de arvores no cluster
    treesnocluster=[]
    for am in m:
        treesnocluster.append(am[0])
    #gerar matrix somente com linha
    mat = []
    for a in m:
        mat.append(a[1])
    npmat = np.array(mat)
    tmat = np.transpose(npmat)

    matavg = []
    for line in tmat:
        av = np.mean(line)
        matavg.append(av)
    matavg = np.array(matavg)

    dist
    #Arvore mais proxima
    distancia = dist(npmat[0],matavg) #faz a primeira pra ter comparativo
    menorTree = m[0][0]
    for j in range(len(npmat)):
        tdist = dist(npmat[j],matavg)
        if tdist<distancia:
            distancia = tdist
            menorTree = m[j][0]
    #importante somar +1 pois a numeracao das arvores nao comeca em zero.
    return (treesnocluster,menorTree)

def outputf(b,i,output):
    mp = getTree(b)
    treesnocluster = mp[0]
    menorTree = mp[1]
    s1 = ""
    for k in treesnocluster:
        s1 = s1 + str(k) + ', '


    output.write("Cluster%s : %s\n" % (i,menorTree))
    output.write(s1.rstrip()+"\n\n\n")


dicclust={}
f1 = open(folder+'TOTAL/reptree.txt')
for line in f1:
    if line == '\n':
                continue
    try:
        d = line.rstrip().split(" ")
        tree = int(d[0])
        clust = int(d[1])
        dicclust[tree]=clust
    except:
        print "Last line is empty - that is ok"

f2 = open(folder+'weka/'+t+'/matrix.csv')
f2.readline()
i=0
m0=[]
m1=[]
m2=[]
m3=[]
for line in f2:
    d = line.rstrip().split(',')
    linha = []
    for l in d:
        linha.append(float(l))
    n = dicclust[i]
    if n == 0:
        m0.append((i,linha))
    elif n == 1:
        m1.append((i,linha))
    elif n == 2:
        m2.append((i,linha))
    elif n == 3:
        m3.append((i,linha))
    else:
        "check your input file!"
    i = i + 1

output = open(folder+'TOTAL/repTree.csv','w')

outputf(m0,0,output)
outputf(m1,1,output)
outputf(m2,2,output)
outputf(m3,3,output)


