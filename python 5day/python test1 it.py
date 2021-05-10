class It(object):

    def __init__(self, company, employee, name, age):
        self.company = company
        self.employee = employee
        self.name = name
        self.age = age

    def __str__(self):
        return '{}는 {}명 근무 {}이름 {}나이'.format(self.company, self.employee, self.name, self.age)

    def disp_It(self):
        print('{}는 {}명 근무 {}이름 {}나이'.format(self.company, self.employee, self.name, self.age)) 

    def get_company(self):
        return self.company
    
    def get_employee(self):
        return self.employee

    def set_company(self, company):
        self.company = company

    def set_employee(self, employee): 
        self.employee = employee

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def set_name(self, name):
        self.name = name
    
    def set_age(self, age):
        self.age = age


it1 = It('google', 56000, '김만덕', 28)
it2 = It('facebook', 46000, '이순신', 25)

print(it1)
print(it2)

it1.disp_It()
it2.disp_It()