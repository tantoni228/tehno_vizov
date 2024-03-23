from collections import deque

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w) -> None:
        self.graph.append([u, v, w])


def levit(graph, start):
    # вершины, расстояние до которых и сосдей которых посчитали
    m0 = []

    # вершины, расстояние до соседей которых надо рассчитать
    m1 = deque()
    
    # вершины, до которых мы ещё не знаем, как добраться
    m2 = [x for x in range(graph.V)]
    m1.append(m2.pop(start))
    
    # массив расстояний до вершины
    dist = [float('inf') for _ in range(graph.V)]
    dist[start] = 0

    # родительские вершины
    pred = [-1 for _ in range(graph.V)]
    pred[start] = None

    while m1:
        current = m1.popleft()
        for u, v, w in graph.graph:
            if u == current:
                # мы не находили путь к этой вершине раньше
                if v in m2:
                    dist[v] = dist[u] + w
                    pred[v] = u
                    m2.remove(v)
                    m1.append(v)
                    
                # мы уже знаем какой-то путь к ней, но не от неё
                elif v in m1:
                    # нашли более короткий путь
                    if dist[v] >= dist[u] + w:
                        dist[v] = dist[u] + w
                        pred[v] = u
                
                # мы уже посчитали путь от вершины v к её соседям
                elif v in m0:
                    # нашли более короткий путь до вершины v
                    if dist[v] > dist[u] + w:
                        dist[v] = dist[u] + w
                        pred[v] = u
                        m0.remove(v)
                        # отправили вершину на перерасчёт всех путей к её соседям
                        m1.appendleft(v)

        # расчёт путей до соседей окончен
        m0.append(current)
    return pred, dist


graph = Graph(7)  # граф из 7 вершин

# Добавление рёбер с весами
graph.add_edge(0, 1, 7)
graph.add_edge(0, 2, 9)
graph.add_edge(0, 6, 14)
graph.add_edge(1, 2, 10)
graph.add_edge(1, 3, 15)
graph.add_edge(2, 3, 11)
graph.add_edge(2, 6, 2)
graph.add_edge(3, 4, 6)
graph.add_edge(4, 5, 9)
graph.add_edge(5, 6, 9)

pred, dist = levit(graph, start=0)  # запуск алгоритма Левита с начальной вершиной 0

def print_shortest_path(dest:int, pred:list, dist:list) -> None:
    path = []
    v = dest
    while v is not None:
        path.append(v)
        v = pred[v]
    path.reverse()

    print("Кратчайший путь до вершины", dest, ":", path)
    print("Стоимость пути:", dist[dest])

# Вызываем функцию для печати кратчайшего пути до вершины dest
dest = 6  # указываем нужную вершину до которой хотим найти кратчайший путь
print_shortest_path(dest, pred, dist)