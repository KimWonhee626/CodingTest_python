N, M = map(int, input().split())
A, B, d = map(int, input().split())

# 맵 정보 받기
Map = []
for i in range(N):
    Map.append(list(map(int, input().split())))

# 방문여부 저장하는 배열 초기화
is_visited = [[0]*M for _ in range(N)]

# 현재 좌표 방문처리
is_visited[A][B] = 1;

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def turn_left(): 
    global d
    d -= 1
    if d < 0:
        d = 3
        
count = 1;
turn_count = 0

while True:
    turn_left()
    px = A+dx[d]
    py = B+dy[d]
    if is_visited[px][py] == 0 and Map[px][py] == 0:
        A = px
        B = py
        count += 1
        turn_count = 0
        is_visited[px][py] = 1
        continue
    turn_count += 1
    ## 네 방향 모두 못갈 때
    if turn_count == 4:
        px = A-dx[d]
        py = B-dy[d]
        # 뒤쪽이 육지일 때 뒤로 한칸 이동
        if Map[px][py] == 0:
            A = px
            B = py
            turn_count = 0
        #뒤쪽이 바다일 때
        else: 
            break
        
print(count)
        
        