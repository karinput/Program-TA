import re
import pandas as pd
# import collections from defaultdict
from collections import defaultdict
import numpy as np
# from collections import Counter
import collections
import Clustering
import Accuracy
from scipy.cluster import hierarchy
import matplotlib.pyplot as plt



def load_txt():
    t = open('Dataset Revisi.txt')
    return t.readlines()

if __name__ == '__main__':

    temp = []
    merge = []
    split = []
    data = []
    newData = []
    noun = []
    new_noun = []
    # katasama = []
    # wordfreq = []

    tesa = load_txt()
    # print(tesa)

    for i in range(len(tesa)):
        tesa[i] = tesa[i].rstrip()
        if len(tesa[i]) > 1:
            temp.append(tesa[i])

    for i in range(len(temp)):
        string = temp[i]
        while i < len(temp) and temp[i][len(temp[i])-1] == ',':
            i += 1
            string += ' ' + temp[i]
        data.append(string)
    #
    # for i in range(len(data)):
    #     for j in range(len(data[i])):
    #         print(data[i][j])
    print("---------------------------------------------------------------------")

    # index = 0
    # for i in range(len(data)):
    #     tmp = data[i]
    #     while index < len(tmp):
    #         buka = tmp.find("[",index)
    #         tutup = tmp.find("]", index)
    #         if index == -1:
    #             break
    #         # index += 1
    #         newData.append(tmp[buka: tutup+1])
    # print(newData)
        # print(data[i][j])
    # for i in range(0, len(noun)):
    #     if "]," in noun[i]:
    #     # new_noun = "\n".join(str(x) for x in noun)
    #         print('&&bsp ')
    #     if "[" in noun[i]:
    #         new_noun.append(baris[i])
    # print(new_noun)
    #
    for i in range(0, len(data)):
        # if ' n ' in data[i]:
        #     string = re.sub(r'[^a-z ^-]', ' ', data[i])
            string = re.sub('\ |\'|\[|\]', '',data[i])
            # noun.append(data[i])
            string = string.split(",")
            # string.remove('n')
            noun.append(string)
    # tesa = noun

    # for i in range(len(noun)):
        # print(noun[i])


    # print (noun)
    # seen = []
    for i in range(len(noun)):
        # seen = set()
        result = []
        for item in noun[i]:
            if item not in result:
                # seen.add(item)
                result.append(item)
        merge.append(result)
     # print('result:' ,result)

    tesa = merge
    for i in range(len(tesa)):
        print(tesa[i])

    # # print(merge[0])
    #
    # (--------------------------------------------------------------------------------------------------------------)
    cluster = Clustering.ClusterAgglo(tesa)
    print("---------------------------------------------------------------------")
    data_distance = pd.DataFrame(cluster[1])
    ytdist = data_distance
    Z = hierarchy.linkage(ytdist, 'complete')
    plt.figure()
    dn = hierarchy.dendrogram(Z)

    # Now plot in given axes, improve the color scheme and use both vertical and
    # horizontal orientations:

    hierarchy.set_link_color_palette(['m', 'c', 'y', 'k'])
    fig, axes = plt.subplots(1, 2, figsize=(8, 3))
    dn1 = hierarchy.dendrogram(Z, ax=axes[0], above_threshold_color='y',
                               orientation='top')
    dn2 = hierarchy.dendrogram(Z, ax=axes[1], above_threshold_color='#bcbddc',
                               orientation='right')
    hierarchy.set_link_color_palette(None)  # reset to default after use
    plt.show()
    print("DATA DISTANC: ")
    print(data_distance)#distance value
    print("---------------------------------------------------------------------")
    print(pd.DataFrame(cluster[0]))#similarity

    # (--------------------------------------------------------------------------------------------------------------)

    # BigSim = Clustering.locateLargest(cluster[0])
    BigSim = Clustering.locateBigValue(cluster[0])
    print("Maximum similarity :",BigSim)
    # BigDistance = Clustering.locate_Largest(cluster[1])
    BigDistance,idxDistance1, idxDistance2 = Clustering.locateBigDistance(cluster[1])
    print("Maximum distance value :",BigDistance)
    print("Index Distance : ", idxDistance1, idxDistance2)

    coe = 0.7
    threshold = BigDistance*coe #mencari nilai threshold
    print( "Threshold value : ",threshold)
    synset_new = Clustering.output_synset(tesa, idxDistance1, idxDistance2)
    print("New synset : ", synset_new)
    print('----------------------------------------------------------------------')
    SynMerged = Clustering.unite_synset(synset_new)
    print("Merged synset : ", SynMerged)

    iter = 1
    while (BigDistance >= threshold):


        print('----------------------------------------------------------------------')
        datadistance1 = data_distance

        datadistance1 = datadistance1.drop([idxDistance1, idxDistance2])
        datadistance1 = datadistance1.drop([idxDistance1, idxDistance2], axis=1)
        print(datadistance1)

        tesa.pop(idxDistance1)
        tesa.pop(idxDistance2-1)
        # print("Jumlah Lama : ", len(tesa))
        #
        tesa.append(SynMerged)
        print("Jumlah Baru : ", len(tesa))
        cluster = Clustering.ClusterAgglo(tesa)

        data_distance = pd.DataFrame(cluster[1])
        print(data_distance)  # distance value

        BigSim = Clustering.locateBigValue(cluster[0])
        print("Maximum similarity :", BigSim)

        # BigDistance = Clustering.locate_Largest(cluster[1])
        BigDistance, idxDistance1, idxDistance2 = Clustering.locateBigDistance(cluster[1])
        print("Maximum distance value :", BigDistance)
        print("Index Distance : ", idxDistance1, idxDistance2)

        if BigDistance >= threshold:
            print("iterasi ke - ", iter)
            synset_new = Clustering.output_synset(tesa, idxDistance1, idxDistance2)
            print("New synset : ", synset_new)
            SynMerged = Clustering.unite_synset(synset_new)
            print("Merged synset : ", SynMerged)
            iter = iter+1

    save_result = open("Revisi 0.7.txt", 'w')
    print("PRINT FOR LOOP TESA")
    for i in range(0,len(tesa)):
        print(tesa[i])
    print("Panjang tesa : ", len(tesa))

    kata = "\n".join(str(x) for x in tesa)
    # kata = '\n'.join(tesa[i])
    save_result.write(kata)
        # kata = (str(tesa[i]).strip('[' ']'))
        # save_result.write(kata)
        # save_result.write('\n'.join(map(str, tesa[i])))


    # lines = save_result.readline()
    # line = ''

    # while lines:
    #     # print lines
    #     line = re.sub('\s{2,}', '', tesa)
    #     save_result.write(line)
    #     lines = tesa.readline()
    #     if not lines:
    #         break
    #
    # file.close()
    # files.close()

    # print ("Panjang tesa: ", len(tesa))
    # print ("Panjang tesa[0]: ", len(tesa[1]))
    # print (tesa[0][0])
    # accu = Accuracy.accuracy(text)

    text = Accuracy.load_preprocess()
    (prec, rec, fm) = Accuracy.accuracy2(text,tesa)
    # print("Precision : ", precision)
    # rec = Accuracy.accuracy(text)
    # print("Recall : ", rec)
    # Fmeas = Accuracy.accuracy(text)
    # print("F1 measure : ", Fmeas)

    print ("Precision:" , prec)
    print ("Recall:" , rec)
    print ("Fmeasure: " , fm)

    # ytdist = np.array([662., 877., 255., 412., 996., 295., 468., 268.,
    #                    400., 754., 564., 138., 219., 869., 669.])
