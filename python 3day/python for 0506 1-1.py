#for 문
'''
Sume = 0
for i in range(1, 10, 1):
    Sum = Sum + i
    print(' i ==> ', i, 'Sum ==< ' , Sum)


'''


#Sum = 0
'''
for i in range(1, 100, 1):
'''

'''
for i in range(2, 101, 2):
'''
'''
#for i in range(100, 0 , -5):
    for
    Sum = Sum + i
    print(' i ==> ', i, 'Sum ==> ' , Sum)
'''
#dan = int(input('몇 단 출력 : '))

#for i in range(1, 10):

 #   print(' {} * {} = {}'.format(dan, i, dan*i))

'''
for i in range(1,10):
    for b in range(
'''
"""
for i in range(1,10):
    for b in range(1, 10):
        print(" {} * {} = {}".format(i, b, i*b))
"""


'''
for i in range(1, 7):
    if i == 3:
        #continue #3만 건너뛰었다. continue는 스킵
        break # break는 빠져나간다.멈춤
    print(i, end = ' ') 
'''


'''
for i in range(1,10):
    for b in range(1, 10):
        print(" {} * {} = {}".format(i, b, i*b))

'''
'''
while True:
    
    dan = int(input('몇 단 출력 : '))
    if dan == 0:
        print('종료되었습니다.')
        break
    if dan <=2 or dan>9:
        continue
    for i in range(1, 10):

        print(' {} * {} = {}'.format(dan, i, dan*i))
'''



#별 삼각형
for i in range(0, 10):
  #print('')  
  for j in range(0,i):
      
        print("*", end = ' ')
      
  print(' ')

#for 에서 0은 이중 for문일 때 표시가 안된다.



     

'''
if False:
    print('참');

print('목요일') # 이부분은 if 문과 상관이 없다.

'''


'''
if (3<2) and (3==2):
    print(' 참' ); print('목요일')
'''

'''
while True:

    score = int(input("점수 입력 : "))
    if score == 0:
        break

    if score >100 or score <0:
        continue

    if score >= 90:
       
        print(score, '\n수 ')
    elif score >= 80:
        print(score, '\n우')
    elif score >= 70:
        print(score, '\n미')
    elif score >= 60:
        print(score, '\n양')
    elif score >= 50:
        print(score, '\n가')
    
    else:
        print(score, '\n집에 가세요.')
'''



'''
###성적 처리

st = []

with open('c:\\dd\\ss.txt', 'r', encoding = 'utf-8') as f:
    for i in range(10):
        st.append(f.readline().split() ) #line 단위로 읽어드림 readline()
        st[i][1] = int(st[i][1]) ##str ==> int형으로 변환 이순신 뒤에 85, 87, 90번을 int 형으로 바꿔야됨 아니면 str이 됨
        st[i][2] = int(st[i][2]) ##리스트 안의 숫자는 str형식이된다. 그러므로 int로 바꿔줘야 한다.
        st[i][3] = int(st[i][3])

        ##총점과 평균
        total = st[i][1] + st[i][2] + st[i][3]
        avg = total / 3
        st[i].append(total)
        st[i].append(avg)

        
##과목별 평균, 반전체 평균
total_kor = total_eng = total_mat = 0

for i in range(10):    
    total_kor = total_kor + st[i][1]
    total_eng = total_eng + st[i][2]
    total_mat = total_mat + st[i][3]
avg_kor = total_kor / len(st)
avg_eng = total_eng / len(st)
avg_mat = total_mat / len(st)

for i in range(10):
    print(st[i])
'''

    

'''

print('**********성적표************')
print('*****************************')
print('이름   국어   영어   수학   총점   평균')

for i in range(10):
    print(' {}    {}     {}     {}      {}     {:.1f}'
          .format(st[i][0], st[i][1], st[i][2], st[i][3], st[i][4], st[i][5])) 

print('***************************** \n')

print(' 국어 평균 : {} 영어 평균 : {}, 수학 평균 : {}, 반 평균{}'
      .format(avg_kor, avg_eng, avg_mat, (avg_kor+ avg_eng+ avg_mat)/3))

print(len(st))
'''


'''
for i in range(10):
    st.write(' {}    {}     {}     {}      {}     {:.1f}'
          .format(st[i][0], st[i][1], st[i][2], st[i][3], st[i][4], st[i][5]))
    st.write(' 국어 평균 : {} 영어 평균 : {}, 수학 평균 : {}, 반 평균{}'
      .format(avg_kor, avg_eng, avg_mat, (avg_kor+ avg_eng+ avg_mat)/3))
'''


'''
a = []

with open('c:\\dd\\city.txt', 'r', encoding = 'utf-8') as f:
   # k = f.read()
    for i in range(5):
        a.append(f.readline().split())
        a[i][1] = int(a[i][1])
      
   # print(len(k))
#       for i in range(5):
 #          print(a[i])

            
for i in range(5):
    print(a[i])
#print(type(b))
'''











