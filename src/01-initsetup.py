# ################################
#AUTHOR: ESTHER CAMILO          #
#e-mail: esthercamilo@gmail.com #
#################################
import os

finput = open("config.txt")
folder = finput.readline().rstrip("\n")


def makedir(namedir):
    if not os.path.exists(namedir):
        os.makedirs(namedir)

#Levels

l1 = ['100', '95', '90', '85']
l2 = ['ppi', 'reg', 'met', 'int']
l3 = ['butland', 'babu']
l4 = ['deg', 'bet', 'jc', 'complete']
l5 = ['cold', 'mix']
l6 = ['csv', 'result', 'arff']



for a in l1:
    for b in l2:
        for c in l3:
            for d in l4:
                for e in l5:
                    for f in l6:
                        path = ('%s/%s/%s/%s/%s/%s' % (a, b, c, d, e, f))
                        makedir(folder + path)


