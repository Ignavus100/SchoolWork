class Node:
    def __init__(self):
        self.temp = float('inf')
        self.permanent = False
        self.edges = []


def dijkstra(graph, start_index):
    graph[start_index].temp = 0

    while True:
        current_index = None
        min_temp = float('inf')

        for i, node in enumerate(graph):
            if not node.permanent and node.temp < min_temp:
                min_temp = node.temp
                current_index = i

        if current_index is None:
            break

        current_node = graph[current_index]
        current_node.permanent = True

        for neighbor_index, weight in current_node.edges:
            neighbor = graph[neighbor_index]
            if not neighbor.permanent:
                if neighbor.temp > current_node.temp + weight:
                    neighbor.temp = current_node.temp + weight


# ---------- TEST DATA ----------
# Graph layout (adjacency list with weights):
# Node 0 → Node 1 (1), Node 2 (4)
# Node 1 → Node 2 (2), Node 3 (6)
# Node 2 → Node 3 (3)
# Node 3 → []


graph = [Node() for _ in range(4)]


graph[0].edges = [(1, 1), (2, 4)]
graph[1].edges = [(2, 2), (3, 6)]
graph[2].edges = [(3, 3)]


start_node = 0
dijkstra(graph, start_node)


for i, node in enumerate(graph):
    print(f"Node {i}: Shortest distance from Node {start_node} = {node.temp}")
