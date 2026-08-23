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
    if(n == 10 ):
        return 10
    
    
    if(n % 2==0):
      return n + sum_even(n+2)

x = sum_even(2)
print(x)

# sum of odd number
def sum_odd(n):
    if(n == 9):
        return 9
    
    if(n % 2 != 0):
        return n + sum_odd(n+2)
    
x = sum_odd(1)
print(x)

#Count digits
print("___________")
def count ( n):
    if ( n == 0):
        return 0 
    return 1 + count ( n // 10 )
x = count(12345)
print(x)

##

def sum_count(n):
    if(n == 0):
        return 0
    return  n % 10 + sum_count( n //10)

x = sum_count(12345)
print(x)
#####
print("__________")
def reverse_num(n,reverse = 0):
    if(n == 0):
        return reverse
    digit = n % 10
    reverse = reverse * 10 + digit 
    
    return reverse_num(n // 10 , reverse)


x = reverse_num(12345)
print(x)