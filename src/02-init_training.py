# ################################
# AUTHOR: ESTHER CAMILO          #
#e-mail: esthercamilo@gmail.com #
#################################
import random as rm
import networkx as nx

finput = open("config.txt")
folder = finput.readline().rstrip("\n")

l1 = ['100', '95', '90', '85']
l2 = ['ppi', 'reg', 'met', 'int']
l3 = ['babu', 'butland']
l4 = ['deg', 'bet', 'complete']
l5 = ['cold/training', 'cold/test', 'mix']
l6 = ['csv']


################################################

def readlist(c):
	f_pairs = open(folder + "files/" + c + "score.tab")
	header = f_pairs.readline();
	dic_pairs = {}  #dictionary of gene pairs
	for line in f_pairs:
		d = line.split()
		dic_pairs[(d[0], d[1])] = (d[2]).replace(",",".")
	f_pairs.close()
	return dic_pairs


dic_pairs_babu = readlist(l3[0])
dic_pairs_butland = readlist(l3[1])

#################################################

def savefile(lista, address):
	f = open(folder + address, 'w')
	for line in lista:
		f.write(line)


def jaccard(G, tuplas):
	dicjc = {}
	for t in tuplas:
		nodes = G.nodes()
		if (t[0] not in nodes) or (t[1] not in nodes):
			continue
		else:
			jc = 0.0
			n1 = G.neighbors(t[0])
			n2 = G.neighbors(t[1])
			inter = len(set(n1) & set(n2))
			union = len(set(n1) | set(n2))
			try:
				jc = inter / union
			except ZeroDivisionError:
				pass
			dicjc[t] = jc

	return dicjc



for a in l1:  #['100','95','90','85']
	#define the sub-network percentage
	per = float(a) / 100

	for b in l2:  #['ppi','reg','met','int']
		#read interaction file, shuffle, keep it in a list
		l_int = []  #interaction list
		fint = open(folder + "files/" + b + ".tab")
		for line in fint:
			d = line.split()
			l_int.append((d[0], d[1]))
		rm.shuffle(l_int)
		#take only a percetage
		size = len(l_int)
		last = int(per * size)
		l_int = l_int[0:last]  #replace list with only percentage
		#Build network
		G = None
		if b == "reg" or b == "met":
			G = nx.Graph()
		else:
			G = nx.Graph()
		for elem in l_int:
			G.add_edge(elem[0], elem[1])

		dic_deg = G.degree()
		dic_bet = nx.algorithms.centrality.betweenness_centrality(G)
		dic_jc_babu = {}
		dic_jc_butland = {}

		for c in l3:  # ['babu','butland']
			this_dic = eval("dic_pairs_" + c)
			listatuplas = this_dic.keys()
			#preds = jaccard(G, listatuplas)  #dicionario key=tuplas value=jaccard

			#generate a complete training as a dictionary
			output = []
			output.append("gene1,gene2,deg_min,deg_max,bet_min,bet_max,score\n")
			t_dic = eval("dic_pairs_" + c)
			for pa in t_dic.keys():
				try:
					degs = [dic_deg[pa[0]], dic_deg[pa[1]]]
					bets = [dic_bet[pa[0]], dic_bet[pa[1]]]
					#jc = preds[pa]
					degs.sort()
					bets.sort()
					score = (str(t_dic[pa]))
					lineout = pa[0] + "," + pa[1] + ',' + str(degs[0]) + ',' + str(degs[1]) \
							  + ',' + str(bets[0]) + ',' + str(bets[1])  \
							  + ',' + score + '\n'

					output.append(lineout)
				except Exception as inst:
					pass#print inst.args
			print "Saving results"
			address = "%s/%s/%s/complete/training.csv" % (a, b, c)
			savefile(output, address)

























