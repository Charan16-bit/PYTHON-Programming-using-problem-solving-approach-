# basics to call the function
def wel1():
    print("welcome"*2)
wel1()
###
def wel ():
    for i in range(4):
        print(i)
wel()
# Parentheses () are used to call (execute) a function and pass data to it (if needed).
def welcome (name):
    print("welcome",name)
welcome("charan")
####Call it 4 times.
def stars():
    for i in range(5):
        print("*****")
    
stars()

###
def college(campus):
    i = 1 
    while(i<=3):
        print("Welcome to SRM",campus)
        i+=1
college("KTR")
#########
def menu():
    print("login: 5667")
    print("register:getting into it")
    print("signoff")
menu()

#Parameter and Argument
def student(name):
    print("student name : ",name)
    
student("charan")
student("virat")
student("dhoni")
#Print the square of the given number.
def square(n):
    print(n*n)
square(5)
square(8)
square(10)
#Print the multiplication table of the given number.

def table(num):
     i = 1
     while (i<=10):
        print(num,"x",i,"=",num*i)
        i+=1
table(5)
table(2)
table(10)


#If mark ≥ 50
def grade(marks):
    if(marks >= 50):
        print("Pass")
    else:
        print("Fail")
grade(75)
grade(30)
grade(90)
print("__________ ___")                        
#
def charan (age):
    print("Charan:",age)
charan(21)

#retrn sstatement 
def square1(n):
    return(n*n)

x =square1(6)
print(square1(9)+ 4)
#
def add(a,b):
    return(a+b)

print(add(5,6)+10)
####
def even(num):
    if(num%2==0):
        print(num,"EVEN")
    else:
        print("odd")

even(2)
even(5)
even(17)
even(20)


######Print the factorial of a number using a while loop.
def factorial(n):
    result = 1
    while(n>0):
        result*=n
        n-=1
    return result
x = factorial(5)
print(x+3)
