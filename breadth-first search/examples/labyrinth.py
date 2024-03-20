# ----------------------------------ШАБЛОН-------------------------------------------
from collections import deque


def search(start_node, target_node):
    search_queue = deque()
    search_queue += [(start_node, [start_node])]
    searched = []
    
    while search_queue:
        (current_node, path) = search_queue.popleft()
        
        if not current_node in searched:
            if goal_search(current_node, target_node):
                print(f'Target node: {current_node}, Number of nodes: {len(path)}')
                mark_shortest_path(matrix, path) # функция заменяет в марице позиции пути на '*'
                return True
            else:
                for neighbour in graph[current_node]:
                    search_queue.append((neighbour, path + [neighbour]))
                searched.append(current_node)
    return False

def goal_search(current_node, target_node):
    return current_node == target_node

#-----------------------------------------------------------------------------------------------

matrix = []
with open('labyrinth.txt', 'r', encoding='utf-8') as file:
    for line in file:
        matrix.append(list(map(int, line.strip().split())))

graph = {}
rows = len(matrix)
cols = len(matrix[0])
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] != 3:
            graph[(i, j)] = []
            if i > 0 and matrix[i - 1][j] != 3:
                graph[(i, j)].append((i - 1, j))
            if i < rows - 1 and matrix[i + 1][j] != 3:
                graph[(i, j)].append((i + 1, j))
            if j > 0 and matrix[i][j - 1] != 3:
                graph[(i, j)].append((i, j - 1))
            if j < cols - 1 and matrix[i][j + 1] != 3:
                graph[(i, j)].append((i, j + 1))
        
        if matrix[i][j] == 1:
            start_position = (i, j)
        
        if matrix[i][j] == 2:
            target_position = (i, j)

# заменяет путь на '*'
def mark_shortest_path(matrix, path):
    for node in path:
        matrix[node[0]][node[1]] = "*"

# выводит матрицу
def print_matrix():
    for i in range(rows):
        for j in range(cols):
            print(matrix[i][j], end=' ')
        print()

print_matrix()
search(start_position, target_position)
print('----------------------------')
print_matrix()