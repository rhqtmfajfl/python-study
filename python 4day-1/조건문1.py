'''
##조건문 끝자리로 짝수와 홀수 구분

while True:
    
    number = input('정수입력: ')

    lchr = number[-1]

    lnum = int(lchr)


    
    if lnum == 0\
        or lnum==2\
        or lnum==4\
        or lnum==6\
        or lnum==8:
        print('짝수 ')
        
    if lnum == 0\
        or lnum==1\
        or lnum==3\
        or lnum==5\
        or lnum==7\
        or lnum==9:

        print('홀수 ')

'''
'''
#in 문자열 연산자를 활용해서 짝수와 홀수 구분

while True:
    num = input('정수입력:')
    
    k=num[-1]

   #a = int(k)

    if k in '02468':
        print('짝수')

    if k in '13579':
        print('홀수')


'''

'''
#나머지 연산자를 이용해 짝수와 홀 수 구분

while True:

    num = input('정수입력:')
    k = int(num[-

    if k % 2 ==0:
        print('짝수')

    if k %2 ==1:
        print('홀수')

'''


'''
##else 조건문의 활용

number = input('정수 입력:')
number = int(number)

if number % 2 == 0:
    print('짝수')
else:
    print('홀수')
'''


import datetime

now = datetime.datetime.now()

month = now.month()
if 3 <= month <= 5 :
    print('봄')
elif 6 <= month <=8:
    print('여름')    
elif 9 <= month <=11:
    print('가을')
else:
    print('겨율')

