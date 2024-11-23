# Method - 1
from collections import defaultdict
class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.distances[(from_node, to_node)] = distance

def dijkstra_algorithm(graph, initial):
    visited = {initial : 0}
    path = defaultdict(list)

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
        if min_node is None:
            break
        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            weight = current_weight + graph.distances[(min_node, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge].append(min_node)

    return visited, path

my_graph = Graph()
my_graph.add_node("A")
my_graph.add_node("B")
my_graph.add_node("C")
my_graph.add_node("D")
my_graph.add_node("E")
my_graph.add_node("F")
my_graph.add_node("G")
my_graph.add_edge("A", "B", 2)
my_graph.add_edge("A", "C", 5)
my_graph.add_edge("B", "C", 6)
my_graph.add_edge("B", "D", 1)
my_graph.add_edge("B", "E", 3)
my_graph.add_edge("C", "F", 8)
my_graph.add_edge("D", "E", 4)
my_graph.add_edge("E", "G", 9)
my_graph.add_edge("F", "G", 7)
#print(dijkstra_algorithm(my_graph, "A"))


# Method - 2
import heapq
class Edge:
    def __init__(self, weight, start_vertex, target_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex

class Node:
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.prev_node = None
        self.neighbors = []
        self.min_distance = float("inf")

    def __lt__(self, other_node):
        return self.min_distance < other_node.min_distance

    def add_edge(self, weight, destination_vertex):
        edge = Edge(weight, self, destination_vertex)
        self.neighbors.append(edge)

class Dijkstra:
    def __init__(self):
        self.heap = []

    def calculate(self, start_vertex):
        start_vertex.min_distance = 0
        heapq.heappush(self.heap, start_vertex)
        while self.heap:
            actual_vertex = heapq.heappop(self.heap)
            if actual_vertex.visited:
                continue
            for edge in actual_vertex.neighbors:
                start = edge.start_vertex
                target = edge.target_vertex
                new_distance = start.min_distance + edge.weight
                if new_distance < target.min_distance:
                    target.min_distance = new_distance
                    target.prev_node = start
                    heapq.heappush(self.heap, target)
            actual_vertex.visited = True

    def get_shortest_path(self, vertex):
        print(f"The shortest path to the vertex is: {vertex.min_distance}")
        actual_vertex = vertex
        while actual_vertex is not None:
            print(actual_vertex.name, end = " ")
            actual_vertex = actual_vertex.prev_node


nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")
nodeD = Node("D")
nodeE = Node("E")
nodeF = Node("F")
nodeG = Node("G")
nodeH = Node("H")

nodeA.add_edge(6, nodeB)
nodeA.add_edge(10, nodeC)
nodeA.add_edge(9, nodeD)

nodeB.add_edge(5, nodeD)
nodeB.add_edge(16, nodeE)
nodeB.add_edge(13, nodeF)

nodeC.add_edge(6, nodeD)
nodeC.add_edge(5, nodeH)
nodeC.add_edge(21, nodeG)

nodeD.add_edge(8, nodeF)
nodeD.add_edge(7, nodeH)

nodeE.add_edge(10, nodeG)

nodeF.add_edge(4, nodeE)
nodeF.add_edge(12, nodeG)

nodeH.add_edge(2, nodeF)
nodeH.add_edge(14, nodeG)

algorithm = Dijkstra()
algorithm.calculate(nodeA)
algorithm.get_shortest_path(nodeG)






