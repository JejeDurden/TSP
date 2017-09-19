def two_opt(graph, cycle):
    improvement = True;
    while improvement is True:
        improvement = False;
        for i in cycle.node:
            for j in cycle.node && (j != i && j != i - 1 && j != i + 1):
                if dist(cycle.node[i], cycle.node[i + 1]) + dist(cycle.node[j], cycle.node[j + 1]) > dist(cycle.node[i], cycle.node[j]) + dist(cycle.node[i + 1], cycle.node[j + 1]):
                    #remplacer i-i+1 par i-j et j-j+1 par i+1, j+1
                    improvement = True
    return cycle

def dist(a, b):
    return ()
