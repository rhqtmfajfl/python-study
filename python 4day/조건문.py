Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def print_n_times(value, n):
	for i in range(n):
		print(value)
    print_n_times('안녕하세요',5)
    
SyntaxError: unindent does not match any outer indentation level
>>> def print_n_times(value, n):
	for i in range(n):
		print(value)
		
    print_n_times('안녕하세요',5)
    
SyntaxError: unindent does not match any outer indentation level
>>> def print_n_times(value, n):
	for i in range(n):
		print(value)

	    print_n_times('안녕하세요',5)
	    
SyntaxError: unindent does not match any outer indentation level
>>> def print_n_times(value, n):
	for i in range(n):
		print(value)


>>>             print_n_times('안녕하세요',5)

SyntaxError: unexpected indent
>>> print_n_times('안녕하세요',5)
안녕하세요
안녕하세요
안녕하세요
안녕하세요
안녕하세요
>>> sum()#iterable 숫자 하나씩

	
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    sum()#iterable 숫자 하나씩
TypeError: sum() takes at least 1 positional argument (0 given)
\
>>> def print_n_times(n, *values):
	#n번 반복합니다.
	for i in range(n):
		#values는 리스트처럼 활용합니다.
		for value in values:
			print(value)
			#단순한 줄바꿈
			print()

			
>>> print_n_times(3, '안녕하세요', '즐거운', '파이')
안녕하세요

즐거운

파이

안녕하세요

즐거운

파이

안녕하세요

즐거운

파이

>>> print_n_times(3, '안녕하세요즐거운 파이')
안녕하세요즐거운 파이

안녕하세요즐거운 파이

안녕하세요즐거운 파이

>>> print_n_times(3, '안녕하세요즐거운 파이', 3,4,3,2)
안녕하세요즐거운 파이

3

4

3

2

안녕하세요즐거운 파이

3

4

3

2

안녕하세요즐거운 파이

3

4

3

2

>>> def pinrt_n_times(value, n):
	for i in range(n):
		print(value)

		
>>> print_n_times('안녕', 5)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    print_n_times('안녕', 5)
  File "<pyshell#21>", line 3, in print_n_times
    for i in range(n):
TypeError: 'str' object cannot be interpreted as an integer
>>> def pinrt_n_times(value, n):
	for i in range(n):
	    print(value)

	    
>>> print_n_times('안녕', 5)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    print_n_times('안녕', 5)
  File "<pyshell#21>", line 3, in print_n_times
    for i in range(n):
TypeError: 'str' object cannot be interpreted as an integer
>>> def print_n_times(value, n):
	for i in range(n):
	    print(value)

	    
>>> print_n_times('안녕', 5)
안녕
안녕
안녕
안녕
안녕
>>> 
>>> 
>>> ##기본 매개변수
>>> def print_n_times(value, n=2):
	#n번 반복합니다.
	for i in range(n):
		print(value)

		
>>> #함수를 호출 합니다.
>>> print_n_times('안녕')
안녕
안녕
>>> def print_n_times(value, n=2):
	#n번 반복합니다.
	for i in range(n):
		print(value)