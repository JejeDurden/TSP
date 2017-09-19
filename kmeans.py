from sklearn.cluster import KMeans
import numpy as np


def kmeans(cities_graph, K):
    coords = cities_graph.as_matrix([1,2])
    #np_graph = np.array(coords)
    kmeans = KMeans(n_clusters=K, random_state=0).fit(coords)
    # print (kmeans.label_)
