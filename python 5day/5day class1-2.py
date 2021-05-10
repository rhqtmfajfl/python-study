class korea: #클래스 선언
    def __init__(self, city, pop): #생성자함수
        self.city = city #멤버변수
        self.pop = pop #멤버변수
        print('korea __init__ : 생성자')
        
    def __del__(self): #함수 소멸자 함수
        print('korea __dal__ : 소멸자')

    def __str__(self):
        return '{}인구는 ==> {}만명 '.format(self.city, self.pop)    
    
    def disp_korea(self): #함수
        print(self.city, '인구는', self.pop, '만원', id(self))
        #위의 과정은 class 선언이다.

    def get_city(self):
       return self.city

    def get_pop(self):
       return self.pop

    def set_city(self, city):
        self.city = city
    
    def set_pop(self, pop):
        self.pop = pop

print('###############')

# def ff(): 
#     print('나는 ff함수다.00') #함수 선언


k1 = korea('서울시', 950) #korea 객체생성
k2 = korea('부산시', 700)
#k2.pop = 360
k1.disp_korea()
k2.disp_korea()

k1.city = '수원'
k1.pop = 110
print(k1.get_city(), k1.get_pop())
print(k2.get_city(), k2.get_pop())
