'''
print('start')
try:
    2 /0
except ZeroDivisionError as msg:
    print(msg)
'''
'''
a = [1,2,3]

try:

    a[3] = 4
except IndexError as msg:
    print(msg)

except TypeError as msg:
    print(msg)

except ZeroDivisionError as msg:
    print(msg)
    
except(IndexError, TypeError, ZeroDivisionError):
    print('셋중하나')


finally:
    print('에러와 상관없이 무조건 실행')




else:
    print('위 세계는 아니다')    

print('end')
'''

import os 

while True:
    print('1. 메모장')
    print('2. 계산기')
    print('3. 그림판')
    print('4. 크롬')
    print('0. 종료')

    sw = input(' 선택해 주세요 [    ]\b\b\b')

    if sw == '0':
        print('안녕히계세요')
        break

    if sw == '1':
        os.system('notepad')
    elif sw == '2':
        os.system('calc')
    elif sw == '3':
        os.system('mspaint')
    elif sw == '4':
        os.system('start chrome')
    else:
        print(sw, '없는 메뉴')
        
#os.system('start chrome')


