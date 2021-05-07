Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 3+2
5
>>> 10-5
5
>>> 2*3
6
>>> 10/3
3.3333333333333335
>>> 10//3
3
>>> #//는 뒤에 소수점을 없앤다
>>> 
>>> 10 % 3
1
>>> 2 ** 3
8
>>> # 2에 몇승
>>> 
>>> 2 **8
256
>>> 2**10
1024
>>> '2 + 3 *4
SyntaxError: EOL while scanning string literal
>>> 2 + 3 *4
14
>>> (2+3) *4
20
>>> (2+3) *4 + 5 /3
21.666666666666668
>>> 
>>> print("코딩 파이썬")
코딩 파이썬
>>> print(10 - 5)
5
>>> print(2 *3)
6
>>> print("korea" + 'seoul')
koreaseoul
>>> 
>>> 
>>> #입력함수 input()함수
>>> 
>>> a = input('정수 입력 : ')
정수 입력 : 12
>>> type(a)
<class 'str'>
>>>  a = int(a)
 
SyntaxError: unexpected indent
>>> a = int(a)
>>> a
12
>>> print(a)
12
>>> name = input('이름:')
이름:홍길동
>>> ㅜ믇
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    ㅜ믇
NameError: name 'ᅮ믇' is not defined
>>> name
'홍길동'
>>> a = int(input('정수입력 :'))
정수입력 :123
>>> ㅁ
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    ㅁ
NameError: name 'ᄆ' is not defined
>>> a
123
>>> age = int(input('나이 :'))
나이 :20
>>> print(name, '님은', age, '살')
홍길동 님은 20 살
>>> 
>>> 
>>> print(' a= %d, b = %f, c = %s' % (a, b, c))
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    print(' a= %d, b = %f, c = %s' % (a, b, c))
NameError: name 'b' is not defined
>>> print(' a= %d, b = %f, c = %s' % (1, 23.1, c))
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    print(' a= %d, b = %f, c = %s' % (1, 23.1, c))
NameError: name 'c' is not defined
>>> print(' a= %d, b = %f, c = %s' % (1, 23.1, cdfd))
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    print(' a= %d, b = %f, c = %s' % (1, 23.1, cdfd))
NameError: name 'cdfd' is not defined
>>> 
>>> print(' a= %d, b = %f, c = %s' % (1, 23.1, cdfd'))
				  
SyntaxError: EOL while scanning string literal
>>> print(' a= %d, b = %f, c = %s' % (1, 23.1, 'cdfd'))
 a= 1, b = 23.100000, c = cdfd
>>> a= 1
>>> b =12,1
>>> c = 'korea'
>>> print(' a= %d, b = %f, c = %s' % (a, b, c))
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    print(' a= %d, b = %f, c = %s' % (a, b, c))
TypeError: must be real number, not tuple
>>> print(' a= %d, b = %f, c = %s' % (a, b, c))
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    print(' a= %d, b = %f, c = %s' % (a, b, c))
TypeError: must be real number, not tuple
>>> type(a)
<class 'int'>
>>> type(b)
<class 'tuple'>
>>> type(c)
<class 'str'>
>>> b= 12.1
>>> print(' a= %d, b = %f, c = %s' % (a, b, c))
 a= 1, b = 12.100000, c = korea
>>> print(' a= %d, b = %.2f, c = %s' % (a, b, c))
 a= 1, b = 12.10, c = korea
>>> a= 30
>>> b=30
>>> c= 50
>>> id(a), id(b)
(1737080270032, 1737080270032)
>>> id(c)
1737080270672
>>> id(30), id(50)
(1737080270032, 1737080270672)
>>> id('star')
1737117104752
>>> id(100)
1737080460752
>>> 
>>> #위에 id 함수
>>> 
>>> 
>>> # 1-5-3 print()출력함수
>>> a = 30
>>> b= 2.345
>>> c = 'corea'
>>> print("{} {} {}".format(a, b, c))
30 2.345 corea
>>> print("{0} {1} {2}".format(a, b, c))
30 2.345 corea
>>> print("{2} {0} {2}".format(a, b, c))
corea 30 corea
>>> print("[{2:10}] [{0:10}] [{2:10}]".format(a, b, c))
[corea     ] [        30] [corea     ]
>>> print("[{2:<10}] [{0:^10}] [{2:>10}]".format(a, b, c))
[corea     ] [    30    ] [     corea]
>>> 
>>> 
>>> 
>>> print("[{1:<10.2f}] [{1:^10.2f}] [{1:>10.2f}]".format(a, b, c))
[2.35      ] [   2.35   ] [      2.35]
>>> 
>>> 
>>> 
>>> 
>>> 
>>> #파일 다루기 미리 파일을 만들어 놓고 시작하세요
>>> 
>>> f = open("c:\\dd\\cc.txt", "r", encoding = 'utf8')
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    f = open("c:\\dd\\cc.txt", "r", encoding = 'utf8')
FileNotFoundError: [Errno 2] No such file or directory: 'c:\\dd\\cc.txt'
>>> f = open("c:\\dd\\cc.txt", "w", encoding = 'utf8')
>>> f = open("c:\\dd\\cc.txt", "r", encoding = 'utf8')
>>> r = f.read()
>>> print(r)

>>> f.(write('dfasdf. \n')
   
SyntaxError: invalid syntax
>>> f.write('dfasdf. \n')
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    f.write('dfasdf. \n')
io.UnsupportedOperation: not writable
>>> f = open("c:\\dd\\cc.txt", "w", encoding = 'utf8')
>>> f.(write('dfasdf. \n')
   
SyntaxError: invalid syntax
>>> f.write('dfasdf. \n')
9
>>> f.write('adfasdfasdf.\n')
13
>>> f.close()
>>> #f에 다 쓰고 close()를 해야 된다.
>>> 
>>> 
>>> 
>>> print(" python \t linux \t oracle')
      
SyntaxError: EOL while scanning string literal
>>> print(" python \t linux \t oracl")
 python 	 linux 	 oracl
>>> print('k\t o\t r\t e\t a')
k	 o	 r	 e	 a
>>> 
>>> 
>>> # bool
>>> bool([])
False
>>> bool(True)
True
>>> bool([])
False
>>> bool(true)
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    bool(true)
NameError: name 'true' is not defined
>>> 
>>> 
>>> 
>>> 
>>> # 1-2 정수
>>> 
>>> pow(2,3)
8
>>> #pow() 함수  pow(2,3)은 2의 3승이다.
>>> 
>>> 
>>> 
>>> 
>>> #수학관련 함수
>>> 
>>> import math as m
>>> 
>>> m.pi
3.141592653589793
>>> m.cos(10)
-0.8390715290764524
>>> m.log(8,2)
3.0
>>> m.log(100, 2)
6.643856189774725
>>> m.log(100,10)
2.0
>>> m.factorial(5)
120
>>> m.factorial(10)
3628800
>>> 
>>> 
>>> #1-4 진수 다루기
>>> 
>>> a = 10
>>> a
10
>>> hex(a)
'0xa'
>>> oct(a)
'0o12'
>>> bin(a)
'0b1010'
>>> 
>>> 
>>> print('16진수 : ', hex(a), '8진수 : ', oct(a), '2진수: ', bin(a))
16진수 :  0xa 8진수 :  0o12 2진수:  0b1010
>>> b = input("정수입력 : ")
정수입력 : 123
>>> print('16진수 : ', hex(b), '8진수 : ', oct(b), '2진수: ', bin(b))
Traceback (most recent call last):
  File "<pyshell#154>", line 1, in <module>
    print('16진수 : ', hex(b), '8진수 : ', oct(b), '2진수: ', bin(b))
TypeError: 'str' object cannot be interpreted as an integer
>>> b
'123'
>>> b = int(input("정수입력 : "))
정수입력 : 123
>>> print('16진수 : ', hex(b), '8진수 : ', oct(b), '2진수: ', bin(b))
16진수 :  0x7b 8진수 :  0o173 2진수:  0b1111011
>>> 
>>> #input 사용시 자료형을 정해줘야지 int를 사용한다.
>>> #ex b = int(input("정수입력 : "))로 int 해줘야 입력값이 정수가 되지
>>> #아니면 str 문자형이 된다.
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> #실
>>> 
>>> 
>>> 
>>> #실수
>>> 
>>> a = 12.3
>>> b = 23.4
>>> 
>>> type(a)
<class 'float'>
>>> type(b)
<class 'float'>
>>> a+b
35.7
>>> k = 23.4 - 12.3
>>> k
11.099999999999998
>>> 
>>> print('%f' % (k))
11.100000
>>> print('%f' % (k, 23.4))
Traceback (most recent call last):
  File "<pyshell#185>", line 1, in <module>
    print('%f' % (k, 23.4))
TypeError: not all arguments converted during string formatting
>>> print('%f , %f' % (k, 23.4))
11.100000 , 23.400000
>>> 
>>> sum = 0,0
>>> sum = 0.0
>>> for i in range(100):
	sum = sum +1.7

	
>>> print(sum)
169.99999999999986
>>> print('%.15f' % (sum))
169.999999999999858
>>> 
>>> 
>>> 
>>> #복소수
>>> 
>>> a = 3+4j
>>> b = 5+ 2j
>>> a
(3+4j)
>>> b
(5+2j)
>>> type(a)
<class 'complex'>
>>> a.real
3.0
>>> a.imag
4.0
>>> a.conjugate()
(3-4j)
>>> 
>>> 
>>> #real은 상수 값
>>> #imag는 j의 상수값
>>> 
>>> #imag는 허수j의 상수값
>>> 
>>> #
>>> ##complex(x, y)는 x + yj로 표현됩니다.
#공액복소수는 허수의 부호를 변경합니다.
a.conjugate()는 a에 영향을 미치지 않습니다. 즉, a의 값 자체가 바뀌지는 않습니다
SyntaxError: invalid syntax
>>> 3##complex(x, y)는 x + yj로 표현됩니다.
#공액복소수는 허수의 부호를 변경합니다.a.conjugate()는 a에 영향을 미치지 않습니다. 즉, a의 값 자체가 바뀌지는 않습니다
3
>>> 
>>> 
>>> 
>>> #문자열 관련 함수
>>> 
>>> k = 'korea'
>>> type(k)
<class 'str'>
>>> k[0]
'k'
>>> k[1]
'o'
>>> 
>>> k.find('k')
0
>>> k.find('o')
1
>>> k
'korea'
>>> k.find('k')
0
>>> k.find('r')
2
>>> #find는 내가 찾고자 하는 문자의 위치를 나타낸다.
>>> 
>>> k2 = k *3
>>> k2
'koreakoreakorea'
>>> k2.count('R')
0
>>> k2.count('p')
0
>>> k2.rfind('a')
14
>>> k2.rfind('p')
-1
>>> k2.upper()
'KOREAKOREAKOREA'
>>> k2/.endswith('b')
SyntaxError: invalid syntax
>>> k2.endswith('b')
False
>>> s = '  seoul  '
>>> s
'  seoul  '
>>> k
'korea'
>>> k2
'koreakoreakorea'
>>> len(k)
5
>>> len(k2)
15
>>> len(s)
9
>>> s.strip()
'seoul'
>>> s.strip()
'seoul'
>>> s
'  seoul  '
>>> 'T'.isalpha()
True
>>> '0'.isalpha()
False
>>> '5'.isalpha()
False
>>> '7'.isnumeric()
True
>>> 'A'.isnumeric()
False
>>> 'a'.isnumeric()
False
>>> print(s, '가 좋아요')
  seoul   가 좋아요
>>> s.replace('e'.'E')
SyntaxError: invalid syntax
>>> s.replace('e','E')
'  sEoul  '
>>> bc4 = 'kbs/mbc/sbs'
>>> bc4
'kbs/mbc/sbs'
>>> bc4.split()
['kbs/mbc/sbs']
>>> a = '1,2,3,4,5'
>>> a.split()
['1,2,3,4,5']
>>> bc4.split(": ")
['kbs/mbc/sbs']
>>> 
>>> 
>>> bc5 = bc4.split(": ")
>>> bc5
['kbs/mbc/sbs']
>>> a = apple
Traceback (most recent call last):
  File "<pyshell#274>", line 1, in <module>
    a = apple
NameError: name 'apple' is not defined
>>> a = apple
Traceback (most recent call last):
  File "<pyshell#275>", line 1, in <module>
    a = apple
NameError: name 'apple' is not defined
>>> c = aple
Traceback (most recent call last):
  File "<pyshell#276>", line 1, in <module>
    c = aple
NameError: name 'aple' is not defined
>>> a = banana
Traceback (most recent call last):
  File "<pyshell#277>", line 1, in <module>
    a = banana
NameError: name 'banana' is not defined
>>> a + b
Traceback (most recent call last):
  File "<pyshell#278>", line 1, in <module>
    a + b
TypeError: can only concatenate str (not "complex") to str
>>> b * 4
(20+8j)
>>> a
'1,2,3,4,5'
>>> a = apple
Traceback (most recent call last):
  File "<pyshell#281>", line 1, in <module>
    a = apple
NameError: name 'apple' is not defined
>>> 
>>> 
>>> # 내장함수 종류
>>> 
>>> bool(1)
True
>>> bool(none)
Traceback (most recent call last):
  File "<pyshell#287>", line 1, in <module>
    bool(none)
NameError: name 'none' is not defined
>>> bool([])
False
>>> # bool은 값이 있으면 무조건 참
>>> 
>>> 
>>> aa = [2, 0, 0.0, none, [])
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> aa = [2, 0, 0.0, none, []]
Traceback (most recent call last):
  File "<pyshell#293>", line 1, in <module>
    aa = [2, 0, 0.0, none, []]
NameError: name 'none' is not defined
>>> aa = [2, 0, 0.0, []]
>>> aa
[2, 0, 0.0, []]
>>> 
>>> 
>>> #none 은 배열안에 들어갈 수 없다.
>>> 
>>> 
>>> 
>>> #내장함수 종류

>>> #__add__ 던더 add라고 읽는다. magic method
>>> 
>>> ㅁ = 50
>>> ㅁ + 5
55
>>> ㅁ.__add__(5)
55
>>> ㅁ+10
60
>>> 
>>> 
>>> #아스키 코드
>>> 
>>> #숫자를 아스키 코드로 바꿀때 chr(65)
>>> 
>>> #문자를 숫자로 바꿀 때 ord(a)
>>> 
>>> '\uac00'
'가'
>>> dir(list)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> dir(tuple)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
>>> dir(set)
['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> ord('히라가나 마')
Traceback (most recent call last):
  File "<pyshell#321>", line 1, in <module>
    ord('히라가나 마')
TypeError: ord() expected a character, but string of length 6 found
>>> chr(55203)
'힣'
>>> ord('힣')
55203
>>> for i in a:
	print(i)

	
1
,
2
,
3
,
4
,
5
>>> for i in b:
	print(i)

	
Traceback (most recent call last):
  File "<pyshell#329>", line 1, in <module>
    for i in b:
TypeError: 'complex' object is not iterable
>>> for i in c:
	print(i)

	
c
o
r
e
a
>>> a.encode()
b'1,2,3,4,5'
>>> aa = a.encode()
>>> type(aa)
<class 'bytes'>
>>> aa.decode()
'1,2,3,4,5'
>>> b.encode()
Traceback (most recent call last):
  File "<pyshell#336>", line 1, in <module>
    b.encode()
AttributeError: 'complex' object has no attribute 'encode'
>>> b
(5+2j)
>>> 
>>> 
>>> 
>>> #실전 코딩
>>> chr(90)
'Z'
>>> chr(100)
'd'
>>> odr('A')
Traceback (most recent call last):
  File "<pyshell#344>", line 1, in <module>
    odr('A')
NameError: name 'odr' is not defined
>>> ord('A')
65
>>> 
>>> 
>>> while True:
	c = input('한 문자 입력 :')
	if c == '0':
		break
	print(c, '==>',ord(c))

	
한 문자 입력 :d
d ==> 100
한 문자 입력 :f
f ==> 102
한 문자 입력 :e
e ==> 101
한 문자 입력 :q
q ==> 113
한 문자 입력 :0
>>> 
한문자 입력:
한문자 입력:
Traceback (most recent call last):
  File "<pyshell#358>", line 2, in <module>
    a = input('한문자 입력:')
KeyboardInterrupt
>>> while True:
	c = input('한 문자 입력 :')
	if c == '1':
		break
	print(c, '==>',ord(c))

	
한 문자 입력 :d
d ==> 100
한 문자 입력 :2
2 ==> 50
한 문자 입력 :3
3 ==> 51
한 문자 입력 :4
4 ==> 52
한 문자 입력 :5
5 ==> 53
한 문자 입력 :6
6 ==> 54
한 문자 입력 :1
>>> while True:
	c = input('한 문자 입력 :')
	if c == 1:
		break
	print(c, '==>',ord(c))

	
한 문자 입력 :d
d ==> 100
한 문자 입력 :1
1 ==> 49
한 문자 입력 :2
2 ==> 50
한 문자 입력 :3
3 ==> 51
한 문자 입력 :4
4 ==> 52
한 문자 입력 :5
5 ==> 53
한 문자 입력 :
	while True:
		c = input('한 문자 입력 :')
		if c == '1': # 1을 문자로 만들어줘야 한다.
			break
		print(c, '==>',ord(c))
Traceback (most recent call last):
  File "<pyshell#362>", line 5, in <module>
    print(c, '==>',ord(c))
TypeError: ord() expected a character, but string of length 0 found
>>> while True:
	c = input('한 문자 입력 :')
	if c == '1': # 1을 문자로 만들어줘야 한다.
		break
	print(c, '==>',ord(c))

	
한 문자 입력 :Traceback (most recent call last):
  File "<pyshell#364>", line 5, in <module>
    print(c, '==>',ord(c))
TypeError: ord() expected a character, but string of length 12 found
>>> while True:
	c = input('한 문자 입력 :')
	if c == '1': ## 1을 문자로 만들어줘야 한다.
		break
	print(c, '==>',ord(c))

	
한 문자 입력 :Traceback (most recent call last):
  File "<pyshell#366>", line 5, in <module>
    print(c, '==>',ord(c))
TypeError: ord() expected a character, but string of length 24 found
>>> while True:
	c = input('한 문자 입력 :')
	if c == 1:
		break
	print(c, '==>',ord(c))

	
한 문자 입력 :Traceback (most recent call last):
  File "<pyshell#368>", line 5, in <module>
    print(c, '==>',ord(c))
TypeError: ord() expected a character, but string of length 33 found
>>> while True:
	c = input('문자 입력 :')
	if c == '1':
		break
	print(c, '==>', ord(c))

	
문자 입력 :Traceback (most recent call last):
  File "<pyshell#374>", line 5, in <module>
    print(c, '==>', ord(c))
TypeError: ord() expected a character, but string of length 8 found
>>> while True:
	c = input('한 문자 입력 :')
	if c == '0':
		break
	print(c, '==>',ord(c))

	
한 문자 입력 :Traceback (most recent call last):
  File "<pyshell#376>", line 5, in <module>
    print(c, '==>',ord(c))
TypeError: ord() expected a character, but string of length 24 found
>>> 
한 문자 입력 :
한 문자 입력 :
한 문자 입력 :
Traceback (most recent call last):
  File "<pyshell#378>", line 2, in <module>
    c = input('한 문자 입력 :')
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> d
Traceback (most recent call last):
  File "<pyshell#379>", line 1, in <module>
    d
NameError: name 'd' is not defined
>>> 
>>> 
>>> 
>>> 
>>> 
>>> while True:
	c = input('한 문자 입력 :')
	    if c == '0':
		break
	    print(c, '==>',ord(c))
	    
SyntaxError: unexpected indent
>>> while True:
	c = input('한 문자 입력 :')
	if c == '0':
		break
	    print(c, '==>',ord(c))
	    
SyntaxError: unindent does not match any outer indentation level
>>> while True:
	c = input('한 문자 입력 :')
	if c == '0':
		break
	print(c, '==>',ord(c))

	
한 문자 입력 :d
d ==> 100
한 문자 입력 :0
>>> while True:
	c = input('한 문자 입력 :')
	if c == '1':
		break
	print(c, '==>',ord(c))

	
한 문자 입력 :d
d ==> 100
한 문자 입력 :2
2 ==> 50
한 문자 입력 :3
3 ==> 51
한 문자 입력 :1
>>> while True:
	c = input('한 정수 입력 :')
	if c == '0':
		break
	print(c, '==>',chr(c))

	
한 정수 입력 :d
Traceback (most recent call last):
  File "<pyshell#392>", line 5, in <module>
    print(c, '==>',chr(c))
TypeError: an integer is required (got type str)
>>> while True:
	c = input('한 정수 입력 :')
	if c == '0':
		break
	print(c, '==>',chr(c))

	
한 정수 입력 :1
Traceback (most recent call last):
  File "<pyshell#394>", line 5, in <module>
    print(c, '==>',chr(c))
TypeError: an integer is required (got type str)
>>> while True:
	c = input('한 정수 입력 :')
	if c == '0':
		break
	print(c, '==>',chr(c))

	
한 정수 입력 :3
Traceback (most recent call last):
  File "<pyshell#396>", line 5, in <module>
    print(c, '==>',chr(c))
TypeError: an integer is required (got type str)
>>> while True:
	c = input('한 정수 입력 :')
	if c == '0':
		break
	print(c, '==>', chr(c))

	
한 정수 입력 :4
Traceback (most recent call last):
  File "<pyshell#398>", line 5, in <module>
    print(c, '==>', chr(c))
TypeError: an integer is required (got type str)
>>> while True:
	c = int(input('정수 입력:'))
	if c == '0':
		break
	print(c, '==>',chr(c))

	
정수 입력:d
Traceback (most recent call last):
  File "<pyshell#404>", line 2, in <module>
    c = int(input('정수 입력:'))
ValueError: invalid literal for int() with base 10: 'd'
>>> while True:
	c = int(input('정수 입력:'))
	if c == '0':
		break
	print(c, '==>',chr(c))

	
정수 입력:2
2 ==> 
정수 입력:3
3 ==> 
정수 입력:4
4 ==> 
정수 입력:5
5 ==> 

Traceback (most recent call last):
  File "<pyshell#406>", line 2, in <module>
    c = int(input('정수 입력:'))
ValueError: invalid literal for int() with base 10: ''
>>> while True:
	c = int(input('정수 입력:'))
	if c == '0':
		break
	print(c, '==>',chr(c))

	
정수 입력:d
Traceback (most recent call last):
  File "<pyshell#408>", line 2, in <module>
    c = int(input('정수 입력:'))
ValueError: invalid literal for int() with base 10: 'd'
>>> while True:
	c = int(input('정수 입력:'))
	if c == '0':
		break
	print(c, '==>',chr(c))

	
정수 입력:99
99 ==> c
정수 입력:87
87 ==> W
정수 입력:0
0 ==> 
정수 입력:0
0 ==> 
정수 입력:0
0 ==> 
정수 입력:0
0 ==> 
정수 입력:0
0 ==> 
정수 입력:1
1 ==> 
정수 입력:1
1 ==> 
정수 입력:1
1 ==> 
정수 입력:1
1 ==> 
정수 입력:2
2 ==> 
정수 입력:3
3 ==> 
정수 입력:
Traceback (most recent call last):
  File "<pyshell#410>", line 2, in <module>
    c = int(input('정수 입력:'))
ValueError: invalid literal for int() with base 10: ''
4
>>> 
56
>>> 4
4
>>> 
>>> 
>>> #####3-1-1 list 다루기
>>> 
>>> a = [1,2,3]
>>> a
[1, 2, 3]
>>> type(a)
<class 'list'>
>>> len(a)
3
>>> a[0]
1
>>> a.append(4)
>>> a
[1, 2, 3, 4]
>>> a.append(66,60)
Traceback (most recent call last):
  File "<pyshell#424>", line 1, in <module>
    a.append(66,60)
TypeError: list.append() takes exactly one argument (2 given)
>>> a.append(66)
>>> a.append(6333)
>>> a.append([6333, 3234])
>>> a
[1, 2, 3, 4, 66, 6333, [6333, 3234]]
>>> a[7][0]
Traceback (most recent call last):
  File "<pyshell#429>", line 1, in <module>
    a[7][0]
IndexError: list index out of range
>>> a[6][0]
6333
>>> a[7][1]
Traceback (most recent call last):
  File "<pyshell#431>", line 1, in <module>
    a[7][1]
IndexError: list index out of range
>>> a = [1,2,3,4,5,66,[88,99]]
>>> a
[1, 2, 3, 4, 5, 66, [88, 99]]
>>> a[6]
[88, 99]
>>> a[6][0]4
SyntaxError: invalid syntax
>>> a[6][0]
88
>>> a = [1,2,3]
>>> a.append(4)
>>> a.append(66,60)
Traceback (most recent call last):
  File "<pyshell#439>", line 1, in <module>
    a.append(66,60)
TypeError: list.append() takes exactly one argument (2 given)
>>> a.append(66)
>>> a.append(6333)
>>> a.append([6333, 3234])
>>> a
[1, 2, 3, 4, 66, 6333, [6333, 3234]]
>>> a[6][0]
6333
>>> a.insert(2,7)
>>> a
[1, 2, 7, 3, 4, 66, 6333, [6333, 3234]]
>>> a.sort()
Traceback (most recent call last):
  File "<pyshell#447>", line 1, in <module>
    a.sort()
TypeError: '<' not supported between instances of 'list' and 'int'
>>> a.sort()
Traceback (most recent call last):
  File "<pyshell#448>", line 1, in <module>
    a.sort()
TypeError: '<' not supported between instances of 'list' and 'int'
>>> a.pop()
[6333, 3234]
>>> a
[1, 2, 3, 4, 7, 66, 6333]
>>> a.sort
<built-in method sort of list object at 0x00000194743F8600>
>>> a
[1, 2, 3, 4, 7, 66, 6333]
>>> ca = a.copy()
>>> ca
[1, 2, 3, 4, 7, 66, 6333]
>>> a.append(11)
>>> a
[1, 2, 3, 4, 7, 66, 6333, 11]
>>> c
3
>>> ac
Traceback (most recent call last):
  File "<pyshell#458>", line 1, in <module>
    ac
NameError: name 'ac' is not defined
>>> ca
[1, 2, 3, 4, 7, 66, 6333]
>>> b=a
>>> a.append(143)
>>> a
[1, 2, 3, 4, 7, 66, 6333, 11, 143]
>>> b
[1, 2, 3, 4, 7, 66, 6333, 11, 143]
>>> a[:3]
[1, 2, 3]
>>> a.extend([23,34,45])
>>> a
[1, 2, 3, 4, 7, 66, 6333, 11, 143, 23, 34, 45]
>>> a.extend(b)
>>> a
[1, 2, 3, 4, 7, 66, 6333, 11, 143, 23, 34, 45, 1, 2, 3, 4, 7, 66, 6333, 11, 143, 23, 34, 45]
>>> 0|1
1
>>> 3|5
7
>>> 