class It(object):
    
    def __init__(self, company, employee):
        self.company = company
        self.employee = employee

    
    def __str__(self):
        return '{}는 {}명 근무'.format(self.company, self.employee)

    def disp_It(self):
        print('{}는 {}명 근무'.format(self.company, self.employee))

    def get_company(self):
        return self.company
    
    def get_employee(self):
        return self.employee

    def set_company(self, company):
        self.company = company

    def set_employee(self, employee): 
        self.employee = employee

    def __add__(self, num): #연산자 중복 재정의
        self.employee = self.employee + num

    def __sub__(self, num):
        self.employee = self.employee - num
    
    def __eq__(self, other):
        if self.company == other.company and self.employee == other.employee:
            return True
        else:
            return False

it1 = It('google', 56000)
it2 = It('facebook', 46000)
print(it1)
print(it2)  

it1.disp_It()
it2.disp_It()

print(it1.get_company(), '의 직원은', it1.get_employee(), '명')

it1.set_company('삼성전자')
it1.set_employee(96000)

print(it1.get_company(), '의 직원은', it1.get_employee(), '명')

it1 + 100

it1.disp_It()

it1 - 1500

it1.disp_It()
it33 = it2

it2.disp_It()
it33.disp_It()

print('==', it2 == it33)