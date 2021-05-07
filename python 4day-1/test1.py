
st = []

with open('c:\\dd\\ss.txt', 'r', encoding = 'utf-8') as f:
   for i in range(10):
        st.append(f.readline().split())
        st[i][1] = int(st[i][1])
        st[i][2] = int(st[i][2])
        st[i][3] = int(st[i][3])

        total = st[i][1] + st[i][2] + st[i][3]
        avg = total / 3
        st[i].append(total)
        st[i].append(avg)

total_kor = total_eng = total_mat = 0

for i in range(10):
    total_kor = total_kor + st[i][1]
    total_eng = total_eng + st[i][2]
    total_mat = total_mat + st[i][3]

avg_kor = total_kor / len(st)
avg_eng = total_eng / len(st)
avg_mat = total_mat / len(st)

        
#for i in range(10):
for i in range(10):
        print(st[i])


for i in range(10):
    print(' {}     {}    {}    {}    {}    {:.2f}'.format(st[i][0], st[i][1], st[i][2], st[i][3], st[i][4], st[i][5]))

 
