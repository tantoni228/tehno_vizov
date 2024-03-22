class Graph():
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)
    
    def construct_graph(self, nodes, init_graph):
        """ Этот метод обеспечивает симметричность графика.
        Другими словами, если существует путь от узла A к B со значением V,
        должен быть путь от узла B к узлу A со значением V."""

        """ Если же в задаче симметричнось будет не нужна, то можно будет спокойно вырезать этот метод"""

        graph = {}

        # Добавляем все вершины в граф
        for node in nodes:
            graph[node] = {}
        
        # Добавлеяем всеми данными из init_graph
        graph.update(init_graph)

        # Цикл обеспечивающий симметричность
        for node, neighbours_and_values in init_graph.items():  # достает из графа вершины и соседние вершины с их значениями
            for neighbour, value in neighbours_and_values.items():  # достает название вершины соседа и его цену
                # проверяет есть ли в словаре соседа, вершина с которой мы как раз таки получили этого соседа
                if node not in graph[neighbour]:
                    # Если нет то добавляем
                    graph[neighbour][node] = value
        
        return graph
    
    def get_nodes(self):
        return self.nodes
    
    def get_neighbours(self, curren_min_node):
        neighbours = []

        for node in self.graph[curren_min_node].keys():
            neighbours.append(node)
        
        return neighbours

    def value(self, current_min_node, neighbour):
        return self.graph[current_min_node][neighbour]


def dijkstra_search(graph, start_node):
    unvisited_nodes = graph.get_nodes()  # получаем все вершины
    shortest_path_value = {}  # здесь будет храниться значение(цена) самого короткого пути к вершине
    previous_nodes = {}  # Это связь между одной вершиной и другой

    # Устанавливаем огромное значение цены пути непосещенных узлов
    for i in unvisited_nodes:
        shortest_path_value[i] = 10 ** 9
    
    # Но стартовое обозначаем 0
    shortest_path_value[start_node] = 0

    # Алгоритм выполняется до тех пор, пока мы не посетим все узлы
    while unvisited_nodes:
        # Находим узел с наименьшей оценкой на данный момент из shortest_path_value
        current_min_node = search_current_min_node(unvisited_nodes, shortest_path_value)

        # Находим соседние вершины узла с наименшей оценкой
        neighbours = graph.get_neighbours(current_min_node)
        for neighbour in neighbours:
            # Текущее значение(новая цена пути до соседа):
            # от наименьшего узла(вся цена пути до наименшего узла) + путь от наименшего к с соседу
            current_value = shortest_path_value[current_min_node] + graph.value(current_min_node, neighbour)
            
            # Сравнивает явл ли новая цена соседа < старой
            if current_value < shortest_path_value[neighbour]:
                # Обновляем цену соседа
                shortest_path_value[neighbour] = current_value
                # Добавляем новую менее затратную вершину пути до соседа
                previous_nodes[neighbour] = current_min_node
        
        unvisited_nodes.remove(current_min_node)  # Удаляем текущее наименьшее значение

    return previous_nodes, shortest_path_value

def search_current_min_node(unvisited_nodes, shortest_path_value):
    current_min_node = None

    for node in unvisited_nodes:
        if current_min_node == None:
            current_min_node = node
        elif shortest_path_value[current_min_node] > shortest_path_value[node]:
            current_min_node = node
    
    return current_min_node

def print_result(previous_nodes, shortest_path_value, start_node, target_node):
    path = []
    node = target_node

    # Выстраиваем полноценный маршрут, так как сейчас лишь указан ближайший сосед в вершине
    while node != start_node:
        path.append(node)
        node = previous_nodes[node]
    
    path.append(start_node)

    print("Найден следующий лучший маршрут с ценностью {}.".format(shortest_path_value[target_node]))
    print(" -> ".join(reversed(path)))

# Все вершины графа
nodes = ["Reykjavik", "Oslo", "Moscow", "London", "Rome", "Berlin", "Belgrade", "Athens"]
 
init_graph = {}

# Добавление вершин в init_graph(Нельзя сразу указать init_graph["Reykjavik"]["Oslo"] = 5, иначе выйдет ошибка)
for i in nodes:
    init_graph[i] = {}

# Путь со значением от одной вершины к другой
init_graph["Reykjavik"]["Oslo"] = 5
init_graph["Reykjavik"]["London"] = 4
init_graph['London']['Berlin'] = 3
init_graph["Oslo"]["Berlin"] = 1
init_graph["Oslo"]["Moscow"] = 3
init_graph["Moscow"]["Belgrade"] = 5
init_graph["Moscow"]["Athens"] = 4
init_graph["Athens"]["Belgrade"] = 1
init_graph["Rome"]["Berlin"] = 2
init_graph["Rome"]["Athens"] = 2

graph = Graph(nodes, init_graph)
previous_nodes, shortest_path_value = dijkstra_search(graph, start_node='Reykjavik')
print(previous_nodes)
print_result(previous_nodes, shortest_path_value, start_node='Reykjavik', target_node='Belgrade')