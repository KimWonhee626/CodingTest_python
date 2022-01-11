from collections import deque

N, M = map(int, input().split())

maze = []
for i in range(N):
    maze.append(list(map(int, input().split())))
    
count = 0

dx = [-1, 1, 0, 0] # 왼, 오
dy = [0, 0, -1, 1] # 상 ,하

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            # 다음에 이동할 좌표
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=N or ny>=M:
                continue
            if maze[nx][ny] == 0: # 막혀있음
                continue
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1 # 이동한 위치에 거리정보 저장
                queue.append((nx, ny))
    return maze[N-1][M-1] # 거리정보 반환

result = bfs(0, 0)
print(result)