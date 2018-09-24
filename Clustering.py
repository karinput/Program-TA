import numpy as np

def ClusterAgglo(tesa):
    # similar = [[0 for col in range(len(tesa))] for row in range(len(tesa))]
    distancevalue = [[0 for col in range(len(tesa))] for row in range(len(tesa))]

    sim = np.zeros((len(tesa), len(tesa)))
    for i in range(0, len(tesa)):
        for j in range(0, len(tesa[i])):
            for k in range(0, len(tesa)):
                if tesa[i][j] in tesa[k]:
                    if i != k:
                        sim[i][k] = sim[i][k] + 1
                        unique = (len(tesa[i]) + len(tesa[k])) - sim[i][k]  # mencari unique words dengan menjumlahkan kedua synstes & menguranginya dengan jumlah kata yg sama
                        # print(unique)
                        distancevalue[i][k] = sim[i][k] / unique  # mencari distance value
    return sim, distancevalue

def locateBigValue(sim):
    largeValue = 0
    for i in range(0, len(sim)):
        for j in range(0, len(sim)):
            if sim[i][j] > largeValue:
                largeValue = sim[i][j]

    return largeValue

def locateBigDistance(distance):
    largeDistance = 0
    for i in range(0, len(distance)):
        for j in range(0, len(distance[i])):
            if distance[i][j] > largeDistance:
                largeDistance = distance[i][j]
                idxDistance1 = i
                idxDistance2 = j
                if largeDistance == 1:
                    break

    return largeDistance, idxDistance1, idxDistance2

def output_synset(tesa, idxDistance1, idxDistance2):
    synset = []
    synset.append(tesa[idxDistance1])
    synset.append(tesa[idxDistance2])
    return synset

def unite_synset(synset):
    if len(synset)>1:
        merged_synset = synset[0]
        for i in range(1, len(synset)):
            for j in range(0, len(synset[i])):
                if synset[i][j] not in merged_synset:
                    merged_synset.append(synset[i][j])
    return merged_synset