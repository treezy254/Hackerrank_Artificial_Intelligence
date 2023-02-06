"""
In the previous game, you performed DFS on the PacMan grid. It was seen that DFS might not always give the shortest path between the source and the destination.

In this game, PacMan is positioned in a grid. PacMan has to find the food using Breadth First Search (BFS), provided the grid is completely observable, perform a BFS on the grid and then print the path obtained by BFS from the PacMan to the food.
"""

import copy

pacman_x, pacman_y = list(map(int, input().split()))
food_x, food_y = list(map(int, input().split()))
n, m = list(map(int, input().split()))
grid = []
node_expanded = []
queue = []
answer_routes = None

for i in range(0, n):
    grid.append(list(map(str, input())))

directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]

queue.append([pacman_x, pacman_y, []])
while len(queue) > 0:
    x, y, r = queue.pop(0)
    routes = copy.deepcopy(r)
    routes.append([x, y])

    node_expanded.append([x, y])

    if x == food_x and y == food_y:
        if answer_routes == None:
            answer_routes = routes
            break

    for direction in directions:
        next_x, next_y = x + direction[0], y + direction[1]
        if next_x < 0 or next_x >= n or next_y < 0 and next_y >= n:
            continue

        if grid[next_x][next_y] == "-" or grid[next_x][next_y] == ".":
            grid[next_x][next_y] = '='
            queue.append([next_x, next_y, routes])

print(str(len(node_expanded)))
for point in node_expanded:
    print(str(point[0]) + " " + str(point[1]))

print(str(len(answer_routes) - 1))
for point in answer_routes:
    print(str(point[0]) + " " + str(point[1]))