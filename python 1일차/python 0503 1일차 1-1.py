Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = [5,6,2,3,8]
>>> a
[5, 6, 2, 3, 8]
>>> a = [5, 6, 2, 3, 8]
>>> type(a)
<class 'list'>
>>> a
[5, 6, 2, 3, 8]
>>> sum(a)
24
>>> a
[5, 6, 2, 3, 8]
>>> min(a)
2
>>> max(a)
8
>>> a.sort()
>>> a
[2, 3, 5, 6, 8]
>>> a.sort()
>>> a
[2, 3, 5, 6, 8]
>>> b = ['seoul', 'busan', 'incheon', 'dokodo']
>>> b
['seoul', 'busan', 'incheon', 'dokodo']
>>> b.sort()
>>> b
['busan', 'dokodo', 'incheon', 'seoul']
>>> b
['busan', 'dokodo', 'incheon', 'seoul']
>>> bb
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    bb
NameError: name 'bb' is not defined
>>> b
['busan', 'dokodo', 'incheon', 'seoul']
>>> min(b)
'busan'
>>> sum(b)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    sum(b)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> max(b)
'seoul'
>>> 