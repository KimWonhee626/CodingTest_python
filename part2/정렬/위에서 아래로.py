N = int(input())

array = []

for i in range(N):
    array.append(int(input()))
    
array = sorted(array, reverse=True) # 오름차순 정렬
    
for i in range(N):
    print(array[i], end=' ')