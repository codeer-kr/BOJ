import sys
from collections import deque

input = sys.stdin.readline


dx = (0, -1, 1, 0)
dy = (-1, 0, 0, 1)


def pArr(arr):
    for i in arr:
        print(i)


def main():
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    fish = [0] * 7

    curr_y, curr_x = 0, 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != 0:
                if matrix[i][j] == 9:
                    matrix[i][j] = 0
                    curr_y, curr_x = i, j
                else:
                    fish[matrix[i][j]] += 1

    def bfs(start):
        nonlocal baby_size

        que = deque()
        que.append(start)
        visited = [[0] * n for _ in range(n)]
        visited[start[0]][start[1]] = 1
        while que:
            y, x = que.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n and visited[ny][nx] == 0:
                    if not (baby_size < matrix[ny][nx]):
                        visited[ny][nx] = visited[y][x] + 1
                        que.append((ny, nx))
                    if 0 < matrix[ny][nx] < baby_size:
                        fish[matrix[ny][nx]] -= 1
                        matrix[ny][nx] = 0
                        pArr(matrix)
                        print(baby_size)
                        print(visited[ny][nx] - 1)
                        print()
                        return (ny, nx, visited[ny][nx] - 1)
        return -1

    baby_size = 2
    time = 0
    count = 0

    while True:
        edible = sum(fish[1:baby_size])
        if not edible:
            break

        result = bfs((curr_y, curr_x))
        if result == -1:
            break

        next_y, next_x, spent = result
        count += 1
        time += spent
        curr_y, curr_x = next_y, next_x
        if baby_size == count:
            baby_size += 1
            count = 0

    print(time)
    print(fish)
    pArr(matrix)


main()
