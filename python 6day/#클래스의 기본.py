#클래스의 기본

#딕셔너리로 객체 만들기

#학생 리스트를 선언
'''
students = [ {'name' : '윤인성', 'korean':87, 'math': 98, 'english': 88,  'science' : 95},
{'name' : '연하진', 'korean':92, 'math': 98, 'english': 96,  'science' : 98},
{'name' : '구지연', 'korean': 76, 'math': 96, 'english': 94,  'science' : 90},
{'name' : '나선주', 'korean':98, 'math': 63, 'english': 94,  'science' : 92},
{'name' : '윤아린', 'korean':95, 'math': 95, 'english': 98,  'science' : 98},
{'name' : '윤명월', 'korean':98, 'math': 88, 'english': 92,  'science' : 92}]

#학생이름을 한 명씩 반보

print('이름', '총점','평균', sep='\t')

for student in students:
    #점수의 총합과 평균을 구합니다.
    score_sum = student['korean'] + student['math'] + \
        student['english'] + student['science']
    score_average = score_sum / 4
    #출력합니다.
    print(student['name'], score_sum, score_average, sep='\t')

'''


#객체를 만드는 함수

#딕셔너리를 리턴하는 함수를 선언합니다.

'''

def create_student(name, korean, math, english, science):

    return {'name':name, 'korean':korean, 'math':math, 'english':english, 'science': science}

#학생 리시트를 선언함
students = [create_student('윤인성', 87,98,88,95),
create_student('연하진', 92,98,96,98),
create_student('구지연', 76,96,94,90),
create_student('나선주', 98,92,96,92),
create_student('윤아린', 95,98,98,98),
create_student('윤명월',98,88,92,92)
]

#학생을 한 명씩 반복합니다.

print('이름', '총점', '평균', sep='\t')
for student in students:
    #점수의 총합과 평균을 구함
    score_sum = student['korean'] + student['math'] + \
        student['english'] + student['science']
    score_average = score_sum/ 4

#출력함
    print(student['name'], score_sum, score_average, sep= '\t')

'''


#객체를 처리하는 함수(2)

# def create_student(name, korean, math, english, science):
#     return { 'name' : name, 'korean' : korean, 'math':math, 'english': english, 'science': science}
# '''
# def create_student(name, korean, math, english, science):
#     return { 'name':name, 'korean', korean, 'math' : math, 'english': english, 'science': science}
# '''
# #학생을 처리하는 함수를 선언한다.

# def student_get_sum(student):
#     return student['korean'] + student['math'] +\
#          student['english'] + student['science']
# '''
# def student_get_sum(student):
#     return student['korean'] + student[1q   
#     ]
# '''
# def student_get_average(student):
#     return student_get_sum(student) / 4

# def student_to_string(student):
#     return '{} \t {} \t{}'.format(student['name'], student_get_sum(student), student_get_average(student))
# # def studnet_to_string(student):
#     return'{} {} {}'.format(student['name'],)



# #학생리스트를 선언한다.

# students = [create_student('윤인성', 87,98,88,95),
# create_student('연하진', 92,98,96,98),
# create_student('구지연', 76,96,94,90),
# create_student('나선주', 98,92,96,92),
# create_student('윤아린', 95,98,98,98),
# create_student('윤명월',98,88,92,92)
# ]

# #학생을 한 명씩 반복
# print('이름', '총점', '평균', sep ='\t')
# for student in students:
#     #출력
#     print(student_to_string(student))




#생성자


#클래스를 선언한다.

'''

class student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

#학생 리스트를 선언
students = [student('윤인성', 87,98,88,95),
student('연하진', 92,98,96,98),
student('구지연', 76,96,94,90),
student('나선주', 98,92,96,92),
student('윤아린', 95,98,98,98),
student('윤명월', 64,88,92,92)
]

#student 인사턴스의 속성에 접근하는 방법

print(students[0].name)
print(students[0].korean)
print(students[0].math)
print(students[0].english)
print(students[0].science)
'''


#생성자와 소멸자

"""
class test:
    def __init__(self, name):
        self.name = name
        print("{} - 생성되었습니다.".format(self.name))
    def __del__(self):
        print('{} - 파괴되었습니다.'.format(self.name))

test= test('A')       

"""

#메소드

#클래스 내부에 함수(메소드) 선언하기


'''
class student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math +\
            self.english + self.science

    def get_average(self):
        return self.get_sum() /4

    def to_string(self):
        return '{} \t {}\t {}'.format(\
            self.name, self.get_sum(),self.get_average())



students = [student('윤인성', 87,98,88,95),
student('연하진', 92,98,96,98),
student('구지연', 76,96,94,90),
student('나선주', 98,92,96,92),
student('윤아린', 95,98,98,98),
student('윤명월', 64,88,92,92)
]

print('이름', '총점', '평균', sep ='\t')
for student in students:
    #출력
    print(student.to_string())

'''



#클래스의 추가적인 구문

#어떤 클래스의 인스턴스인지 확인하기

#클래스 선언
'''
class Student:
    def __init__(self):
        pass
#학생을 선언
student =Student()

#인스턴스 확인

print('instance(ststuden, student): ', isinstance(student,Student))

'''



# isinstance()함수와 type()함수로 확인하는 것의 차이
#클래스 선언

'''
class HUMAN:
    def __init__(self):
        pass
class STUDENT(HUMAN):
    def __init__(self):
        pass

#학생을 선언합니다.
student = STUDENT()

#인스턴스 확인
print('isinstance(student, HUMAN : ',isinstance(student, HUMAN))
print('type(student) == HUMAN',type(student)==HUMAN)

'''



#isinstance
#학생클래스를 선언
'''
class Student:
    def study(self):
        print('공부하십다.')

#선생님 클스를 선언
class teacher:
    def teach(self):
        print('학생 가르친다.')

#교실 내부의 객체리스트를 생성

classroom = [Student(), Student(), teacher(), Student(), Student()]


#반복을 적용해서 적절한 함수를 호출하게 합니다.
for person in classroom:
    if isinstance(person, Student):
        person.study()
    elif isinstance(person, teacher):
        person.teach()
'''


#__str__() 함수


'''
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math +\
            self.english + self.science
    def get_average(self):
        return self.get_sum() / 4

    def __str__(self):
        return '{} \t {} \t {} '. format(
            self.name,
            self.get_sum(),
            self.get_average()
        )

#학생리스트를 선언합ㄴ디ㅏ.

students = [Student('윤인성', 87,98,88,95),
Student('연하진', 92,98,96,98),
Student('구지연', 76,96,94,90),
Student('나선주', 98,92,96,92),
Student('윤아린', 95,98,98,98),
Student('윤명월', 64,88,92,92)
]

#출력
print('이름', '총점', '평균', sep ='\t')
for student in students:
    print(str(student))

'''

#크기 비교함수

#클래스 선언

'''
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_average(self):
        return get_sum() / 4

    def __str__(self):
        return '{} \t {} \t {}'.format(self.name, self.get_sum(), self.get_average())

    def __eq__(self, value):
        return self.get_sum()  == value.get_sum()

    def __ne__(self, value):
        return self.get_sum() != value.get_sum()
    
    def __gt__(self, value):
        return self.get_sum() > value.get_sum()

    def __ge__(self, value):
        return self.get_sum() >= value.get_sum()
    
    def __lt__(self, value):
        return self.get_sum() < value.get_sum()

    def __le__(self, value):
        return self.get_sum() <= value.get_sum()

    
#학생 리스트를 선언

students = [Student('윤인성', 87,98,88,95),
Student('연하진', 92,98,96,98),
Student('구지연', 76,96,94,90),
Student('나선주', 98,92,96,92),
Student('윤아린', 95,98,98,98),
Student('윤명월', 64,88,92,92)
]


#학생을 선언한다.

student_a = Student('윤이성', 87,98,88,95),
student_b = Student('연하지', 92,98,96,98),


#출력

print('student_a == student_b= ', student_a == student_b)
print('student_a != student_b =', student_a != student_b)
print('student_a > student_b =', student_a > student_b)
print('student_a >= student_b =', student_a >= student_b)
print('student_a < student_b =', student_a < student_b)
print('student_a <= student_b = ', student_a <= student_b)
    
'''

#클래스 변수


'''
class Student:
    count = 0

    def __init__(self, name, korean, math, english, science):
        #인스턴스 변수 초기화
        self.name = name
        self.korean = korean
        self.math = math
        self. english = english
        self.science = science

        #클래스 변수 설정

        Student.count +=1
        print('{}번째 학생이 생성되었씁니다.'.format(Student.count))



#학생 리스트르 선언합니다.


students = [Student('윤인성', 87,98,88,95),
Student('연하진', 92,98,96,98),
Student('구지연', 76,96,94,90),
Student('나선주', 98,92,96,92),
Student('윤아린', 95,98,98,98),
Student('윤명월', 64,88,92,92)
]

#출력하빈다.
print()
print('현재 생성된 총 학생 수는 {} 명 이빈다.'.format(Student.count))
'''


#클래스 함수

#클래스를 선언
'''
class Student:
    #클래스 변수
    count = 0
    students = []

    #클래스 함수
    @classmethod
    def print(cls):
        print('-----학생목록-----')
        print('이름 \t 총점\t 평균')
        for student in cls.students:
            print(str(student))
        print('--------------------------')

    #인스턴스 함수 

    def __init__(self, name, korean, math, english, science):
        self.name = nema
        self

'''



#사용자 정의 예외를 생성합니다.
'''
class CustomException(Exception):
    def __init__(self, message, value):
        Exception.__init__(self)
        self.message = message
        self.value = value
    
    def __str__(self):
        return self.message

    def print(self):
        print('오류 정보')
        print('메시지:', self.message)
        print('값:', self.value)

try:
    raise CustomException('딱히 이유없음', 273)
except CustomException as e:
    e.print()

'''



