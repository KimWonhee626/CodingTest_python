# N, M 입력
N, M = map(int, input().split())

result = 0
for i in range(N):
    data = list(map(int, input().split()))
    min_value = min(data)
    if result < min_value:
        result = min_value

print(result)
