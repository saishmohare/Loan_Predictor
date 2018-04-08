import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from DataLoader import DataLoader

[X,y,df] = DataLoader.getDataSet()

kmeans = KMeans(n_clusters=9, random_state=0).fit(X)
print(kmeans.cluster_centers_)
print(kmeans.predict(X))