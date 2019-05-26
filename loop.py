stuffs = ["Cake", "Pen", "Jackhammer", "Chainsaw", "Shotgun"]

#Using a for-loop to print the stuffs
#Begins from 2nd element of list
for s in stuffs[2:]:
    print(s)
    print(len(s))

#for-loop using range
print("Using Range")
for i in range(1,10,1): #range(from, to, increment value)
    print(i*10)

#fizz or buzz in place of 3 and 5
a = 5
b = 3

for i in range(1,101):
    if i % (a*b) is 0:
        print("FizzBuzz")
    elif i%a is 0:
        print("Fizz")
    elif i%b is 0:
        print("Buzz")
    else:
        print(i)

#While loop to check even number from 1 to 100
i = 1
while i <= 100:
    if i%2 is 0:
        print("Even")
    else:
        print('Odd')
    i += 1
