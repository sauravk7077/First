#This stops a loop in between using 'break'
k = 5
for j in range(100,50,-1):
    if j % k is 0:
        print("This is number divisible by",k,"is",j)
        break

#This is a single line comment

'''
    This is a
    multiple
    line
    comment
'''

#This skips the divisible numbers and prints others using 'continue'
k = 7
for r in range(1,100):
    if r%k is 0:
        continue
    else:
        print(r)

#This prints multiples of 4 which are less than 100
for r in range(1,100):
    if r%4 is 0:
        print(r)
'''
#This is a better way
for i in range(4,100,4):
    print(i)
'''
