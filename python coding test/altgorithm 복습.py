

'''
n= 1260
count = 0

a = [500,100,50,10]

for i in a:
    count += n //i#해당화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %=i

print(count)
'''


'''
n, m, k =map(int, input().split())

data = list(map(int, input().split()))

data.sort()#
'''

'''

n = int(input())

#n개의 정수를 입력받아 리스트에 저장
array = []

for i in range(n):
    array.append(int(input()))

#파이썬 기본정렬 라이브러리

array = sorted(array, reverse=True)

#정렬이 수행된 결과를 출력
for i in array:
    print(i, end= ' ')

'''

'''

n = int(input())

#n명의 학생 정보를 입력받아 리스트에 저장
array = []
for i in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))

'''

n, k =map(int, input().split())
result = 0


