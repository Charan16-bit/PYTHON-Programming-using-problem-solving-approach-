def fucn(a , b=10, *args,**kwargs):
    print(a,b,args,kwargs)
fucn(1,2+3,3,4,name = "charan")
###🟢 Q1 — Lambda
square = lambda x: x*x
print(square(5))

#🟡 Q2 — Lambda + condition

check = lambda x: "even" if x % 2 ==0 else "odd"
print(check(5))


#3Write a function that accepts any number of integers and returns their sum.

def total(*args):
    sum = 0
    for x in args:
        sum += x
    return sum
print(total(12,23,43,12,10))

#🟡 Q4 — Default argument
print("========")
def power(n,p=2):
    print(n * n)
    print(n + p+1)
power(5)


#🔴 Q5 — Keyword arguments

def student(name, age, course = "CSE"):
    return name , age, course
x = student(age= 21, name = "charan")
print(x)

#🔴 Q6 — Lambda + list

numbers = [ 1,2,3,4,5]
result = list ( map( lambda x : x * 2 , numbers))
print(result)

#🔴 Q7 — Lambda thinking

numbers = [10, 15, 20, 25, 30]

result = list(filter(lambda x: x % 2 == 0, numbers))

print(result)

#💀 Q8 — *args + lambda
def cal(*args):
    f = lambda x : x* 2
    return [f(x) for x in args]
print(cal(2,4,6))

#💀 Q9 — Coding challenge
print("+++")
def even_count(*args):
    count = 0
    for x in args:
        if(x%2==0):
            count +=1
    return count 

print(even_count(10,3,8,7,6))

##
def process(*args):
    result = []
    check = lambda x : x % 2== 0
    for x in args:
        
        if check(x):
            result.append(x)
    return result
print(process(3,8,11,20,25,40))

def add(a, b):
    """Adds two numbers."""
    return a + b
print(add.__doc__)