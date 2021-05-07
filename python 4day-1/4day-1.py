'''
## 사용자 정의 함수

def f1():  ##함수 정의
    pass   ##아무일도 하지 않음

def f2():
    print('f2...')

def f3(x): #여기서 x는 매개변수 이다.
    print(x, '가 좋아요')
    return None
def f4(x,y):
    print('{} + {} = {} '.format(x, y, x+y))
    return None
def plus(x,y):
    print('{} + {} = {}'.format(x, y, x+y))
    return None #생가ㅑㄱ되어있는 것
def minus(x,y):
    return x-y  #여기서 return을 하게 되면 밑에서 호출한 minus로 다시 돌려주는 것이다.
                #밑에서 아무 조치를 취하지않았기 때문에 아무 값도 안나온다.
                #

f1()  ##함수 호출
f2()
print(f3(100)) #처음에 f2(100)이 호출되고 그다음에 print로 return 값 none가 호출 괸다.

f3('bts')

f4(100,200)
plus(100, 200) #여기서 100과 200을 argument라고 한다.

minus(300,200)

retv = minus(300,200)
print(retv)

print(' 300- 200 =',minus(300, 200))


'''


##덧셈만 할 줄 아는 계산기

'''
def plus(x,y):
    print('{} + {} = {}'.format(x, y, x+y))
    return None #생가ㅑㄱ되어있는 것

while True:
    number = int(input('첫번째 수 : '))
    if number == 0:
        break
    number2 = int(input('두번째 수 : '))

    plus(number, number2)
    #print('{}+  {} = {}'.format(number,number2,number+number2))
'''


'''
def plus(x,y):
    print('{} + {} = {}'.format(x, y, x+y))
    return x+y #생가ㅑㄱ되어있는 것
def add(x,y):
    return x+y

while True:
    number = int(input('첫번째 수 : '))
    if number == 0:
        break
    number2 = int(input('두번째 수 : '))

    retv = add(number, number2)
    print('{}+  {} = {}'.format(number,number2,retv))
'''

'''
#초간단 계산기
def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mul(x,y):
    return x * y

def div(x,y):
    return x /y



while True:
    print('** 간단계산기**')
    n1 = int(input('첫번째수 입력 : '))
    if n1 == 0:
        break

   
    op = input('[+,-,*,/] : ')
    n2 = int(input('두번째 수 입력'))

    if op == '+':
        res = add(n1,n2)
    if op == '-':
        res = sub(n1,n2)
    if op == '*':
        res = mul(n1,n2)
    if op == '/':
        res = int(div(n1,n2))
        print(op, '없는 연산입니다.')

    print(' {}  {}  {} = {}'.format(n1, op, n2, res))
'''
'''
def disp(name = '만수르'):
    print(name,  '님은 돈이 많아요...')

#disp()
#disp('홍길동')

def disp2(x):
    for i in x:
        print(i)


def disp3(x):
    print(x)

def disp4(*x): #list의 개별값이 tuple 형태로 전달
    for i in x:
        print(i, end = ' ')

    print(x)

def sum(x):
    s = 0
    for i in x:
            s = s + i
    return s

def sum100(*x):
    s = 0
    for i in x:
            s = s + i
    return s


'''

'''
a = [3,6,9]
b=a
disp2(a)
disp3(a)
print(id(a),id(b))
disp4(*a)

print(sum(a))
print(sum([1,2,3,4,5,6]))

print(sum100(*a))
'''

'''
#빌트인  함수명은 허용되나 사용하면 안된다.

#del min, sum

color = {'black' : '검정', 'yellow' : '노랑', 'blue' : '파랑'} #앞에 key 뒤에 value

def disp_color(**x):
    for key, value in x.items():
        print(key, value)
    print(x['black'], x['yellow'], x['blue']) #index를 문자로 준다.    

disp_color(**color)
'''



'''
gg =500
def f1(x):
    global gg    ##전역변수
    
    gg = 2000000 #전역변수 gg
    print(' x ==> ', x*x)

def f2(x,y):
    t = x*y   # t는 지역변수, f2함수내에서만 통용된다.
    print(t)


print(f1(100))
print(f2(100,300))
    '''


##람다 함수
lambda x :x*x
