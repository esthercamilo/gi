# ################################
# AUTHOR: ESTHER CAMILO          #
# e-mail: esthercamilo@gmail.com #
# ################################
import random as rm

finput = open("config.txt")
folder = finput.readline().rstrip("\n")

l1 = ['100', '95', '90', '85']
l2 = ['ppi', 'reg', 'met', 'int']
l3 = ['butland', 'babu']
l4 = ['complete', 'deg', 'bet', 'jc']
l5 = ['cold', 'mix']
l6 = ['csv', 'result', 'arff']

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

                    # ####  generate mix training ######
                l_agg1 = []
                l_all1 = []
                for v in listacomplete:
                    d = v.split(',')
                    score = d[-1].rstrip()
                    if float(score) < 0:
                        newline1 = ','.join(d[0:-1] + ['AGG\n'])
                        l_agg1.append(newline1)
                        # l_agg1.append(v.replace(score, "AGG"))
                    else:
                        newline2 = ','.join(d[0:-1] + ['ALL\n'])
                        l_all1.append(newline2)
                        # l_all1.append(v.replace(score, "ALL"))

                s11 = len(l_agg1)
                s22 = len(l_all1)
                size1 = min(s11, s22)
                for i in range(100):
                    output_mix = open(folder + path + "mix/csv/" + str(i + 1) + ".csv", "w")
                    output_mix.write(head_complete)
                    for j in range(size1 / 2):
                        output_mix.write(l_agg1[j])
                        output_mix.write(l_all1[j])



                ##### generate cold training ######
                rm.shuffle(listacomplete)

                dic_unique = {}
                for elem in listacomplete:
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
                    output_train = open(folder + path + "cold/csv/" + str(i + 1) + "_train.csv", "w")
                    output_test = open(folder + path + "cold/csv/" + str(i + 1) + "_test.csv", "w")
                    output_train.write(head_complete)
                    output_test.write(head_complete)
                    for j in range(size / 2):
                        output_train.write(l_agg[j])
                        output_train.write(l_all[j])
                    for j in range(size / 2, size):
                        output_test.write(l_agg[j])
                        output_test.write(l_all[j])
                    output_train.close()
                    output_test.close()

    print a, " done"










