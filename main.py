#!/usr/bin/python3

import sys
import csv
import pandas as pd

from parser import parse_args
from kmeans import kmeans

def get_csv():
    cities_graph = pd.read_csv("cities_coordinates.csv", header=None, index_col=0)
    return cities_graph

def main(arg):
    parse_args(arg)
    K = arg[0]
    cities_graph = get_csv()
    kmeans(cities_graph, K)


if __name__ == "__main__":
    main(sys.argv[1:])
