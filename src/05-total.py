__author__ = 'esther'

import os

finput = open("config.txt")
folder = finput.readline().rstrip("\n")

def makedir(namedir):
    if not os.path.exists(namedir):
        os.makedirs(namedir)


makedir(folder + "TOTAL/undersampling/babu/csv/")
makedir(folder + "TOTAL/undersampling/butland/csv/")
makedir(folder + "TOTAL/undersampling/babu/arff/")
makedir(folder + "TOTAL/undersampling/butland/arff/")
makedir(folder + "TOTAL/undersampling/babu/result_meta/")
makedir(folder + "TOTAL/undersampling/butland/result_meta/")
makedir(folder + "TOTAL/undersampling/babu/result_j48/")
makedir(folder + "TOTAL/undersampling/butland/result_j48/")



def getdic(f):
    f.readline()
    dic = {}
    for line in f:
        d = line.split(',')
        try:
            dic[(d[0], d[1])] = d[2:]
        except:
            pass
    return dic

#babu

f1=open(folder+'100/ppi/babu/complete/training.csv')
dicbabuppi = getdic(f1)
f2=open(folder+'100/reg/babu/complete/training.csv')
dicbabureg = getdic(f2)
f3=open(folder+'100/met/babu/complete/training.csv')
dicbabumet = getdic(f3)
f4=open(folder+'100/int/babu/complete/training.csv')
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

l2 = ['int', 'ppi', 'reg', 'met']
label = 'gene1,gene2,'+','.join([x+'_deg_min,'+x+'_deg_max,'+x+'_bet_min,'+x+'_bet_max,'+x+'_jc' for x in l2])+',score\n'

#se um valor nao existe na rede eh considerado zero

def save(dicint,dicppi,dicreg,dicmet,name):
    outfile=open(folder+name,'w')
    outfile.write(label)

    for k in dicint.keys():

        d_ppi = ['0','0','0','0','0','0\n']
        d_reg = ['0','0','0','0','0','0\n']
        d_met = ['0','0','0','0','0','0\n']

        try:
            d_ppi = dicppi[k]
        except:
            pass

        try:
            d_reg = dicreg[k]
        except:
            pass

        try:
            d_met = dicmet[k]
        except:
            pass

        novalinha = dicint[k][0:-1]+d_ppi[0:-1]+d_reg[0:-1]+d_met[0:-1]+[dicint[k][-1]]
        outfile.write(k[0]+','+k[1]+','+','.join([x for x in novalinha]))



save(dicbabuint,dicbabuppi,dicbabureg,dicbabumet,'TOTAL/undersampling/babu/babu.csv')
save(dicbutint,dicbutppi,dicbutreg,dicbutmet,'TOTAL/undersampling/butland/butland.csv')





