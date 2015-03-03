# ################################
#AUTHOR: ESTHER CAMILO          #
#e-mail: esthercamilo@gmail.com #
#################################
import random as rm

finput = open("config.txt")
folder = finput.readline().rstrip("\n")

l1 = ['100', '95', '90', '85']
l2 = ['ppi', 'reg', 'met', 'int']
l3 = ['butland','babu']
l4 = ['complete','deg', 'bet']



################################################

#fill folders deg and bet
for a in l1:
    for b in l2:
        for c in l3:
            fcomplete = open(folder+a+"/"+b+"/"+c+"/complete/training.csv")
            fdeg = open(folder+a+"/"+b+"/"+c+"/deg/training.csv","w")
            fdeg.write("gene1,gene2,deg_min,deg_max,score\n")
            fbet = open(folder+a+"/"+b+"/"+c+"/bet/training.csv","w")
            fbet.write("gene1,gene2,bet_min,bet_max,score\n")
            fjc = open(folder+a+"/"+b+"/"+c+"/jc/training.csv","w")
            fjc.write("gene1,gene2,jc,score\n")
            head_complete = fcomplete.readline()
            for line in fcomplete:
                d = line.split(",")
                fdeg.write("%s,%s,%s,%s,%s" % (d[0],d[1],d[2],d[3],d[7]))
                fbet.write("%s,%s,%s,%s,%s" % (d[0],d[1],d[4],d[5],d[7]))
                fjc.write("%s,%s,%s,%s" % (d[0],d[1],d[6],d[7]))
            fcomplete.close()
            fdeg.close()
            fbet.close()
