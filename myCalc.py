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

## 초간단 계산기
from mymodule import Add, Sub, Mul, Div

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
