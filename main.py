#!/usr/bin/python3

import sys
import pandas as pd

from parser import parse_args
from algos import kmeans, nearest_neighbor, two_opt, three_opt

def get_csv():
    cities_graph = pd.read_csv("cities.csv", header=None)
    return cities_graph

def formatting(l):
    result = []
    for i in range(len(l)):
        result.append(l[i].name)
    return result

def get_result(K, cities_graph):
    result = []
    if K > 1:
        for i in range(0, K):
            l = []
            for index, city in cities_graph.iterrows():
                if city["cluster"] == i:
                    l.append(city)
            result.append(formatting(two_opt(three_opt(nearest_neighbor(l)))))
    else:
        l = []
        for index, city in cities_graph.iterrows():
            l.append(city)
        result.append(formatting(two_opt(three_opt(nearest_neighbor(l)))))
    return result

def file_write(result):
    f = open("kopt.txt","w")
    for i in range(len(result)):
        l = len(result[i])
        for nb in result[i]:
            f.write(str(nb) + "")
            l -= 1
            if l > 0:
                f.write(", ")
        f.write("\n")
    f.close()

def main(arg):
    parse_args(arg)
    K = int(arg[0])
    cities_graph = get_csv()
    cities_graph.columns = ['name', 'x', 'y']
    if K > 1:
        cities_graph = kmeans(cities_graph, K)
    cities_graph["marked"] = False
    result = get_result(K, cities_graph)
    file_write(result)

if __name__ == "__main__":
    main(sys.argv[1:])
