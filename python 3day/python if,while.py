Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import datetime

now = datetime.datetime.now()

if now.hour < 12:
    print("현재 시각은 {}시로 오전입니다.!".format(now.hour))

if now.hour>12:
    print("현재 시각은 {}시로 오후입니다.!"format(now.hour))
    
SyntaxError: multiple statements found while compiling a single statement
>>> import datetime

    now = datetime.datetime.now()

if now.hour < 12:
    print("현재 시각은 {}시로 오전입니다.!".format(now.hour))

if now.hour>12:
    print("현재 시각은 {}시로 오후입니다.!"format(now.hour))
    
SyntaxError: multiple statements found while compiling a single statement
>>> import date time
SyntaxError: invalid syntax
>>> import datetime
>>> now = datetime.datetime.now()

if now.hour < 12:
    print("현재 시각은 {}시로 오전입니다.!".format(now.hour))

if now.hour>12:
    print("현재 시각은 {}시로 오후입니다.!"format(now.hour))
    
SyntaxError: multiple statements found while compiling a single statement
>>> if now.hour < 12:
    print("현재 시각은 {}시로 오전입니다.!".format(now.hour))

if now.hour>12:
    print("현재 시각은 {}시로 오후입니다.!"format(now.hour))
    
SyntaxError: invalid syntax
>>> if now.hour < 12:
    print("현재 시각은 {}시로 오전입니다.!".format(now.hour))

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    if now.hour < 12:
NameError: name 'now' is not defined
>>> if now.hour < 12:
    print("{}년 {}월 {}일 {}시 {}분 {}초".format(
    now.year
    now.month
    now.day
    now.hour,
    now.minute,
    now.second
    ))
    
SyntaxError: invalid syntax
>>> if now.hour < 12:
    print("{}년 {}월 {}일 {}시 {}분 {}초".format(
    now.year,
    now.month,
    now.day,
    now.hour,
    now.minute,
    now.second
    ))

    
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    if now.hour < 12:
NameError: name 'now' is not defined
>>> now = datetime.datetime.now()
>>> print("{}년 {}월 {}일 {}시 {}분 {}초".format(
    now.year,
    now.month,
    now.day,
    now.hour,
    now.minute,
    now.second
    ))
2021년 5월 6일 9시 11분 10초
>>> if now.hour < 12:
    print("현재 시각은 {}시로 오전입니다.!".format(now.hour))

if now.hour>12:
    print("현재 시각은 {}시로 오후입니다.!"format(now.hour))
    
SyntaxError: invalid syntax
>>> if now.hour < 12:
    print("현재 시각은 {}시로 오전입니다.!".format(now.hour))

    
현재 시각은 9시로 오전입니다.!
>>> if now.hour>12:
    print("현재 시각은 {}시로 오후입니다.!"format(now.hour))
    
SyntaxError: invalid syntax
>>> if now.hour>12:
    print("현재 시각은 {}시로 오후입니다.!".format(now.hour))

    
>>> if now.hour < 12:
    print("현재 시각은 {}시로 오전입니다.!".format(now.hour))

if now.hour>12:
    print("현재 시각은 {}시로 오후입니다.!".format(now.hour))
    
SyntaxError: invalid syntax
>>> if now.hour < 12:
    print("현재 시각은 {}시로 오전입니다.!".format(now.hour))

else now.hour>12:
    print("현재 시각은 {}시로 오후입니다.!".format(now.hour))
    
SyntaxError: invalid syntax
>>> if now.hour < 12:
    print("현재 시각은 {}시로 오전입니다.!".format(now.hour))

else now.hour >12:
    print("현재 시각은 {}시로 오후입니다.!".format(now.hour))
    
SyntaxError: invalid syntax
>>> if now.hour < 12:
    print("현재 시각은 {}시로 오전입니다.!".format(now.hour))

else now.hour >12
    print("현재 시각은 {}시로 오후입니다.!".format(now.hour))
    
SyntaxError: invalid syntax
>>> if now.hour < 12:
    print("현재 시각은 {}시로 오전입니다.!".format(now.hour))

else now.hour >12:
    print("현재 시각은 {}시로 오후입니다.!".format(now.hour))
    
SyntaxError: invalid syntax
>>> if now.hour < 12:
    print("현재 시각은 {}시로 오전입니다.!".format(now.hour))

else :
    print("현재 시각은 {}시로 오후입니다.!".format(now.hour))

    
현재 시각은 9시로 오전입니다.!
>>> print("{}년 {}월 {}일 {}시 {}분 {}초".format(
    now.year,
    now.month,
    now.day,
    now.hour,
    now.minute,
    now.second
    ))
2021년 5월 6일 9시 11분 10초
>>> now = datetime.datetime.now()
>>> print("{}년 {}월 {}일 {}시 {}분 {}초".format(
    now.year,
    now.month,
    now.day,
    now.hour,
    now.minute,
    now.second
    ))
2021년 5월 6일 9시 26분 24초
>>> print("{}년 {}월 {}일 {}시 {}분 {}초".format(
    now.year,
    now.month,
    now.day,
    now.hour,
    now.minute,
    now.second
    ))
2021년 5월 6일 9시 26분 24초
>>> if 3 <= now.month <= 5:
	print("이번 달은 {}월로 봄입니다.!".format(now.month))
	else if 6<=now.month <=8:
		
SyntaxError: invalid syntax
>>> if 3 <= now.month <= 5:
	print("이번 달은 {}월로 봄입니다.!".format(now.month))
    else if 6<=now.month <=8:
	    
SyntaxError: unindent does not match any outer indentation level
>>> if 3 <= now.month <= 5:
	print("이번 달은 {}월로 봄입니다.!".format(now.month))
    elif 6<=now.month <=8:
	    
SyntaxError: unindent does not match any outer indentation level
>>> now = datetime.datetime.now()
>>> if 3 <= now.month <= 5:
	print("이번 달은 {}월로 봄입니다.!".format(now.month))
    elif 6<=now.month <=8:
	    
SyntaxError: unindent does not match any outer indentation level
>>> if 3 <= now.month <= 5:
	print("이번 달은 {}월로 봄입니다.!".format(now.month))

	
이번 달은 5월로 봄입니다.!
>>> if 3 <= now.month <= 5:
	print("이번 달은 {}월로 봄입니다.!".format(now.month))
    elif
    
SyntaxError: unindent does not match any outer indentation level
>>> output = " {:<5} ".format(52)
>>> print(output)
 52    
>>> output = " {:<5} ".format(52, 42)
>>> print(output)
 52    
>>> output = " {:>5} ".format(52, 42)
>>> 
>>> print(output)
    52 
>>> output = " {:>5d} ".format(52, 42)
>>> print(output)
    52 
>>> output = " {1:>5d} ".format(52, 42)
>>> print(output)
    42 
>>> t.count(30)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    t.count(30)
NameError: name 't' is not defined
>>> t.count(30)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    t.count(30)
NameError: name 't' is not defined
>>> output = "{:+d} ".format(-52)
>>> output
'-52 '
>>> print(output)
-52 
>>> for a in range(2,4)
SyntaxError: invalid syntax
>>> for a in range(2,4):
	for b in range(1,10):
		ptint('{0} * {1} = {2:2}'.format(a, b, a*b))

		
Traceback (most recent call last):
  File "<pyshell#74>", line 3, in <module>
    ptint('{0} * {1} = {2:2}'.format(a, b, a*b))
NameError: name 'ptint' is not defined
>>> for a in range(2,4):
	for b in range(1,10):
		ptint('{0} x {1} = {2:2}'.format(a, b, a*b))

		
Traceback (most recent call last):
  File "<pyshell#76>", line 3, in <module>
    ptint('{0} x {1} = {2:2}'.format(a, b, a*b))
NameError: name 'ptint' is not defined
>>> for a in range(2,4):
	for b in range(1,10):
		print('{0} x {1} = {2:2}'.format(a, b, a*b))

		
2 x 1 =  2
2 x 2 =  4
2 x 3 =  6
2 x 4 =  8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
3 x 1 =  3
3 x 2 =  6
3 x 3 =  9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
>>> 