#William Pulkownik
#Data Mining Project
#Shortest path graph
from collections import defaultdict, deque


class Graph(object):
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance


def dijkstra(graph, initial):
    explored = {initial: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in explored:
                if min_node is None:
                    min_node = node
                elif explored[node] < explored[min_node]:
                    min_node = node
        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = explored[min_node]

        for edge in graph.edges[min_node]:
            try:
                weight = current_weight + graph.distances[(min_node, edge)]
            except:
                continue
            if edge not in explored or weight < explored[edge]:
                explored[edge] = weight
                path[edge] = min_node

    return explored, path


def shortest_path(graph, origin, destination):
    explored, paths = dijkstra(graph, origin)
    full_path = deque()
    _destination = paths[destination]

    while _destination != origin:
        full_path.appendleft(_destination)
        _destination = paths[_destination]

    full_path.appendleft(origin)
    full_path.append(destination)

    return explored[destination], list(full_path)


graph = Graph()

for node in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
    graph.add_node(node)


graph.add_edge('A', 'B', 10)
graph.add_edge('A', 'C', 20)
graph.add_edge('B', 'D', 15)
graph.add_edge('C', 'D', 30)
graph.add_edge('B', 'E', 50)
graph.add_edge('D', 'E', 30)
graph.add_edge('E', 'F', 5)
graph.add_edge('F', 'G', 2)

start = input('Please enter a start Node')
end = input('Please enter an end Node:')

print(f'{shortest_path(graph, start, end)}')
