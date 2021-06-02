# n =1260
# count = 0

# coin =[500,100,50,10]

# for coina in coin:
#     count += n //coina
#     n%=coina #n에서 coina와 n을 나누고 남은 값이 들거간다 그리고 for로 인해서 그 값이 위에서 n이 사용된다.

# print(count)


n, m, k = map(int, input.split())

data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0

while True:
     for i in range(k):
            if m == 0:
             break
         result += first
     m -=1
    if m ==0:
        break
     result += second\
m -= 1





