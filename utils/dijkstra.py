from collections import deque
def dijkstra(start, edge_list, n):
    """
    n = 4
    edge_list = [[1, 2], [0, 2], [1, 3, 0], [2]]
    start = 0
    [0, 1, 1, 2] == dijkstra(start, edge_list, n)
    """
    dist = [int(2e9) for _ in range(n)]
    dist[start] = 0
    stack = deque([start])
    while len(stack) != 0:
        start = stack.pop()
        next_list = edge_list[start]
        for nex in next_list:
            ## ここの1は，辺のcostを1にしていることに相当している
            if dist[start] + 1 < dist[nex]:
                dist[nex] = dist[start] + 1 
                stack.append(nex)
                
    return dist