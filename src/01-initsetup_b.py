#################################
#AUTHOR: ESTHER CAMILO          #
#e-mail: esthercamilo@gmail.com #
#################################
import os
import networkx as nx
import random as rm
import numpy as np

finput = open("config.txt")
folder = finput.readline().rstrip("\n")


def makedir(namedir):
    if not os.path.exists(folder+namedir):
        os.makedirs(folder+namedir)

#Levels

perc = ['100', '95', '90', '85']

network = ['deg', 'reg', 'met', 'int']

att_single = ['deg', 'bet']
att_double = ['sp', 'cn', 'fsw', 'jc']

att_reg = ['regin', 'regout']
att_met = ['metin', 'metout']

#read butland file
dicpairs = {}
filebut = open(folder+'files/butlandscore.tab')
filebut.readline()
for line in filebut:
    d = line.split()
    dicpairs[(d[0],d[1])]=d[2]


for p in perc:
    makedir(p)

def avgDegree(dicValues):
    list = []
    for elem in dicValues.values():
        list.append(float(elem))
    avg = np.mean(list)
    return avg

def CN(G, pairs):  #common neighbors
    dic = {}
    nodes = G.nodes()
    for p in pairs:
        if p[0] in nodes and p[1] in nodes:
            n1 = G.neighbors(p[0])
            n2 = G.neighbors(p[1])
            inter = len(set(n1) & set(n2))
            dic[p] = inter
        else:
            dic[p]=0
    return dic

def FSW(G, pairs):
    dic = {}
    n = G.nodes()
    avg = avgDegree(G.degree())
    for p in pairs:
        if p[0] in n and p[1] in n:
            n1 = G.neighbors(p[0])
            n2 = G.neighbors(p[1])
            i = len(set(n1) & set(n2))  #intersection
            m = abs(len(n1) - len(n2))
            l1 = max(0, avg - len(n1))
            l2 = max(0, avg - len(n2))
            #set formed by x ! in y
            xmy_init = n1
            for elem in n2:
                if elem in xmy_init:
                    xmy_init.remove(elem)
            xmy = len(xmy_init)
            #set formed by y ! in x
            ymx_init = n2
            for elem in n1:
                if elem in ymx_init:
                    ymx_init.remove(elem)
            ymx = len(ymx_init)
            try:
                fsw = (2 * i / (ymx + 2 * i + l1)) * (2 * i / (xmy + 2 * i + l2))
            except:
                fsw = 0
            dic[p] = fsw
        else:
            dic[p]=0
    return dic

def JC(G, pairs):  #Jaccard
    dic = {}
    nodes = G.nodes()
    for p in pairs:
        if p[0] in nodes and p[1] in nodes:
            n1 = G.neighbors(p[0])
            n2 = G.neighbors(p[0])
            inter = len(set(n1) & set(n2))
            union = len(set(n1) | set(n2))
            jc = 0
            try:
                jc = inter / union
            except ZeroDivisionError:
                pass
            dic[p] = jc
        else:
            dic[p]=0
    return dic


#return a list of pairs
def readintfile(filename):
    myfile = open(folder + filename)
    listpair = []
    for line in myfile:
        d = line.split()
        listpair.append((d[0],d[1]))
    rm.shuffle(listpair)
    return listpair


listint = readintfile('files/int.tab')
listppi = readintfile('files/ppi.tab')
listreg = readintfile('files/reg.tab')
listmet = readintfile('files/met.tab')

def getatt(perc):
    print "Network ",perc
    per = float(perc) / 100

    Gint = nx.Graph()
    Gppi = nx.Graph()
    Greg = nx.DiGraph()
    Gmet = nx.DiGraph()

    sint = int(per*len(listint))
    sppi = int(per*len(listppi))
    sreg = int(per*len(listreg))
    smet = int(per*len(listmet))

    for elem in listint[0:sint]:
        Gint.add_edge(elem[0], elem[1])
    for elem in listppi[0:sppi]:
        Gppi.add_edge(elem[0], elem[1])
    for elem in listreg[0:sreg]:
        Greg.add_edge(elem[0], elem[1])
    for elem in listmet[0:smet]:
        Gmet.add_edge(elem[0], elem[1])

    #computation of the att
    deg_int = Gint.degree()
    deg_ppi = Gppi.degree()
    deg_reg = Greg.degree()
    deg_met = Gmet.degree()
    print "Degree computed."
    bet_int = nx.algorithms.centrality.betweenness_centrality(Gint)
    print 'betint'
    bet_ppi = nx.algorithms.centrality.betweenness_centrality(Gppi)
    print 'betppi'
    bet_reg = nx.algorithms.centrality.betweenness_centrality(Greg)
    print 'betreg'
    bet_met = nx.algorithms.centrality.betweenness_centrality(Gmet)
    print "Betweennes computed."
    regin = Greg.in_degree()
    regout = Greg.out_degree()
    metin = Gmet.in_degree()
    metout = Gmet.out_degree()
    cn_int = CN(listint,dicpairs.keys())
    cn_ppi = CN(listppi,dicpairs.keys())
    cn_reg = CN(listreg,dicpairs.keys())
    cn_met = CN(listmet,dicpairs.keys())
    print "Common neighbors computed."
    FSW_int = FSW(listint,dicpairs.keys())
    FSW_ppi = FSW(listppi,dicpairs.keys())
    FSW_reg = FSW(listreg,dicpairs.keys())
    FSW_met = FSW(listmet,dicpairs.keys())
    print "FSW computed."
    JC_int = JC(listint,dicpairs.keys())
    JC_ppi = JC(listppi,dicpairs.keys())
    JC_reg = JC(listreg,dicpairs.keys())
    JC_met = JC(listmet,dicpairs.keys())
    print "Jaccard computed."
    sp_int = nx.shortest_path_length(Gint)
    sp_ppi = nx.shortest_path_length(Gppi)
    sp_met = nx.shortest_path_length(Gmet)
    print "Spaths computed."

    def maxmin(dic,p):
        tupla = (0.0, 0.0)
        try:
            gene1 = dic[p[0]]
            gene2 = dic[p[1]]
            par = sorted[float(gene1),float(gene2)]
        except:
            pass

        return tupla

    def tenta(dic,p):
        valor = 0.0
        try:
            valor = dic[p]
        except:
            pass
        return valor

    output = open (folder+perc+'/training.csv', 'w')

    output.write('gene1,gene2,deg_int_max,deg_int,min,deg_ppi_max,deg_ppi_min,deg_reg_max,deg_reg_min,\
    deg_met_max,deg_met_min,bet_int_max,bet_int_min,bet_ppi_max,bet_ppi_min,bet_reg_max,bet_reg_min,bet_met_max,\
    bet_met_min,regin_max,regin_min,regout_max,regout_min,metin_max,metin_min,metout_max,metout,min,cn_int,\
    cn_ppi,cn_reg,cn_met,FSW_int,FSW_ppi,FSW_reg,FSW_met,JC_int,JC_ppi,JC_reg,JC_met,sp_int,sp_ppi,sp_met\n')

    for p in dicpairs.keys():
        v_deg_int = maxmin(deg_int,p)
        v_deg_ppi = maxmin(deg_ppi,p)
        v_deg_reg = maxmin(deg_reg,p)
        v_deg_met = maxmin(deg_met,p)
        v_bet_int = maxmin(bet_int,p)
        v_bet_ppi = maxmin(bet_ppi,p)
        v_bet_reg = maxmin(bet_reg,p)
        v_bet_met = maxmin(bet_met,p)
        v_regin = maxmin(regin,p)
        v_regout = maxmin(regout,p)
        v_metin = maxmin(metin,p)
        v_metout = maxmin(metout)
        v_cn_int = tenta (cn_int)
        v_cn_ppi = tenta (cn_ppi)
        v_cn_reg = tenta (cn_reg)
        v_cn_met = tenta (cn_met)
        v_FSW_int = tenta (FSW_int)
        v_FSW_ppi = tenta (FSW_ppi)
        v_FSW_reg = tenta (FSW_reg)
        v_FSW_met = tenta (FSW_met)
        v_JC_int = tenta(JC_int)
        v_JC_ppi = tenta (JC_ppi)
        v_JC_reg = tenta (JC_reg)
        v_JC_met = tenta (JC_met)
        v_sp_int = tenta (sp_int)
        v_sp_ppi = tenta (sp_ppi)
        v_sp_met = tenta (sp_met)

        output.write(42*'%s'+'\n' % (p[0],p[1],v_deg_int[0],v_deg_int[1],v_deg_ppi[0],v_deg_ppi[1],v_deg_reg[0],v_deg_reg[1],
    v_deg_met[0],v_deg_met[1],v_bet_int[0],v_bet_int[1],v_bet_ppi[0],v_bet_ppi[1],v_bet_reg[0],v_bet_reg[1],v_bet_met[0],\
    v_bet_met[1],v_regin[0],v_regin[1],v_regout[0],v_regout[1],v_metin[0],v_metin[1],v_metout[0],v_metout[1],v_cn_int[p],\
    v_cn_ppi[p],v_cn_reg[p],v_cn_met[p],v_FSW_int[p],v_FSW_ppi[p],v_FSW_reg[p],v_FSW_met[p],v_JC_int[p],v_JC_ppi[p],v_JC_reg,
    v_JC_met[p],v_sp_int[p],v_sp_ppi[p],v_sp_met[p]))

for p in perc:
    getatt(p)