Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> dir(__builtins__)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
>>> a = input()
100
>>> a
'100'
>>> type(a)
<class 'str'>
>>> a = 100
>>> a + 100
200
>>> a = input()
100
SyntaxError: multiple statements found while compiling a single statement
>>> a = int(input('정수입력 :'))
정수입력 :500
>>> int(a)
500
>>> int(a) + 100
600
>>> a = int(input())
500
>>> a
500
>>> a = int(input('정수입력 :'))
정수입력 :500
>>> city = input('어디서 오셨나요 : ')
어디서 오셨나요 : 부산시
>>> city
'부산시'
>>> a = float(input('실수입력 :'))
실수입력 :3.141592653589
>>> a
3.141592653589
>>> print(a, city)
3.141592653589 부산시
>>> # 두개를 같이 프린트 해서 나타낼 수도 있다
>>> print('aa \t bb \t cc \n dd \t ee \a ff \b gg')
aa 	 bb 	 cc 
 dd 	 ee  ff  gg
>>> print(" 서울은 좁아요 \t\t" "아주 좁아요 \n" '정말 좁아요')
 서울은 좁아요 		아주 좁아요 
정말 좁아요
>>> age = 20
>>> name = '홍길동'
>>> print(name, "님은 ", age, '살')
홍길동 님은  20 살
>>> print(name, "님은 ", age, '살 입니다.')
홍길동 님은  20 살 입니다.
>>> 
>>> print(" %s, %d " %(name,age))
 홍길동, 20 
>>> 
>>> print(" %d, %s " %(name,age))
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    print(" %d, %s " %(name,age))
TypeError: %d format: a number is required, not str
>>> print(" [%d] [%10d] [%-10d] " %(5, 5, 5))
 [5] [         5] [5         ] 
>>> print(' {} {}'.format(10, 'seoul'))
 10 seoul
>>> print(' {} {} {}'.format(10,3.14 'seoul'))
SyntaxError: invalid syntax
>>> print(' {} {} {}'.format(10,3.14, 'seoul'))
 10 3.14 seoul
>>> print(' {2} {2} {2}'.format(10,3.14, 'seoul'))
 seoul seoul seoul
>>> print(' {[2}] [{2}] [{2}]'.format(10,3.14, 'seoul'))
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    print(' {[2}] [{2}] [{2}]'.format(10,3.14, 'seoul'))
ValueError: expected '}' before end of string
>>> print(' {[2}] [{2}] [{2}]'.format(10, 30, 'seoul'))
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    print(' {[2}] [{2}] [{2}]'.format(10, 30, 'seoul'))
ValueError: expected '}' before end of string
>>> print(' {[2}] [{2}] [{2}]'.format(10,3.14, 'seoul'))
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    print(' {[2}] [{2}] [{2}]'.format(10,3.14, 'seoul'))
ValueError: expected '}' before end of string
>>> ValueError: expected '}' before end of stringprint(' {[2}] [{2}] [{2}]'.format(10,3.14, 'seoul'))
SyntaxError: invalid syntax
>>> print(' [[2}] [{2}] [{2}]'.format(10,3.14, 'seoul'))
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    print(' [[2}] [{2}] [{2}]'.format(10,3.14, 'seoul'))
ValueError: Single '}' encountered in format string
>>> print(' [{2}] [{2}] [{2}]'.format(10,3.14, 'seoul'))
 [seoul] [seoul] [seoul]
>>> print(' [{:20}] [{:20}] [{:20}]'.format(10,3.14, 'seoul'))
 [                  10] [                3.14] [seoul               ]
>>> 
>>> print(' [{<20}] [{<20}] [{<20}]'.format(10,3.14, 'seoul'))
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    print(' [{<20}] [{<20}] [{<20}]'.format(10,3.14, 'seoul'))
KeyError: '<20'
>>> print(' [{:<20}] [{:<20}] [{:<20}]'.format(10,3.14, 'seoul'))
 [10                  ] [3.14                ] [seoul               ]
>>> print(' [{:>20}] [{:>20}] [{:>30}]'.format(10,3.14, 'seoul'))
 [                  10] [                3.14] [                         seoul]
>>> print(' [{:>20}] [{:^20}] [{:>30}]'.format(10,3.14, 'seoul'))
 [                  10] [        3.14        ] [                         seoul]
>>> print(' [{:>20}] [{:^2}] [{:>3}]'.format(10,3.14, 'seoul'))
 [                  10] [3.14] [seoul]
>>> print(' [{:>20}] [{:^30}] [{:>20\}]'.format(10,3.14, 'seoul'))
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    print(' [{:>20}] [{:^30}] [{:>20\}]'.format(10,3.14, 'seoul'))
ValueError: Unknown format code '\' for object of type 'str'
>>> print(' [{:>20}] [{:^30}] [{:>20}]'.format(10,3.14, 'seoul'))
 [                  10] [             3.14             ] [               seoul]
>>> print(' [{:>20}] [{:^2f}] [{:>20}]'.format(10,3.14, 'seoul'))
 [                  10] [3.140000] [               seoul]
>>> print(' [{:>20}] [{:2f}] [{:>20}]'.format(10,3.14, 'seoul'))
 [                  10] [3.140000] [               seoul]
>>> print(' [{:>20}] [{:.2f}] [{:>20}]'.format(10,3.14, 'seoul'))
 [                  10] [3.14] [               seoul]
>>> print(' [{:>20}] [{:.30f}] [{:>20}]'.format(10,3.14, 'seoul'))
 [                  10] [3.140000000000000124344978758018] [               seoul]
>>> print(' [{:>20}] [{:.30f}] [{:>20}]'.format(2.13,2.13, 2.13))
 [                2.13] [2.129999999999999893418589635985] [                2.13]
>>> print(' %f, %.2f, %.10f'.format(2.13,2.13, 2.13))
 %f, %.2f, %.10f
>>> print(' %f, %.2f, %.10f' % (2.13,2.13, 2.13))
 2.130000, 2.13, 2.1300000000
>>> print(' %f, %.2f, %.10f'.format(2.132324,2.1231241515, 2.1253532234234234)


d
      
SyntaxError: invalid syntax
>>> print(' %f, %.2f, %.10f'.format(2.132324,2.1231241515, 2.1253532234234234))
 %f, %.2f, %.10f
>>> print(' %f, %.2f, %.10f'%(2.132324,2.1231241515, 2.1253532234234234))
 2.132324, 2.12, 2.1253532234
>>> sum =0
>>> range(10)
range(0, 10)
>>> range(0, 10)
range(0, 10)
>>> range(1, 11)
range(1, 11)
>>> for i in range(0):
	print(i)

	
>>> for i in range(10):
	print(i)

	
0
1
2
3
4
5
6
7
8
9
>>> for i in range(10):
	print(i, end = '\n')

	
0
1
2
3
4
5
6
7
8
9
>>> for i in range(1, 10):
	print(i, end = ' ')

	
1 2 3 4 5 6 7 8 9 
>>> for i in range(1, 100, 5):
	print(i, end = ' ')

	
1 6 11 16 21 26 31 36 41 46 51 56 61 66 71 76 81 86 91 96 
>>> for i in range(10):
	print(i, end = '\t')

	
0	1	2	3	4	5	6	7	8	9	
>>> Sum = 0
>>> for i in range(1, 11):
	Sum = Sum + i

	
>>> Sum
55
>>> for i in range(1, 101):
	Sum = Sum + i

	
>>> Sum
5105
>>> print(Sum)
5105
>>> for i in range(0, 101):
	Sum = Sum + i

	
>>> print(Sum)
10155
>>> sum = 0
>>> for i in range(0, 101):
	Sum = Sum + i

	
>>> print(Sum)
15205
>>> sum = 0
>>> for i in range(1, 101):
	Sum = Sum + i

	
>>> Sum
20255
>>> Sum = 0
>>> for i in range(1, 101):
	Sum = Sum + i

	
>>> print(Sum)
5050
>>> Sum
5050
>>> for i in range(1, 101):
	Sum = Sum + i

	
>>> Sum
10100
>>> print(Sum)
10100
>>> Sum = 0
>>> for i in range(1, 101):
	Sum = Sum + i

	
>>> print(Sum)
5050
>>> Sum
5050
>>> Sum = 0
>>> for i in range(1, 101):
	Sum = Sum + i

	
>>> Sum
5050
>>> Sum = 0
>>> for i in range(1, 101):
	Sum = Sum + i

	
>>> Sum
5050
>>> for i in range(2, 101,2):
	Sum = Sum + i

	
>>> Sum2= 0.0
>>> for i in range(2, 101,2):
	Sum2 = Sum2 + i

	
>>> Sum2
2550.0
>>> Sum2= 0.0
>>> for i in range(100):
	Sum2 = Sum2 + i

	
>>> Sum2
4950.0
>>> Sum2= 0.0
>>> for i in range(100):
	Sum2 = Sum2 + i

	
>>> Sum2
4950.0
>>> Sum2= 0.0
>>> for i in range(100):
	Sum2 = Sum2 + 01
	
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> for i in range(100):
	Sum2 = Sum2 + 0.1

	
>>> Sum2
9.99999999999998
>>> print(Sum2)
9.99999999999998
>>> for i in range(100):
	Sum2 = Sum2 + 0.1

	
>>> print(Sum2)
20.000000000000014
>>> Sum2 = 0.0
>>> for i in range(100):
	Sum2 = Sum2 + 0.1

	
>>> print(Sum2)
9.99999999999998
>>> print('%f]' %(Sum2))
10.000000]
>>> print('%f' %(Sum2))
10.000000
>>> print('%.30f' %(Sum2))
9.999999999999980460074766597245
>>> print('%.3f' %(Sum2))
10.000
>>> 
>>> a = int(input('정수 :'))
정수 :30
>>> ㅠ = int(input('정수 :'))
정수 :
Traceback (most recent call last):
  File "<pyshell#156>", line 1, in <module>
    ㅠ = int(input('정수 :'))
ValueError: invalid literal for int() with base 10: ''
>>> b = int(input('정수 :'))
정수 :50
>>> print(a , b)
30 50
>>> a, b = input().split()
30 20
>>> print(a + b)
3020
>>> 
>>> f = open('c:\\dd\\aa.txt', 'r', encoding='utf8')
Traceback (most recent call last):
  File "<pyshell#162>", line 1, in <module>
    f = open('c:\\dd\\aa.txt', 'r', encoding='utf8')
FileNotFoundError: [Errno 2] No such file or directory: 'c:\\dd\\aa.txt'
>>> f = open('c:\\dd\\aa.txt', 'r', encoding='utf8')
>>> print(f.read())
화요일
비
생일
>>> # 파일을 만들고 안에 있는 내용 출력 위에 내용
>>> 
>>> 
>>> # 파일 만들기
>>> f2 = open('c:\\dd\\bb.txt', 'w', encoding='utf8')
>>> f2.write('파이썬은 짱, \n')
9
>>> f2.write('위의 말 사실. \n')
10
>>> # 위에 내용은f2로 만든 bb에 내용이 없다
>>> #내용을 넣으려면 f.close()를 해줘야 한다.
>>> # *.close()
>>> 
>>> f.close()
>>> f2.close()
>>> 
>>> 
>>> f3 = open('c:\\dd\\bb.txt', 'a', encoding='utf8')
>>> for i in range(5):
	name = input('친구 이름 :')
	f3.write(name)

	
친구 이름 :홍길동
3
친구 이름 :김길동
3
친구 이름 :이길동
3
친구 이름 :박길동
3
친구 이름 :고길동
3
>>> f3.close()
>>> for i in range(5):
	name = input('친구 이름 :')
	f3.write(name)
	f3.write('\n')

	
친구 이름 :철수
Traceback (most recent call last):
  File "<pyshell#188>", line 3, in <module>
    f3.write(name)
ValueError: I/O operation on closed file.
>>> for i in range(5):
	name = input('친구 이름 :')
	f3.write(name)
	f3.write('\n')

	
친구 이름 :김철수
Traceback (most recent call last):
  File "<pyshell#190>", line 3, in <module>
    f3.write(name)
ValueError: I/O operation on closed file.
>>> f3 = open('c:\\dd\\bb.txt', 'a', encoding='utf8')
>>> for i in range(5):
	name = input('친구 이름 :')
	f3.write(name)
	f3.write('\n')

	
친구 이름 :철수
2
1
친구 이름 :김철수
3
1
친구 이름 :박철수
3
1
친구 이름 :이철수
3
1
친구 이름 :고철수
3
1
>>> f3.close()
>>> f3 = open('c:\dd\bb.txt', 'a', encoding='utf8')
Traceback (most recent call last):
  File "<pyshell#195>", line 1, in <module>
    f3 = open('c:\dd\bb.txt', 'a', encoding='utf8')
OSError: [Errno 22] Invalid argument: 'c:\\dd\x08b.txt'
>>> print(a+b)
3020
>>> a
'30'
>>> f3 = open('c:\\dd\\bb.txt', 'a', encoding='utf8')
>>> for i in range(5):
	name = input('친구 이름 :')
	f3.write(name '\n')
	
SyntaxError: invalid syntax
>>> print(a, b, a+b)
30 20 3020
>>> a = int(input('정수 : '))
정수 : 30
>>> b = int(input('정수 : '))
정수 : 50
>>> print(a, b, a+b)
30 50 80
>>> chr('A')
Traceback (most recent call last):
  File "<pyshell#204>", line 1, in <module>
    chr('A')
TypeError: an integer is required (got type str)
>>> int('A')
Traceback (most recent call last):
  File "<pyshell#205>", line 1, in <module>
    int('A')
ValueError: invalid literal for int() with base 10: 'A'
>>> str('a')
'a'
>>> ord('a')
97
>>> import keyword
>>> print(keyword.keylist)
Traceback (most recent call last):
  File "<pyshell#209>", line 1, in <module>
    print(keyword.keylist)
AttributeError: module 'keyword' has no attribute 'keylist'
>>> print(keyword.kwlist)
['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> k = 10
>>> k1 = 10
>>> k2 = 20
>>> k3 = 30
>>> k1 = 30
>>> k1 is k3
True
>>> k1 is 30
True
>>> k1 is not 20
True
>>> id(k1)
2403359091920
>>> id(30)
2403359091920
>>> 30 in not k1
SyntaxError: invalid syntax
>>> 30 not int k2
SyntaxError: invalid syntax
>>> 30 not in k2
Traceback (most recent call last):
  File "<pyshell#223>", line 1, in <module>
    30 not in k2
TypeError: argument of type 'int' is not iterable
>>> a = [1,2,3,4,5]
>>> 3 not in a
False
>>> b = (1,2,3)
>>> 3<3
False
>>> 3<=3
True
>>> 3<=3
True
>>> 3=<3
SyntaxError: cannot assign to literal
>>> 4==5
False
>>> 3<=3 and t==5
Traceback (most recent call last):
  File "<pyshell#232>", line 1, in <module>
    3<=3 and t==5
NameError: name 't' is not defined
>>> 3<=3 and 4==5
False
>>> 3<=3 or 4==5
True
>>> 3<=3 ^ 4==5
False
>>> 
>>> 
>>> 
>>> 
>>> str(1000)
'1000'
>>> int('3333')
3333
>>> # 형변환 함수
>>> 
>>> int('30)
    
SyntaxError: EOL while scanning string literal
>>> str('22)
    
SyntaxError: EOL while scanning string literal
>>> str('22')
'22'
>>> float(43.5)
43.5
>>> float('국민')
Traceback (most recent call last):
  File "<pyshell#248>", line 1, in <module>
    float('국민')
ValueError: could not convert string to float: '국민'
>>> type(a)
<class 'list'>
>>> type(b)
<class 'tuple'>
>>> sum(a)
Traceback (most recent call last):
  File "<pyshell#251>", line 1, in <module>
    sum(a)
TypeError: 'int' object is not callable
>>> sum(a), sum(b)
Traceback (most recent call last):
  File "<pyshell#252>", line 1, in <module>
    sum(a), sum(b)
TypeError: 'int' object is not callable
>>> max(a)
5
>>> sum(a)
Traceback (most recent call last):
  File "<pyshell#254>", line 1, in <module>
    sum(a)
TypeError: 'int' object is not callable
>>> min(a)
1
>>> print(sum(a))
Traceback (most recent call last):
  File "<pyshell#256>", line 1, in <module>
    print(sum(a))
TypeError: 'int' object is not callable
>>> mean(a)
Traceback (most recent call last):
  File "<pyshell#257>", line 1, in <module>
    mean(a)
NameError: name 'mean' is not defined
>>> dir(a)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> k =20
>>> dir(k)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> dir(int)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> dir(list)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> k +=30
>>> k= 20
>>> k +=30
>>> print(k)
50
>>> k.__add__(30)
80
>>> k= k+30
>>> k
80
>>> k
80
>>> print(k)
80
>>> k ==60
False
>>> dir(k)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> dir(int)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> dir(eq)
Traceback (most recent call last):
  File "<pyshell#275>", line 1, in <module>
    dir(eq)
NameError: name 'eq' is not defined
>>> dir(__eq__)
Traceback (most recent call last):
  File "<pyshell#276>", line 1, in <module>
    dir(__eq__)
NameError: name '__eq__' is not defined
>>> dir(int)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> 