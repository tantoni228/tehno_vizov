# алгоритм поиска в ширину
from collections import deque  # deque - двусторонняя очередь

def search(start_node, target_node):
    search_queue = deque()
    search_queue += [(start_node, [start_node])]  # кладем в очередь стартовую вершину и путь: deque([you, [you]])
    searched = []
    
    while search_queue:
        (current_node, path) = search_queue.popleft()  # достаем и удаляем самое первое(левое) значени на выходе
        
        if not current_node in searched:  # для того чтобы не случалась зацикленность
            if goal_search(current_node, target_node):
                print(f'Target node: {current_node}, Number of nodes: {len(path)}')
                print("Path:", ' -> '.join(path))
                return True
            else:
                for neighbour in graph[current_node]:  # проверяет всех соседей данной вершины
                    search_queue.append((neighbour, path + [neighbour]))  # добавлеяет сосдей в очередь
                searched.append(current_node)
    return False

# проверяет является ли текущая вершина искомой
def goal_search(current_node, target_node):
    return current_node == target_node


# прмер заначений графа
graph = {}
graph['you'] = ['alice', 'bob', 'carl']
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = []
graph["carl"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

# 1 - начальная вершина, 2 - искомая вершина
search('you', 'thom')