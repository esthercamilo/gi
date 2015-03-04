# ################################
# AUTHOR: ESTHER CAMILO          #
# e-mail: esthercamilo@gmail.com #
# ################################
import random as rm

finput = open("config.txt")
folder = finput.readline().rstrip("\n")


path = folder + "TOTAL/undersampling/"


def undersampling(nameinput, folderoutput):
    fileoriginal = open(path+nameinput)
    header = fileoriginal.readline()
    listaoriginal = fileoriginal.readlines()
    rm.shuffle(listaoriginal)

    dic_unique = {}
    for elem in listaoriginal:
        dic_unique[elem[0:12]] = elem
        l_agg = []
        l_all = []
        for v in dic_unique.values():
            d = v.split(",")
            score = d[-1].rstrip()
            if float(score) < 0:
                newline1 = ','.join(d[0:-1] + ['AGG\n'])
                l_agg.append(newline1)
                #l_agg.append(v.replace(score, "AGG"))
            else:
                newline2 = ','.join(d[0:-1] + ['ALL\n'])
                l_all.append(newline2)
                #l_all.append(v.replace(score, "ALL"))

        s1 = len(l_agg)
        s2 = len(l_all)

        size = min(s1, s2)

        for i in range(100):
            output_train = open(path+folderoutput+ str(i + 1) + "_train.csv", "w")
            output_test = open(path+folderoutput+ str(i + 1) + "_test.csv", "w")
            output_train.write(header)
            output_test.write(header)
            for j in range(size / 2):
                output_train.write(l_agg[j])
                output_train.write(l_all[j])
            for j in range(size / 2, size):
                output_test.write(l_agg[j])
                output_test.write(l_all[j])
            output_train.close()
            output_test.close()

#undersampling('babu/babu.csv', 'babu/csv/')
undersampling('butland/butland.csv', 'butland/csv/')