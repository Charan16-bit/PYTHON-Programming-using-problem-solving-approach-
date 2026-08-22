#🧠 Recursion & Call Stack
def factorial(n):
    if n == 1:          # Base case
        return 1

    return n * factorial(n - 1)

print(factorial(5))

#Print n → 1
def fun(n):
    if(n ==0):
        return
    print(n)
    fun(n-1)

fun(5)

#Print 1 → n
def fun1(n):
    if(n==0):
        return
    fun1(n-1)
    print(n)

fun1(5)

#Factorial ⭐
def fact(n):
    if(n == 0):
      return 1
    
    return n * fact(n-1)
x = fact(5)
print(x)

#Sum of 1 to n ⭐
print("____")
def sum(n):
    if(n==0):
        return 0 
    return ( n + sum ( n - 1))

x = sum(5)
print(x)


#power

def power(n):
    if(n == 1):
        return 0
    return n ** 5

x = power(2)
print(x)

#Sum of even numbers
def sum_even(n):
    if(n == 0 ):
        return 0 
    return sum_even(n + 2)

x = sum_even(2)
print(x)