'''
a = [3,5,6]

try:
    a+2
except (IndexError, TypeError):
    print('sorry')

try:
    a[2] / 0
except ZeroDivisionError as msg:
    print(msg)

print('bye')
print('*')
'''
'''
## 초간단 계산기
from mymodule import Add, Sub, Mul, Div

print('내가 진짜 메인이다.')
print(__name__)


while True:
    print(' ** 간단 계산기 ** ')
    print(' ==> [종료 :0]')
    n1 = int(input(' 첫 번째 수 : '))
    if n1 == 0:
        break
    
    op = input(' [ +, - * / ] : ')
    
    n2 = int(input(' 두 번째 수 : '))

    if op == '+':
        res = Add(n1, n2)
    elif op == '-':
        res = Sub(n1, n2)
    elif op == '*':
        res = Mul(n1, n2)
    elif op == '/':
        res = Div(n1, n2)
    else:
        print(op, '없는 연산입니다.')

    print(' {}  {}  {} = {}'.format(n1, op, n2, res))
'''
'''
coin = [500, 100, 50, 10]
n= 1260
count = 0

for coin in coin:
	count +=n//coin
	n %= coin

print(count)
'''

n = 1260
count = 0

#큰단위의 화폐부터 차례대로 확인

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin #해당화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin

    print(count)

	
