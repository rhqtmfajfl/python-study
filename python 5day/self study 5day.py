##function
'''
def time(value, n):
    for i in range(n):
        print(value)

time("안녕", 5)
'''

'''
def time(n, *values):
    for i in range(n):
        for value in values:
            print(value)

    print()

#함수를 호출
time(3, '안녕', '즐거운', '파이썬')
'''

'''
def time(*values, n=2):
    for i in range(n):
        for value in values:
            print(value)

    print()
time('안녕','친구들', 'ㅎㅎ', n =3) #n을 직접 입력해서 3을 대입한다
'''

'''
#함수에 값을 넣을 때 순서를 바꿔도 원래대로 계산되고  b=10 은 디폴트 인수 이다.
#이값을 쓰거나 값이 넘어오면 그 넘어온 값을 쓴다.
def test(a, b=10, c=100):
    print(a+b+c)

test(10, 20,30)

test(a = 10, b=100, c= 200)

test(c=10, a=100, b=200)

test(10, c= 200)
'''


#리턴
'''
value = input('>')

print(value)
'''


#자료없이 리턴하기

'''
def rtest():
    print('a여')
    return #여기서 리턴되므로 함수가 종료 된다.
    print('b여')

rtest()
'''


#자료와 함께 리턴하기

#함수를 정의한다.

'''
def return_test():
    return 100

#함수를 호출합니다.

value = return_test()
print(value)
'''


#아무것도 리턴하지 않기
'''
def rtest():
    return

#함수를 호출
value = rtest()
print(value)
'''


#범위 내부의 정수를 모두 더하는 함수

'''
#함수를 선언한다.
def sumall(start, end):
    #변수를 선언한다.
    output=0
    #반복문을 돌려 숫자를 더한다.

    for i in range(start, end+1):
        output += i
    #리턴한다.

    return output

#함수를 호출

print(' 0 to 100:', sumall(0,100))
print(' 0 to 1000:', sumall(0,1000))
print(' 50 to 100:', sumall(50,100))
print(' 500 to 1000:', sumall(500,1000))

'''

#기본매개변수와 키워드 매개변수를 활용해 범위의 정수를 더하는 함수.

'''
def sumall(start =0, end = 100, step=1):
    #변수를 선언한다.
    output = 0


    #반복문을 돌려 숫자를 더한다.

    for i in range(start, end +1, step):
        output += i

    return output

#함수를 호출한다.

print('a.', sumall(0,100,10))
print('b.', sumall(end = 100))
print('c.', sumall(end = 100, step =2))

'''

#함수의 활용 - 재귀함수


#반복문으로 팩토리얼 구하기

#함수를 선언

'''
def factorial(n):
    #변수를 선언
    output = 1
    #반복문을 돌려 숫자를 더한다.
    for i in range(output, n + 1):
        output *=i

    #리턴한다.
    return output

#함수를 호출한다.

print('1!:', factorial(1))
print('2!:', factorial(2))
print('3!:', factorial(3))
print('4!:', factorial(4))
print('5!:', factorial(5))
'''


#재귀함수를 사용해 팩토리얼 구하기

#함수를 선언
'''
def factorial(n):
    #n이 0이라면 1을 리턴
    if n == 0:
        return 1
    #n이 0이 아니라면 n*(n-1)!을 리턴

    else:
        return n * factorial(n -1)
print('1!:', factorial(1))
print('2!:', factorial(2))
print('3!:', factorial(3))
print('4!:', factorial(4))
print('5!:', factorial(5))    
'''

#재귀함수 문제

#재귀함수로 구현한 피보나치 수열(1)


#함수를 선언

'''
def fibonacci(n):
    if n ==1:
        return 1
    if n ==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

#함수를 호출

print('피보(1):', fibonacci(1))
print('피보(2):', fibonacci(2))
print('피보(3):', fibonacci(3))
print('피보(4):', fibonacci(4))
print('피보(5):', fibonacci(35))

# 이 피보나치 수열은큰 숫자를 구하려고 할때시간이 많이 걸린다.

'''


#재귀함수를 구현한 피보나치 수열(2)


'''
#변수를 선언

counter = 0

#함수를 선언

def fibonacci(n):
    #어떤 피보나치 수를 구하는지 출력한다.

    print('피보({})를 구한다.'.format(n))
    global counter
    counter +=1
    #피보나치 수를 구합니다.

    if n ==1:
        return 1
    if n ==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

#ㅍ함수를 호출

fibonacci(5)
print('---')
print('fibonacci(10) 계산을 활용된 덧셈 횟수는 {}편입니다.'.format(counter))


'''


#unboundLocalError에 대한 처리

#재귀함수로 구현한 피보나치 수열

'''
#변수를 선언
counter = 0

#함수를 선언

def fibonacci(n):
    #global counter
    counter +=1

    #피보나치 수를 구합ㄴ디ㅏ.

    if n==1:
        return 1
    if n==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

#함수를 호출합니다.
print(fibonacci(10))
'''



#메모화

'''
#메모 변수를 만든다.

dictionary = { 1:1, 2:1}

#함수를 선언

def fibonacci(n):
    if n in dictionary:
        #메모가 되어 있으면 메모된 값을 리턴
        return dictionary[n]
    else:
        #메모가 되어있지않으면 값을 구함
        output = fibonacci(n-1) + fibonacci(n-2)
        dictionary[n] = output
        return output

#함수를 호출
    
print('피보(1):', fibonacci(10))
print('피보(2):', fibonacci(20))
print('피보(3):', fibonacci(30))
print('피보(4):', fibonacci(40))
print('피보(5):', fibonacci(50))

'''


#조기 리턴
'''
#함수를 선언

def fibonacci(n):
    if n in dictionary:
        #메모가 되어 있으면 메모된 값을 리턴
        return dictionary[n]
    else:
        #메모가 되어있지않으면 값을 구함
        output = fibonacci(n-1) + fibonacci(n-2)
        dictionary[n] = output
        return output
'''

#코드
'''
num = float(input('정수입력:'))

radius = num

print('2 * 3.14 * radius :', 2*3.14*radius)
print('2 * radius * radius :', 2*3.14*radius)
'''

#함수 활용 코드

'''
#함수 정의
def num():
    output= float(input('숫자입력'))
    return output
def cir(radius):
    return 2*3.14*radius
def cirarea(radius):
    return 3.14*radius*radius

radius = num()
print(cir(radius))
print(cirarea(radius))
'''

'''
pi = 3.14

def cir(radius):
    return 2*pi*radius
def cirarea(radius):
    return pi*radius*radius
'''

#함수 고급

'''
#변수값을 교환하는 튜플

a, b =10, 20

print('교환전값')
print('a:', a)
print('b:',b)
print()

#값을 교환

a,b = b,a

print('교환후 값')
print('a:',a)
print('b:',b)
print()

'''

#여러개 값 리턴하기

'''
#함수를 선언합니다.

def test():
    return (10,20)

#여러개의 값을 리턴받습니다.

a, b = test()

#출력합니다.
print('a:',a)
print('b:',b)

'''

'''
for i, value in enumerate([1,2,3,4,5]):
    print('{}번째 요소는 {}입니다.'.format(i,value))
''' 


##람다

#함수의 매개변수로 함수 전달하기

'''
#매개변수로 받은 함수를 10번 호출하는함수

def calltime(func):
    for i in range(10):
        func()

#간단한 출력하는 함수

def hello():
    print('안녕')

#조합하기
calltime(hello)

'''

#map()함수와 filter함수

#함수를 선언

def power(item):
    return item * item
def under(item):
    return item < 3

#변수를 선언
'''
list_input = [1,2,3,4,5]
'''
#map()함수를 사용
'''
output_a = map(under, list_input)
print('#map() 함수의 실행결과')
print('map(power, listinput):', output_a)
print('map(power, listinput):', list(output_a))
print()
'''

#filter()함수를 사용한다.
'''
output_b = filter(under, list_input)
print('#filter() 함수의 실행 결과')
print('filter(under_3, list_input):', output_b)
print('filter(under_3, list_input):', list(output_b))
'''


#람다

#함수를 선언한다.

power = lambda x: x*x

under_3= lambda x: x<3


#변수를 선언
'''
list_input=[1,2,3,4,5]
'''
#map()함수를 사용
'''
output_a = map(power, list_input)
print('map() 함수의 실행결과')
print('map(power, list_input):', output_a)
print('map(power, list_input):', list(output_a))
print()
'''
#filter() 함수를 사용합니다.

'''
output_b = filter(under_3, list_input)
print('#filter() 함수의 실행결과')
print('filter(under_3, list_input):', output_b)
print('filter(under_3, list_input):', list(output_b))
'''

#인라인 람다

#변수를 선언

list_input= [1,2,3,4,5]

#map() 함수를 사용한다.

output_a = map(lambda x: x*x, list_input)
print('map() 함수의 실행결과')
print('map(power, list_input):', output_a)
print('map(power, list_input):', list(output_a))
print()

#filter 함수사용


output_b = filter(lambda x: x < 3, list_input)
print('#filter() 함수의 실행결과')
print('filter(under_3, list_input):', output_b)
print('filter(under_3, list_input):', list(output_b))


















































