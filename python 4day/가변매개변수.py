##가변인수(개수가 달라질 수 있다.)

def 함수2(인수1, 인수2):
    print(인수1, 인수2)

함수2('korea', 'korea')


def add1(x):
    print(x+x)


def add3(x, y, z= 100):
    print(x+y+z)


add3(30,20)


def add4(x,y, *z):


    print(x+y+sum(z))
    



add4(1,2,3,123,12,323)

'''
def value_times(*values, times=2): 
	#for value in values: 
		print(value * times) 

value_times(3, 1, 2, 3, 4, 5)
'''

'''
def add5(x=100, y=200, z=300):

    #나는 doc stirng

    print('x =', x, 'y=',y ,'z=',z)

add5(
'''

