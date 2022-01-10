N, M = map(int, input().split())

# 얼음 틀 정보받기
mold = []
for i in range(N):
    mold.append(list(map(int, input().split())))
    
def dfs(x, y):
    if x<0 or x>=N or y<0 or y>=M:
        return False
    if mold[x][y] == 0:
        mold[x][y] = 1
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x+1, y)
        dfs(x, y-1)
        return True
    return False

count = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            count += 1
            
print(count)
    

