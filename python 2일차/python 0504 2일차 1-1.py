Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print()

>>> print(123)
123
>>> 123
123
>>> 10 20 30
SyntaxError: invalid syntax
>>> 10, 20,30
(10, 20, 30)
>>> pi = 3.14159265
>>> r= 10
>>> 
>>> #변수 참조
>>> print('원주율 =", pi)
      
SyntaxError: EOL while scanning string literal
>>> print("원주율 =", pi)
원주율 = 3.14159265
>>> print("반지름 =", r)
반지름 = 10
>>> print("원의 둘레 =", 2*pi*r)
원의 둘레 = 62.831853
>>> "원의 넓이 =", pi*r*r
('원의 넓이 =', 314.159265)
>>> print("원의 넓이 =", pi*r*r)
원의 넓이 = 314.159265
>>> 원의 넓이 =, pi*r*r
SyntaxError: invalid syntax
>>> 
>>> print("원의 넓이 =", pi*r**2)
원의 넓이 = 314.159265
>>> number = 100
>>> number += 10
>>> number +=30
>>> number +=20
>>> print("number : ", number)
number :  160
>>> 
>>> #문자열 복합 대입 연산자
>>> string = "안녕하세요"
>>> string = "!"
>>> print()

>>> print(string)
!
>>> string = "안녕하세요"
>>> string ="!"
>>> string += "!"
>>> string +="!"
>>> print("string :", string)
string : !!!
>>> string = "안녕하세요"
>>> string += "!"
>>> string += "!"
>>> print("string :", string)
string : 안녕하세요!!
>>> string *= "!"
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    string *= "!"
TypeError: can't multiply sequence by non-int of type 'str'
>>> string /= "!"
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    string /= "!"
TypeError: unsupported operand type(s) for /=: 'str' and 'str'
>>> string -= "!"
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    string -= "!"
TypeError: unsupported operand type(s) for -=: 'str' and 'str'
>>> input("인사말을 입력하세요")
인사말을 입력하세요
''
>>> input("인사말을 입력하세요">)
SyntaxError: invalid syntax
>>> input("인사말을 입력하세요>")
인사말을 입력하세요>안녕하세요
'안녕하세요'
>>> string = input("인사말을 입력하세요>")
인사말을 입력하세요>안녕하세요
>>> print(string)
안녕하세요
>>> a = input("정수 입력 :")
정수 입력 :
>>> type(a)
<class 'str'>
>>> a = input("정수 입력 :")
정수 입력 :2
>>> type(a)
<class 'str'>
>>> a = int(a)
>>> a = input("정수 입력 :")
정수 입력 :d
>>> print(a)
d
>>> a = int(a)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    a = int(a)
ValueError: invalid literal for int() with base 10: 'd'
>>> a = string(a)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    a = string(a)
TypeError: 'str' object is not callable
>>> number = input("숫자를 입력하세요>")
숫자를 입력하세요>12345
>>> print(number)
12345
>>> string = input("입력> ")
입력> 52273
>>> print("자료 :", string)
자료 : 52273
>>> string = input("입력> ")
입력> true
>>> print("자료 :", string)
자료 : true
>>> print("자료형 :", type(string))
자료형 : <class 'str'>
>>> print("자료 :", string)
자료 : true
>>> 52273
52273
>>> 
>>> 
>>> print("자료 :", string)
자료 : true
>>> print("자료 :", string)
자료 : true
>>> string = input("입력> ")
입력> 52273
>>> print("자료 :", string)
자료 : 52273
>>> print("자료형 :", type(string))
자료형 : <class 'str'>
>>> 
>>> 
>>> #직접 입력
>>> 
>>> string = input("입력 :")
입력 :100
>>> print("입력 + 100:", string + 100)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    print("입력 + 100:", string + 100)
TypeError: can only concatenate str (not "int") to str
>>> string = int(input("입력 :"))
입력 :100
>>> print("입력 + 100:", string + 100)
입력 + 100: 200
>>> string_a = input("입력a>")
입력a>273
>>> int_a = int(string_a)
>>> string_b = input("입려b>")
입려b>52
>>> int_b = int(string_b)
>>> print('문자열 자료: ", string_a + string_b)
      
SyntaxError: EOL while scanning string literal
>>> print("문자열 자료: ", string_a + string_b)
문자열 자료:  27352
>>> print("숫자 자료 :", int_a + int_b)
숫자 자료 : 325
>>> test = 123.0000001
>>> str(test)
'123.0000001'
>>> repr(test)
'123.0000001'
>>> string(test)
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    string(test)
TypeError: 'int' object is not callable
>>> test = 'ㅇㅇ'
>>> string(test)
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    string(test)
TypeError: 'int' object is not callable
>>> test = "ㅇㅇ"
>>> test
'ㅇㅇ'
>>> string = test
>>> print(string)
ㅇㅇ
>>> string(test)
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    string(test)
TypeError: 'str' object is not callable
>>> test = 'ㅇㅇ'
>>> string(test)
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    string(test)
TypeError: 'str' object is not callable
>>> a= 'ㅇㅇ'
>>> string(a)
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    string(a)
TypeError: 'str' object is not callable
>>> print("숫자 자료 :", string(int_a) + string(int_b))
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    print("숫자 자료 :", string(int_a) + string(int_b))
TypeError: 'str' object is not callable
>>> print("숫자 자료 :", str(int_a) + str(int_b))
숫자 자료 : 27352
>>> output_a = int("52")
>>> output_b = int("52.273")
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    output_b = int("52.273")
ValueError: invalid literal for int() with base 10: '52.273'
>>> output_b = float("52.273")
>>> print(type(output_a), output_a)
<class 'int'> 52
>>> print(type(output_a), output_b)
<class 'int'> 52.273
>>> input_a = float(input("첫번째 숫자>"))
첫번째 숫자>273
>>> input_b = float(input("두번째 숫자>"))
두번째 숫자>52
>>> print("덧셈 결과: ", input_a + input_b)
덧셈 결과:  325.0
>>> print("뺄셈 결과: ", input_a - input_b)
뺄셈 결과:  221.0
>>> print("곱셈 결과: ", input_a * input_b)
곱셈 결과:  14196.0
>>> print("나눗셈 결과: ", input_a / input_b)
나눗셈 결과:  5.25
>>> output_a = str(52)
>>> output_b = str(52.273)
>>> 
>>> 
>>> 
>>> #문자열의 format()함수
>>> 
>>> 
>>> 
>>> "{}".format(10)
'10'
>>> 
>>> #포맷 함수로 숫자를 문자열로 변환하기
>>> 
>>> string_a = "{}".format(10)
>>> 
>>> #출력하기
>>> print(string_a)
10
>>> print(type(string_a))
<class 'str'>
>>> 
>>> 
>>> 
>>> #format() 함수로 숫자르 문자열로 변환하기
>>> 
>>> format_a = "{}만 원".format(5000)
>>> format_b = "파이썬 열공하여 첫 연봉 {}만원 만들기".format(5000)
>>> format_c = "{} {} {}".format(3000, 4000, 5000)
>>> format_d = "{} {} {}".format(1, "문자열", True)
>>> '%f, %.2f, %.10f'.format(2.13, 2.13, 2.13)
'%f, %.2f, %.10f'
>>> print('%f, %.2f, %.10f'.format(2.13, 2.13, 2.13))
%f, %.2f, %.10f
>>> 'f, %.2f, %.10f.format(2.13, 2.13, 2.13)
SyntaxError: EOL while scanning string literal
>>> %f, %.2f, %.10f.format(2.13, 2.13, 2.13)
SyntaxError: invalid syntax
>>> '%f, %.2f, %.10f' % (2.13, 2.13, 2.13)
'2.130000, 2.13, 2.1300000000'
>>> '{%f}, {%.2f}, {%.10f}'.format(2.13, 2.13, 2.13)
Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    '{%f}, {%.2f}, {%.10f}'.format(2.13, 2.13, 2.13)
KeyError: '%f'
>>> print('{%f}, {%.2f}, {%.10f}'.format(2.13, 2.13, 2.13))
Traceback (most recent call last):
  File "<pyshell#151>", line 1, in <module>
    print('{%f}, {%.2f}, {%.10f}'.format(2.13, 2.13, 2.13))
KeyError: '%f'
>>> print(format_a)
5000만 원
>>> print(format_b)
파이썬 열공하여 첫 연봉 5000만원 만들기
>>> print(format_c)
3000 4000 5000
>>> print(format_d)
1 문자열 True
>>> 
>>> 
>>> #정수
>>> 
>>> output_a = "{:d}".format(52)
>>> 
>>> #특정 칸에 출력하기
>>> 
>>> output_b = "{:5d}".format(52)
>>> output_c = "{:10d}".format(52)
>>> 
>>> 
>>> output_d = "{:05d}".format(52)
>>> output_e = "{:05d}".format(-52)
>>> 
>>> print("# 기본")
# 기본
>>> print(ouput_a)
Traceback (most recent call last):
  File "<pyshell#172>", line 1, in <module>
    print(ouput_a)
NameError: name 'ouput_a' is not defined
>>> print(output_a)
52
>>> 