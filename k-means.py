import numpy as np
import pandas as pd
from math import log,ceil
from statistics import mean
# from tqdm import tqdm
from DataLoader import DataLoader

[X,y,df] = DataLoader.getDataSet()

number_of_clusters = ceil(log(len(X),2))
centroids = []

l = X.values.tolist()
initial_points = (np.linspace(0, len(X), num=number_of_clusters, endpoint=False,dtype=int))

for i in range(0,number_of_clusters):
    centroids.append(l[initial_points[i]])


clusters = [[] for i in range(9)]
index_clusters = [[] for i in range(9)]
for i in range(0,len(l)):
    min = 100000
    min_index = 0
    for j in range(0,number_of_clusters):
        dist = np.linalg.norm(np.asarray(l[i])-np.asarray(centroids[j]))
        if dist <= min:
            min = dist
            min_index = j
    clusters[min_index].append(l[i])
    index_clusters[min_index].append(i)

# print(clusters[0])
number_of_attributes = len(clusters[0][0])
flag = 0
cnt = 0

while flag != 1:
    flag = 1
    
    '''Find the new centroids'''
    for i in range(0, number_of_clusters):
        n = np.asarray(clusters[i])
        centroids[i] = (np.mean(n,axis=0).tolist())

    '''Rearrange the clusters '''  
    for i in range(0,number_of_clusters):
        c = clusters[i]
        try:
            for j in range(0,len(clusters[i])):
                min = 100000
                min_index = 0
                for k in range(0, len(centroids)):
                    # print(np.asarray(clusters[i][j])- np.asarray(centroids[k]))
                    dist = np.linalg.norm(np.asarray(clusters[i][j])-np.asarray(centroids[k]))
                    if dist <= min:
                        min = dist
                        min_index = k
                if min_index != i:
                    flag = 0
                    clusters[min_index].append(clusters[i][j])
                    index_clusters[min_index].append(index_clusters[i][j])
                    c.remove(clusters[i][j])
                    index_clusters[i].remove(index_clusters[i][j])
        except:
            pass
    cnt += 1

indices = []
# print(index_clusters[0])
for i in range(len(l)):
    for j in range(len(index_clusters)):
        if i in index_clusters[j]:
            indices.append(j)
print(np.asarray(indices))