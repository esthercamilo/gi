__author__ = 'esther'

finput = open("config.txt")
folder = finput.readline().rstrip("\n")

f = open('/home/esther/projects/gi_babu/100/training.csv')
o = open('/home/esther/projects/gi_babu/100/training_nominal.csv','w')
h=f.readline()
o.write(h)

for l in f:
    d = l.split(',')
    score = float(d[-1].rstrip('\n'))
    classe = ",AGG\n"
    if score < 0:
        classe = ",ALL\n"
    novalinha = ','.join(d[0:-1])+classe
    o.write(novalinha)