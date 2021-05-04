Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
===================== RESTART: C:\dd\python 0503 1일차 1-2.py ====================
프로그래밍은 재밌다.
프로그래밍은 재밌다.
프로그래밍은 재밌다.
프로그래밍은 재밌다.
프로그래밍은 재밌다.
프로그래밍은 재밌다.
프로그래밍은 재밌다.
프로그래밍은 재밌다.
프로그래밍은 재밌다.
프로그래밍은 재밌다.
프로그래밍은 재밌다.
프로그래밍은 재밌다.
프로그래밍은 재밌다.
프로그래밍은 재밌다.
프로그래밍은 재밌다.
프로그래밍은 재밌다.
프로그래밍은 재밌다.
프로그래밍은 재밌다.
프로그래밍은 재밌다.
프로그래밍은 재밌다.
>>> 
===================== RESTART: C:\dd\python 0503 1일차 1-2.py ====================
프로그래밍은 재밌다.
프로그래밍은 재밌다.
프로그래밍은 재밌다.
프로그래밍은 재밌다.
프로그래밍은 재밌다.
>>> k= 20
>>> k ?= 30
SyntaxError: invalid syntax
>>> 5+3*2
11
>>> (5+3)*2
16
>>> a= 20
>>> b = 40
>>> c = 20
>>> d = 20
>>> id(20)
2087795977104
>>> id(a)
2087795977104
>>> id(b)
2087795977744
>>> id(c)
2087795977104
>>> id(b)
2087795977744
>>> id (d)
2087795977104
>>> k = 45000
>>> id(k)
2087836950160
>>> id(30)
2087795977424
>>> s = [2, 3, 4, 6]
>>> s1 = s
>>> s
[2, 3, 4, 6]
>>> s1
[2, 3, 4, 6]
>>> s = [2, 4, 6]
>>> s1 = s
>>> s
[2, 4, 6]
>>> s1
[2, 4, 6]
>>> s[0]
2
>>> s[1]
4
>>> s[2]
6
>>> s[3]
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    s[3]
IndexError: list index out of range
>>> s1[1]
4
>>> s[0] = 9
>>> s1[0]
9
>>> s2 = s.copy
>>> s
[9, 4, 6]
>>> s2
<built-in method copy of list object at 0x000001E61CD57E00>
>>> s2 = s.copy()
>>> s2
[9, 4, 6]
>>> s[0] = 1
>>> s2
[9, 4, 6]
>>> s[0]
1
>>> id(s)
2087837859328
>>> id(s1)
2087837859328
>>> id(s2)
2087837856704
>>> print("그냥 따라하기")
그냥 따라하기
>>> pirnt(10)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    pirnt(10)
NameError: name 'pirnt' is not defined
>>> print(10,20,30)
10 20 30
>>> print(10 20 30)
SyntaxError: invalid syntax
>>> print(2.7)
2.7
>>> print(2.5, 7.4, 90.56)
2.5 7.4 90.56
>>> 
>>> 10
10
>>> 10, 30 ,50
(10, 30, 50)
>>> 10 20 30
SyntaxError: invalid syntax
>>> type(10)
<class 'int'>
>>> type(-35)
<class 'int'>
>>> type(2000)
<class 'int'>
>>> type(50), type(70), type(100)
(<class 'int'>, <class 'int'>, <class 'int'>)
>>> type(3, 5, 7)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    type(3, 5, 7)
TypeError: type.__new__() argument 1 must be str, not int
>>> print("서울", "부산", "광주")
서울 부산 광주
>>> "울산", "여수", "제주"
('울산', '여수', '제주')
>>> type("대한민국")
<class 'str'>
>>> 20 + 30
50
>>> 50 -20
30
>>> 3 * 5
15
>>> 20 / 4
5.0
>>>  20 //4
 
SyntaxError: unexpected indent
>>> 20 //4
5
>>> 10/3
3.3333333333333335
>>> 10 //3
3
>>> 10 ///3
SyntaxError: invalid syntax
>>> 10 %3
1
>>> 20%10
0
>>> 2*2
4
>>> 2**4
16
>>> 4**2
16
>>> for i in range(0,11):
	print(2, "^", i , " = ", 2 **i):
		
SyntaxError: invalid syntax
>>> for i in range(0,11):
print(2, "^", i , " = ", 2 **i)

SyntaxError: expected an indented block
>>> for i in range(0,11):
         print(2, "^", i , " = ", 2 **i)

         
2 ^ 0  =  1
2 ^ 1  =  2
2 ^ 2  =  4
2 ^ 3  =  8
2 ^ 4  =  16
2 ^ 5  =  32
2 ^ 6  =  64
2 ^ 7  =  128
2 ^ 8  =  256
2 ^ 9  =  512
2 ^ 10  =  1024
>>> for i in range(0,11):
         print(2, "^", i , " = ", 2 **i)

         
2 ^ 0  =  1
2 ^ 1  =  2
2 ^ 2  =  4
2 ^ 3  =  8
2 ^ 4  =  16
2 ^ 5  =  32
2 ^ 6  =  64
2 ^ 7  =  128
2 ^ 8  =  256
2 ^ 9  =  512
2 ^ 10  =  1024
>>> 
>>> 
>>> print("복습합니다. ")
복습합니다. 
>>> 
>>> 2*3
6
>>> 2**3
8
>>> 100 / 34
2.9411764705882355
>>> 
>>> 
>>> print( "파이썬(python) - 실수를 공부합니다. ")
파이썬(python) - 실수를 공부합니다. 
>>> 
>>> 3.14
3.14
>>> 
>>> type(3.14)
<class 'float'>
>>> type(10/3)
<class 'float'>
>>> a= 10 /3
>>> print(a)
3.3333333333333335
>>> print(" a = %f \n " %a)
 a = 3.333333 
 
>>> for i in range(0,11, 2):
         print(2, "^", i , " = ", 2 **i)

         
2 ^ 0  =  1
2 ^ 2  =  4
2 ^ 4  =  16
2 ^ 6  =  64
2 ^ 8  =  256
2 ^ 10  =  1024
>>> for i in range(0,11, 3):
         print(2, "^", i , " = ", 2 **i)

         
2 ^ 0  =  1
2 ^ 3  =  8
2 ^ 6  =  64
2 ^ 9  =  512
>>> print("안녕하세요 저의 이름은 ")
안녕하세요 저의 이름은 
>>> print("안녕하세요", "저의", "이름은")
안녕하세요 저의 이름은
>>> print("'안녕하세요' 저의 이름은 ")
'안녕하세요' 저의 이름은 
>>> print(''안녕하세요' 저의 이름은 ')
SyntaxError: invalid syntax
>>> print('"안녕하세요" 저의 이름은 ')
"안녕하세요" 저의 이름은 
>>> print("문자 선택 연산자에 대해 알아볼까요?)
      
SyntaxError: EOL while scanning string literal
>>> print("문자 선택 연산자에 대해 알아볼까요?")
문자 선택 연산자에 대해 알아볼까요?
>>> print("안녕하세요" [0])
안
>>> print("안녕하세요" [1])
녕
>>> print("안녕하세요" [2])
하
>>> print("안녕하세요" [2])