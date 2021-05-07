Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = [3, 6, 9,]
>>> type(a)
<class 'list'>
>>> a[0]
3
>>> a[1]
6
>>> a[2]
9
>>> a[3]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a[3]
IndexError: list index out of range
>>> len(a)#list a의 길이
3
>>> b = [6, 8, 9]
>>> a
[3, 6, 9]
>>> b
[6, 8, 9]
>>> a + b
[3, 6, 9, 6, 8, 9]
>>> ab = a+ b
>>> ab
[3, 6, 9, 6, 8, 9]
>>> a
[3, 6, 9]
>>> b
[6, 8, 9]
>>> b
[6, 8, 9]
>>> a.extend(b)
>>> a
[3, 6, 9, 6, 8, 9]
>>> #extend는 배열을 합치는 것
>>> len(a)
6
>>> a[5]
9
>>> a[5] = 99
>>> a
[3, 6, 9, 6, 8, 99]
>>> a[6]
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a[6]
IndexError: list index out of range
>>> #a 5번째 배열을 바꿀 수 있다.
>>> a[6] = 77
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    a[6] = 77
IndexError: list assignment index out of range
>>> a.append(77)
>>> a.append(44)
>>> a
[3, 6, 9, 6, 8, 99, 77, 44]
>>> #append는 배열 맨 뒤에 추가하는 것
>>> len(8)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    len(8)
TypeError: object of type 'int' has no len()
>>> len(a)
8
>>> a.append(66,33)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    a.append(66,33)
TypeError: list.append() takes exactly one argument (2 given)
>>> #append 한번에 두개 추가 안된다.
>>> 
>>> a.append([66, 33])
>>> a
[3, 6, 9, 6, 8, 99, 77, 44, [66, 33]]
>>> a.extend([22, 88])
>>> a
[3, 6, 9, 6, 8, 99, 77, 44, [66, 33], 22, 88]
>>> 
>>> #배열 중간에 값 넣기 insert
>>> a.insert(2, 80) #두번째 자리에 80을 넣어라
>>> ㅁ
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    ㅁ
NameError: name 'ᄆ' is not defined
>>> a.insert(4, 80) #네번째 자리에 80을 넣어라
>>> a
[3, 6, 80, 9, 80, 6, 8, 99, 77, 44, [66, 33], 22, 88]
>>> a.insert(0, 555) #첫번째 자리에 80을 넣어라
>>> a
[555, 3, 6, 80, 9, 80, 6, 8, 99, 77, 44, [66, 33], 22, 88]
>>> 
>>> #꺼낸 는 것 pop
>>> 
>>> a.pop()
88
>>> a
[555, 3, 6, 80, 9, 80, 6, 8, 99, 77, 44, [66, 33], 22]
>>> a.pop()
22
>>> a.pop()
[66, 33]
>>> #a.pop은 맨 뒤에게 꺼내져 나온다.
>>> 
>>> 
>>> 
>>> a.index(3)
1
>>> #index 배열 안에 숫자의 위치를 알려준다.
>>> a.index(2222)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    a.index(2222)
ValueError: 2222 is not in list
>>> a.pop()
44
>>> a
[555, 3, 6, 80, 9, 80, 6, 8, 99, 77]
>>> print(a)
[555, 3, 6, 80, 9, 80, 6, 8, 99, 77]
>>> a = [1, [1,2], [1,2,3]]
>>> a
[1, [1, 2], [1, 2, 3]]
>>> a[2].pop()
3
>>> a
[1, [1, 2], [1, 2]]
>>> a[2,1]popo()
SyntaxError: invalid syntax
>>> a[2,1].pop()
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    a[2,1].pop()
TypeError: list indices must be integers or slices, not tuple
>>> a[2 0].pop()
SyntaxError: invalid syntax
>>> a[2].pop()
2
>>> a
[1, [1, 2], [1]]
>>> a = [1, [1,2], [1,2,3]]
>>> a[1][0].pop()
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    a[1][0].pop()
AttributeError: 'int' object has no attribute 'pop'
>>> a[1][0]
1
>>> type(a[1][0])
<class 'int'>
>>> type(a[1])
<class 'list'>
>>> a[1].remove(a[1][0])
>>> a
[1, [2], [1, 2, 3]]
>>> a = [1, [1,2], [1,2,3]]
>>> a[1].remove(1)
>>> a
[1, [2], [1, 2, 3]]
>>> a
[1, [2], [1, 2, 3]]
>>> a = [1, [1,2], [1,2,3]]
>>> a
[1, [1, 2], [1, 2, 3]]
>>> t = a.pop([2][1])
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    t = a.pop([2][1])
IndexError: list index out of range
>>> t = a[2][1].pop()
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    t = a[2][1].pop()
AttributeError: 'int' object has no attribute 'pop'
>>> a
[1, [1, 2], [1, 2, 3]]
>>> t = a[2][1]
>>> t
2
>>> a = [4, 6, 5.6, 7.5, 'ace', 'korea']
>>> type(a)
<class 'list'>
>>> len(a)
6
>>> a.sort()
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    a.sort()
TypeError: '<' not supported between instances of 'str' and 'int'
>>> b = ['서울', '부산', '대구']
>>> b.sort()
>>> #같은 문자열 끼리는 sort됨
>>> 
>>> b
['대구', '부산', '서울']
>>> a.bb()
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    a.bb()
AttributeError: 'list' object has no attribute 'bb'
>>> a==b
False
>>> a.__eq__(b)
False
>>> 
>>> ##==rhk __eq__같은 의미
>>> output = "{:=+05d}".format(52)
>>> print(output)
+0052
>>> output = "{:=+5d}".format(52)
>>> print(output)
+  52
>>> output = "{:>=+5d}".format(52)
>>> 
>>> print(output)
+>>52
>>> output = "{:>+5d}".format(52)
>>> 
>>> print(output)
  +52
>>> t = (30, 50, 70)
>>> lent(t)
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    lent(t)
NameError: name 'lent' is not defined
>>> len(t)
3
>>> t[0]
30
>>> t[1]
50
>>> t[1], t[2]4
SyntaxError: invalid syntax
>>> t[1], t[2]
(50, 70)
>>> t. index(30)
0
>>> t.index(0)
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    t.index(0)
ValueError: tuple.index(x): x not in tuple
>>> t.index(50)
1
>>> t.index(70)
2
>>> t.count(30)
1
>>> t.count(1)
0
>>> t[1] = 400
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    t[1] = 400
TypeError: 'tuple' object does not support item assignment
>>> type(t)
<class 'tuple'>
>>> list(t)##형을 바꿔라는 의미
[30, 50, 70]
>>> type(t)
<class 'tuple'>
>>> t = list(t)
>>> type(t)
<class 'list'>
>>> t
[30, 50, 70]
>>> 
>>> 
>>> ### 튜플의 형을 list로 바꾼다.
>>> 
>>> t
[30, 50, 70]
>>> t = tuple(t)
>>> type(t)
<class 'tuple'>
>>> t = list(t)
>>> type(t)
<class 'list'>
>>> t
[30, 50, 70]
>>> t[1] = 500
>>> t
[30, 500, 70]
>>> t = tuple(t)
>>> t
(30, 500, 70)
>>> t[1] = 50
Traceback (most recent call last):
  File "<pyshell#149>", line 1, in <module>
    t[1] = 50
TypeError: 'tuple' object does not support item assignment
>>> 
>>> 
>>> 
>>> ## data 맞교환
>>> 
>>> i, j = j,i
Traceback (most recent call last):
  File "<pyshell#157>", line 1, in <module>
    i, j = j,i
NameError: name 'j' is not defined
>>> #i의 값과 j 의 값이 있을 때 바뀜
>>> 
>>> 
>>> 
>>> ㅋ = 10, 20 ,30
>>> ㅋ
(10, 20, 30)
>>> z = 10, 20, 30
>>> z
(10, 20, 30)
>>> type(z)
<class 'tuple'>
>>> z1, z2, z3 = z
>>> 
>>> #z부분 패킹
>>> 
>>> #z1, z2, z3를 언패킹
>>> 
>>> 약
Traceback (most recent call last):
  File "<pyshell#173>", line 1, in <module>
    약
NameError: name '약' is not defined
>>> dir
<built-in function dir>
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'ab', 'b', 'output', 't', 'z', 'z1', 'z2', 'z3', 'ᄏ']
>>> 
>>> 
>>> 
>>> # set
>>> 
>>> a = {1, 2, 3, 4,5}
>>> b = {2, 4, 6}
>>> 
>>> type(a)
<class 'set'>
>>> type(b)
<class 'set'>
>>> a
{1, 2, 3, 4, 5}
b
>>> 
>>> b
{2, 4, 6}
>>> 
>>> #합집합
>>> a|b
{1, 2, 3, 4, 5, 6}
>>> 
>>> #교집합
>>> a &b
{2, 4}
>>> a - b
{1, 3, 5}
>>> b- a
{6}
>>> 
>>> 
>>> #합집합
>>> a.union(b)
{1, 2, 3, 4, 5, 6}
>>> 
>>> #교집합 &
>>> 
>>> a.intersection(b)
{2, 4}
>>> 
>>> # 차집합-
>>> 
>>> a-b
{1, 3, 5}
>>> 
>>> len(a)
5
>>> len(b)
3
>>> 
>>> a[0]
Traceback (most recent call last):
  File "<pyshell#213>", line 1, in <module>
    a[0]
TypeError: 'set' object is not subscriptable
>>> 
>>> k = []
>>> k.append(2)
>>> k
[2]
>>> k.add(2)
Traceback (most recent call last):
  File "<pyshell#218>", line 1, in <module>
    k.add(2)
AttributeError: 'list' object has no attribute 'add'
>>> 
>>> 
>>> 
>>> #dictionary 사전형
>>> 
>>> d = {'이름': '강호동', '나이' : 51, '직업': 'mc'}
>>> 
>>> # 앞에것이 키 뒤에것이 value
>>> d[0]
Traceback (most recent call last):
  File "<pyshell#227>", line 1, in <module>
    d[0]
KeyError: 0
>>> d['이름']
'강호동'
>>> d['나이']
51
>>> d['직업']
'mc'
>>> d.keys()
dict_keys(['이름', '나이', '직업'])
>>> d.value()
Traceback (most recent call last):
  File "<pyshell#232>", line 1, in <module>
    d.value()
AttributeError: 'dict' object has no attribute 'value'
>>> d.values()
dict_values(['강호동', 51, 'mc'])
>>> d.items()
dict_items([('이름', '강호동'), ('나이', 51), ('직업', 'mc')])
>>> 
>>> # .values()는 value 값만 items()는 전체값
>>> 
>>> 
>>> for key, value in d.items():
	pring(key, values)

	
Traceback (most recent call last):
  File "<pyshell#241>", line 2, in <module>
    pring(key, values)
NameError: name 'pring' is not defined
>>> for key, value in d.items():
	print(key, values)

	
Traceback (most recent call last):
  File "<pyshell#243>", line 2, in <module>
    print(key, values)
NameError: name 'values' is not defined
>>> for key, value in d.items():
	print(key, value)

	
이름 강호동
나이 51
직업 mc
>>> for i, j in d.items():
	print(i, '===>', value)

	
이름 ===> mc
나이 ===> mc
직업 ===> mc
>>> for i, j in d.items():
	print(i, '===>' value)
	
SyntaxError: invalid syntax
>>> for i, j in d.items():
	print(i, '===>', value)

	
이름 ===> mc
나이 ===> mc
직업 ===> mc
>>> for i, j in d.items():
	print(i, '===>', j)

	
이름 ===> 강호동
나이 ===> 51
직업 ===> mc
>>> for i, j in d.items():
	print(key, '===>', values)

	
Traceback (most recent call last):
  File "<pyshell#254>", line 2, in <module>
    print(key, '===>', values)
NameError: name 'values' is not defined
>>> for i, j in d.items():
	print(key, '===>', value)

	
직업 ===> mc
직업 ===> mc
직업 ===> mc
>>> for i, j in d.items():
	print(i, '===>', j)

	
이름 ===> 강호동
나이 ===> 51
직업 ===> mc
>>> d.update({'수입' : 30})
>>> ㅇ
Traceback (most recent call last):
  File "<pyshell#260>", line 1, in <module>
    ㅇ
NameError: name 'ᄋ' is not defined
>>> d
{'이름': '강호동', '나이': 51, '직업': 'mc', '수입': 30}
>>> #d안에 수입 추가
>>> d.get('나이')
51
>>> d.pop()
Traceback (most recent call last):
  File "<pyshell#264>", line 1, in <module>
    d.pop()
TypeError: pop expected at least 1 argument, got 0
>>> d.popitem()
('수입', 30)
>>> 
>>> 
>>> a
{1, 2, 3, 4, 5}
>>> 2 in a
True
>>> 2 not in a
False
>>> aaa = a
>>> a is aaa
True
>>> id(aaa)
2209276070144
>>> a is not aaa
False
>>> ac = a.copy()
>>> id (ac)
2209276205536
>>> a is ac
False
>>> # is 는 id의 값을 비교하는 것이다. in은 안에 있는 값을 비교하는 것
>>> 
>>> true | false
Traceback (most recent call last):
  File "<pyshell#280>", line 1, in <module>
    true | false
NameError: name 'true' is not defined
>>> 1 and 2
2
>>> 1 or 2
1
>>> 