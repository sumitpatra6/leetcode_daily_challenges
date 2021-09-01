def dijkstras(nodes, graph):
    # initialize
    s = [False] * nodes
    s[0] = False
    v = []
    distance = [float('inf')] * nodes
    distance[0] = 0

    def extract_min(s, dist):
        minimum = float('inf')
        for i in range(nodes):
            if not s[i] and dist[i] < minimum:
                min_index = i
                minimum = dist[i]
        return min_index

    for n in range(nodes):
        # print(distance)
        # exttract min
        _current = extract_min(s, distance)
        s[_current] = True
        for j in range(nodes):
            if s[j] == False and graph[_current][j] > 0:
                distance[j] = min(distance[j], distance[_current] + graph[_current][j])
    print(distance)


def bellman_ford(graph, nodes):
    """
    1. initialize
    2.
    """
    dist = [float('inf')]*nodes
    dist[0] = 0

    for i in range(9):
        for j in range(9):
            for k in range(9):
                if graph[j][k] > 0:
                    if dist[k] > dist[j] + graph[j][k]:
                        dist[k] = dist[j] + graph[j][k]
    print(dist)
n = 9
graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
         [4, 0, 8, 0, 0, 0, 0, 11, 0],
         [0, 8, 0, 7, 0, 4, 0, 0, 2],
         [0, 0, 7, 0, 9, 14, 0, 0, 0],
         [0, 0, 0, 9, 0, 10, 0, 0, 0],
         [0, 0, 4, 14, 10, 0, 2, 0, 0],
         [0, 0, 0, 0, 0, 2, 0, 1, 6],
         [8, 11, 0, 0, 0, 0, 1, 0, 7],
         [0, 0, 2, 0, 0, 0, 6, 7, 0]
         ]

dijkstras(n, graph)
bellman_ford(graph, n)
