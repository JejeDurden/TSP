from sklearn.cluster import KMeans
import scipy

def kmeans(cities_graph, K):
    coords = cities_graph.as_matrix(['x','y'])
    kmeans = KMeans(n_clusters=K, random_state=0).fit(coords)
    cities_graph["cluster"] = kmeans.labels_
    return cities_graph

def nearest_neighbor(cities):
    result = [cities[0]]
    cities[0].marked = True
    last_marked = 0
    while (len(result) < len(cities)):
        vertex = last_marked
        dist = 100000
        for index in range(len(cities)):
            if cities[index].marked is False:
                if scipy.spatial.distance.euclidean([cities[vertex].x,cities[vertex].y], [cities[index].x,cities[index].y]) < dist:
                    last_marked = index
        cities[last_marked].marked = True
        result.append(cities[last_marked])
    return result

def two_opt(cities):
    # Change iterations to reduce computing time or to improve your result
    iterations = 1000
    improvement = True;
    while improvement is True:
        improvement = False
        for i in range(len(cities) - 1):
            for j in range(len(cities) - 1):
                if (j != i and j != i - 1 and j != i + 1):
                    if dist(cities[i], cities[i + 1]) + dist(cities[j], cities[j + 1]) > dist(cities[i], cities[j]) + dist(cities[i + 1], cities[j + 1]):
                        cities[j], cities[i + 1] = cities[i + 1], cities[j]
                        improvement = True if iterations > 0 else False
            iterations -= 1
    return cities

def three_opt(cities):
    # Change iterations to reduce computing time or to improve your result
    iterations = 1000
    improvement = True
    while improvement is True:
        improvement = False
        for i in range(len(cities) - 1):
            for j in range(len(cities) - 1):
                for k in range(len(cities) - 1):
                    if j != i and j != i - 1 and j != i + 1 and k != j and k != j and k != j + 1 and k != j - 1 and k != i and k != i + 1 and k != i and k != i - 1:
                            if dist(cities[i], cities[i + 1]) + dist(cities[j], cities[j + 1]) + dist(cities[k], cities[k + 1]) > dist(cities[i], cities[j + 1]) + dist(cities[k], cities[j]) + dist(cities[i + 1], cities[k + 1]):
                                swap = bigswap(cities[i + 1], cities[j], cities[j + 1], cities[k])
                                cities[i + 1] = swap[0]
                                cities[j] = swap[1]
                                cities[j + 1] = swap[2]
                                cities[k] = swap[3]
                                improvement = True if iterations > 0 else False
                iterations -= 1

    return cities

def dist(a, b):
    return scipy.spatial.distance.euclidean([a.x, a.y], [b.x,b.y])

def bigswap(b,c,d,e):
    temp = b
    temp2 = e
    temp3 = c
    b = d
    e = temp
    c = temp2
    d = temp3
    return ([b, c, d, e])
