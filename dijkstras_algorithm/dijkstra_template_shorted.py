class Node:
    def __init__(self, node):
        self.data = node


class Graph:
    def __init__(self, nodes): #создает пустую матрицу графа
        self.graph = [[0] * len(nodes) for _ in range(len(nodes))]
        self.nodes = nodes

    def connect(self, node1, node2, weight=1): #объединяет две вершины и записывает вес между ними в матрицу
        self.graph[self.nodes.index(node1)][self.nodes.index(node2)] = weight
        self.graph[self.nodes.index(node2)][self.nodes.index(node1)] = weight

    def print_graph(self): #вывод матрицы графа (в основном просто для отладки)
        for i in self.graph:
            print(i)
        
    def get_index_from_node(self, node): #выявление индекса вершины (нужно лишь в некоторых случаях, иначе ошибка)
        if not isinstance(node, Node) and not isinstance(node, int):
            raise ValueError("node must be an integer or a Node object")
        if isinstance(node, int):
            return node
        else:
            return self.nodes.index(node)


def dijkstra(self, node): #дейкстра; node = начальная вершина, вывод - мин. расстояние до всех вершин + путь к ним
    nodenum = self.get_index_from_node(node)

    dist = [None] * len(self.nodes) #список дистанций от начальной вершины до всех остальных
    for i in range(len(dist)):
        dist[i] = [float("inf")] #изначально считается, что расстояние до всех вершин бесконечно
        dist[i].append([self.nodes[nodenum]])
    
    dist[nodenum][0] = 0 #расстояние от начальной вершины до нее же равно нулю
    queue = [i for i in range(len(self.nodes))] #список всех вершин к проверке
    seen = set() #множество просмотренных вершин
    while queue:
        min_dist = float("inf")
        min_node = None
        for n in queue: #внутри цикла - поиск мин. расстояний до всех вершин по списку
            if dist[n][0] < min_dist and n not in seen:
                min_dist = dist[n][0]
                min_node = n
        queue.remove(min_node)
        seen.add(min_node)
        column = [row[self.get_index_from_node(min_node)] for row in self.graph]
        connections = [(self.nodes[row_num], column[row_num]) for row_num in range(len(column)) if column[row_num] != 0]
        for (node, weight) in connections: 
            tot_dist = weight + min_dist
            if tot_dist < dist[self.nodes.index(node)][0]:
                dist[self.nodes.index(node)][0] = tot_dist
                dist[self.nodes.index(node)][1] = list(dist[min_node][1])
                dist[self.nodes.index(node)][1].append(node)
    return dist

#код ниже - для проверки и запуска

a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")
 
graph = Graph([a,b,c,d,e,f])
 
graph.connect(a,b,5)
graph.connect(a,c,10)
graph.connect(a,e,2)
graph.connect(b,c,2)
graph.connect(b,d,4)
graph.connect(c,d,7)
graph.connect(c,f,10)
graph.connect(d,e,3)
graph.print_graph()                                                      #1 кортеж = путь к 1 вершине ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
print([(weight, [n.data for n in node]) for (weight, node) in dijkstra(graph, a)]) # вывод в формате [(расст., [путь]), (расст., [путь]), (расст., [путь]), ...]
