

def myRange(f,t,i):
    list = []
    while f < t:
        list.append(f)
        f += i
    return list

def myRange(t):
    return myRange(0,t,1)

for i in myRange(1,100,5):
    print(i)
