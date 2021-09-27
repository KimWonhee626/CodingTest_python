N, M, K = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

first = data[N-1]
second = data[N-2]

result = 0
count = 0

for i in range(M):
    if count == M:
        break
    for j in range(K):
        result += first
        count += 1
    result += second
    count += 1
print(result)