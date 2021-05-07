Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #for 문
>>> 
>>> for i in 3, 4, 7
SyntaxError: invalid syntax
>>> for i in 3, 4, 7:
	print(i, end = '\n')
	print(i*i, end = '\n')

	
3
9
4
16
7
49
>>> for i in 'korea', 'japan', 'china':
	print(i, end = '\t')
	print(i*i, end = '\t')

	
korea	Traceback (most recent call last):
  File "<pyshell#8>", line 3, in <module>
    print(i*i, end = '\t')
TypeError: can't multiply sequence by non-int of type 'str'
>>> for i in 'korea', 'japan', 'china':
	print(i, end = '\t')
	print(i+i, end = '\t')

	
korea	koreakorea	japan	japanjapan	china	chinachina	
>>> for i in range(10)
SyntaxError: invalid syntax
>>> print(i, end = '\t')
china	
>>> for i in range(10):
	print(i, end = '\t')

	
0	1	2	3	4	5	6	7	8	9	
>>> for i in range(10):
	print(i, end = ' ')

	
0 1 2 3 4 5 6 7 8 9 
>>> for i in range(0, 10):
	print(i, end = ' ')

	
0 1 2 3 4 5 6 7 8 9 
>>> for i in range(0, 10, 2):
	print(i, end = ' ')

	
0 2 4 6 8 
>>> 