# ################################
# AUTHOR: ESTHER CAMILO          #
# e-mail: esthercamilo@gmail.com #
# ################################
import random as rm
import sys

finput = open("config.txt")
folder = finput.readline().rstrip("\n")

l1 = ['100', '95', '90', '85']
l2 = ['int', 'ppi', 'reg', 'met']
l3 = ['butland','babu']
l4 = ['complete', 'deg', 'bet', 'jc']
#l5 = ['cold', 'mix']
#l6 = ['csv', 'result', 'arff']

#given a list of instances, it returns the tuple ([AGG],[ALL])
def getClasses(lista):
    all=[]
    agg=[]
    for elem in lista:
        d = elem.rstrip('\n').split(',')
        if float(d[-1])<0:
            novalinha = ','.join(d[0:-1])+',AGG\n'
            agg.append(novalinha)
        else:
            novalinha = ','.join(d[0:-1])+',ALL\n'
            all.append(novalinha)
    tupla = (agg,all)
    return tupla

for a in l1:
    for b in l2:
        for c in l3:
            for d in l4:
                path = ('%s/%s/%s/%s/' % (a, b, c, d))
                fcomplete = open(folder + path + "training.csv")  # sai 3 csvs daqui
                head_complete = fcomplete.readline()
                listacomplete = []

                for line in fcomplete:
                    listacomplete.append(line)

                tupleAllAgg = getClasses(listacomplete)

                for i in range(100):
                    output_train = open(folder + path + "cold/csv/" + str(i + 1) + "_train.csv", "w")
                    output_test = open(folder + path + "cold/csv/" + str(i + 1) + "_test.csv", "w")
                    output_train.write(head_complete)
                    output_test.write(head_complete)

                    #embaralha
                    rn_agg = tupleAllAgg[0]
                    rn_all = tupleAllAgg[1]
                    rm.shuffle(rn_agg)
                    #pega so o comeco
                    sg = len(rn_all) 
                    rn_agg = rn_agg[0:sg]

                    len_rn = len(rn_all)
                    half = len_rn/2 #mesmo tamanho do agg

                    #ordena para dividir em train e test
                    rn_all_o = sorted(rn_all)
                    rn_agg_o = rn_agg #esse nao deve ser ordenado senao grupos saem iguais

                    train_all = rn_all_o[0:half]
                    test_all = rn_all_o[half:len_rn]

                    train_agg = rn_agg_o[0:half]
                    test_agg = rn_agg_o[half:len_rn]

                    #save train
                    for l in train_all:
                        output_train.write(l)
                    for l in train_agg:
                        output_train.write(l)

                    #save test
                    for l in test_all:
                        output_test.write(l)
                    for l in test_agg:
                        output_test.write(l)

                    output_train.close()
                    output_test.close()
                    print a,b,c,d, " done"


                #fill mix
                for i in range(100):
                    inputmix1 = open(folder + path + "cold/csv/" + str(i + 1) + "_train.csv")
                    inputmix2 = open(folder + path + "cold/csv/" + str(i + 1) + "_test.csv")
                    outputmix = open(folder + path + "mix/csv/" + str(i + 1) + ".csv", "w")
                    outputmix.write(head_complete)
                    inputmix1.readline()
                    inputmix2.readline()
                    for line in inputmix1:
                        outputmix.write(line)
                    for line in inputmix2:
                        outputmix.write(line)
                    outputmix.close()
                    inputmix1.close()
                    inputmix2.close()









