#A function named something

def something():
    print("Don't read this. This prints crap.")

#Use the function
something()

#A useless function which tells burgers worth in terms of pizza
burger = 50.0
pizza = 100.0
def burger_to_pizza(amount):
    value = amount * burger / pizza
    print(amount,"Burgers are worth", value, "pizzas")

burger_to_pizza(3)


#This function 'fact' gives factorial of a number using 'return'
def fact(num):
    store = 1
    for i in range(num,0,-1):
        store *=i;
    return store

print(fact(10))


#Default Argument function
def isAdult(age = 4):
    if(age < 18):
        print("You are not an adult")
    else:
        print("You are an adult")

isAdult()

#Keyword Argument function
def doSomething(a = 6,b=7):
    return a*b+a+b-(a*8)-(b*7)

print(doSomething(b= 8,a = 99))

#Variable argument in a function
def add(*args): #args is not necessary
    sum = 0
    for i in args:
        sum += i
    print(sum)

add(1,2,3,4)
