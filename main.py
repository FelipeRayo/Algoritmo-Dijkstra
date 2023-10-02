def dijkstra(grafo, salida):
    dist, prev = {}, {}
    result = []

    for vertice in grafo:
        dist[vertice] = float("inf")
        prev[vertice] = None
    dist[salida] = 0

    Q = [vertice for vertice in grafo]

    while Q:
        u = min(Q, key=dist.get)
        Q.remove(u)
        result.append(u)

        for vecino in grafo[u]:
            if vecino in Q and dist[vecino] > dist[u] + grafo[u][vecino]:
                dist[vecino] = dist[u] + grafo[u][vecino]
                prev[vecino] = u

    return result, dist, prev


grafo = {
    'a': {'b': 8, 'c': 6},
    'b': {'d': 4},
    'c': {'b': 4, 'd': 6, 'e': 9},
    'd': {'f': 7, 'e': 2},
    'e': {'g': 4},
    'g': {'z': 5},
    'f': {'g': 3, 'z': 8},
    'z': {}
}

s, distancia, previos = dijkstra(grafo, 'a')
print(f"{s=}")
print(f"{distancia=}")
print(f"{previos=}")