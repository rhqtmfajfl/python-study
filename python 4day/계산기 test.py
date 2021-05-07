def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

while True:

    num1 = int(input('첫번째 : '))
    if num1 == 0:
       break

    op = input('+,-,*,/ :')
    num2 = int(input('두번째 :'))

    if op == '+':
        res = add(num1,num2)
    if op == '-':
        res = sub(num1,num2)
    if op == '*':
        res = mul(num1,num2)
    if op == '/':
        res = div(num1,num2)    
        #print(op, '없는 연산입니다.')

    print(' {}    {}    {}  =    {}'.format(num1, op, num2, res))
    
