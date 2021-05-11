## gg = 500 -> 전역변수라고 한다.

CUR_YEAR =2021 #전역변수

class date(object):
    def __init__(self, year, month): #self와 d1이 같은 것 year에 2021 month에 2000 들어간다.
        self.year = year #x로 해도 가능
        self.month = month #y도 가능
       # self.age = self.date.Call_age(year)
        print('date __init__')

    

    #쓰레기 수집한다.
    #def gc leak
    # 이거 안해줘도 된다. def __del__(self) 
    def disp_date(self):
        print('{}년 {}월'.format(self.year, self.month ))

    def __del__(self):
        print('date __del__')

# d1 = date(2021,10)
# d2 = date(2000,12)



class Man(date): #date class를 상속 받는다.
    
    #object를 상속 받겠다. 여기서 oject는 생략 가능하다 ()도 생략 가능하다.
    cnt = 0 ## 전역변수 클래스 변수 class  변수

    def __init__(self, name, year, month): # 생성자이다 객체 생성시 자동호출 된다.(constructor)되는 함수, 생성자
        
        super().__init__(year,month)#date의 init을 가져온다. date 한테로 넘겨준다.

        self.name= name
        #self.age = age

        Man.cnt += 1 #클래스 이름을 직접적으로 써준다.
        self.age = CUR_YEAR - year +1
        print('Man __init__')

    def __del__(self): # 객체 소멸시 자동 호출(destructor) 되는 함수, 소멸자
        Man.cnt -= 1
        super().__del__()
        print('Man __del__')

    
    def __str__(self): #객체 출력시 자동으로 호출되는 함수, 기본 값은 객체의 id값 리턴
        return '{} 님은 {}살'.format(self.name, self.age)
        #date.disp_date(self) ## date class의 메서드 호출 부모클래스 메소드 호출
        #super().date.disp_date(self)
    
    def disp_Man(self):
        print('{}님은 {}살'.format(self.name, self.age))
        super().disp_date()

        
    def Call_age(self, year):
        return CUR_YEAR - year +1

    # def get_name(self):
    #     return self.name 
    
    # def get_age(self):
    #     return self.age
    
    # def set_name(self, name):
    #     self.name = name

    # def set_age(self, age):
    #     self.age = age

    def __eq__(self, other): #메소드 재정의(override 덮어쓴다.), 메소드 중복, 메소드 오버라이드,비교 재정의
        if self.name == other.name and self.age == other.age:
            return True
        else:
            return Flase
    def __add__(self, num):#메소드 재정의, 메소드 중복, 메소드 오버라이드,비교 재정의
        self.age = self.age + num
    
    def __sub__(self, num):#메소드 재정의, 메소드 중복, 메소드 오버라이드,비교 재정의
        self.age = self.age - num
    
    @staticmethod #@ 가 붙은 것을 장식자(데코레이터)라고 한다.
    #static 은 dynamic에 반대 고정되어 있는 메소드
    def get_cnt1():
        return Man.cnt
    
    @classmethod #클래스 메소드는 클래스에 전체 포함되어 있는 메소드
    def get_cnt2(cls):
        return Man.cnt
    ##스태틱 메소드와 클래스 메소드 구별 안하는게 좋다.


    


    #전체적으로 수를 셀때 사용 할 수 있다.

    # _---------> 여기까지 클래스선언한것


    #메서드 중복(method overload)

    # def A1(self, x):
    #     return x+x
    
    # def A1(self, x, y):
    #     return x+y

# print('현재 객체 생성 수는 : {}'.format(Man.cnt))
# print('현재 객체 생성 수는 : {}'.format(Man.get_cnt1()))

m1 = Man('손흥민', 1991, 7)

m2 = Man('이강인', 2001, 1)
m3 = Man('손흥민', 1991, 7)

# print('현재 객체 생성 수는 : {}'.format(Man.cnt))
# print('현재 객체 생성 수는 : {}'.format(m1.get_cnt2()))



# print(m1)
# print(m2)
# #print(m1.__str__())
# #print(m2.__str__())

# print(m1 == m3)

# print(int(id(m1) == id(m3)))

# m1 +2
# m2 -2
# #print(m1 +2) #에러가 남 앞에 객체이름은 man 이고 뒤에 2는 int 이기 때무에 타입 에러가 난다.

# m1.disp_Man()
# m2.disp_Man()

# print(dir(m1))


# print(m1.A1(20,30))

m1.disp_Man()
