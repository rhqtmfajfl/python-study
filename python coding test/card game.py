n,m = map(int,input().split())

answer = 0
row_min = []

for j in range(n):
        row = list(map(int,input().split()))
        min_value = min(row)

answer = max(result, min_value)

print(answer);