# ################################
# AUTHOR: ESTHER CAMILO          #
# e-mail: esthercamilo@gmail.com #
# ################################
import random as rm
import os

finput = open("config.txt")
folder = finput.readline().rstrip("\n")



path = folder + "TOTAL/undersampling/"


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

def undersampling(nameinput, folderoutput,b):
    fileoriginal = open(path + nameinput)
    header = fileoriginal.readline()
    listacomplete = fileoriginal.readlines()
    tupleAllAgg = getClasses(listacomplete)

    rn_agg = tupleAllAgg[0]
    rn_all = tupleAllAgg[1]
    len_rn = len(rn_all)
    half = len_rn/2
    rn_all_o = sorted(rn_all)


    for i in range(100):
        output_train = open(path + b + "/csv/" + str(i + 1) + "_train.csv", "w")
        output_test = open(path + b + "/csv/" + str(i + 1) + "_test.csv", "w")
        output_train.write(header)
        output_test.write(header)

        #embaralha
        rm.shuffle(rn_agg)
        #pega so o comeco
        sg = len(rn_all)
        rn_agg = rn_agg[0:sg]

        train_all = rn_all_o[0:half]
        test_all = rn_all_o[half:len_rn]

        train_agg = rn_agg[0:half]
        test_agg = rn_agg[half:len_rn]

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



undersampling('babu/babu.csv', 'babu/csv/', 'babu')
undersampling('butland/butland.csv', 'butland/csv/', 'butland')
