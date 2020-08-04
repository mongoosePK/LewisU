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


def dijkstrasAlgorithm(graph, initial):
    visited = {initial: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes:
        smallest_node = None
        for node in nodes:
            if node in visited:
                if smallest_node is None:
                    smallest_node = node
                elif visited[node] < visited[smallest_node]:
                    smallest_node = node
        if smallest_node is None:
            break

        nodes.remove(smallest_node)
        current_weight = visited[smallest_node]

        for edge in graph.edges[smallest_node]:
            try:
                weight = current_weight + graph.distances[(smallest_node, edge)]
            except:
                continue
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = smallest_node

    return visited, path

#this function calls the dijkstra algorithm
#then it appends
def shortest_path(graph, start_node, end):
    visited, paths = dijkstrasAlgorithm(graph, start_node)
    whole_path = deque()
    #underscore for function definition of _end
    _end = paths[end]

    while _end != start_node:
        whole_path.appendleft(_end)
        _end = paths[_end]

    whole_path.appendleft(start_node)
    whole_path.append(end)

    return visited[end], list(whole_path)
#END Graph Class Def
# here I will make up my graph
graph = Graph()

for node in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
    graph.add_node(node)

graph.add_edge('A', 'B', 10)
graph.add_edge('A', 'C', 20)
graph.add_edge('B', 'D', 15)
graph.add_edge('C', 'D', 30)
graph.add_edge('B', 'E', 50)
graph.add_edge('D', 'E', 30)
graph.add_edge('E', 'F', 5)
graph.add_edge('F', 'G', 2)

start = input('Please enter a start Node: ')
end = input('Please enter an end Node: ')
print(f'{shortest_path(graph, start, end)}')