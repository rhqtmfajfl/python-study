def mysum(*x):
    s = 0
    for i in x:
        s+=i
    return s

ret = mysum(1,2,3)

print(ret)
