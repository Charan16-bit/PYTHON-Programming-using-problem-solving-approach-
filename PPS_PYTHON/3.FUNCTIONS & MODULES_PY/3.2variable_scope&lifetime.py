#Definition

"Scope is the area where a variable can be accessed (used)."

"There are 2 types:"

"Local Variable"
"Global Variable"
## reverse 
n = 5678433#global avriable
def reverse (n):  #fucntion header and parameter(n)
    reverse = 0 #local varible 
    while(n>0):
        digit = n % 10 # gives last elelment which the remainder of given number
        reverse = reverse * 10 + digit #REVERSE THE USING THIS LINE 
        n = n // 10   # REMOVES THE LAST NUMEBR FOR DECREASING SO THEAT CONDTION BECOMES FASKE TILL THE NUMBER COMMPLEETE 
    return reverse #return statement 
print(reverse(n))  # CALLS THE FUNCTION 

print("#Problem 2 – Palindrome Number")


n = 1221   # Global Variable

def palindrome (n):   # Function Header & Parameter
    original = n# keep inside of fucntion (local variable) therre is no use of globally 
    palindrome = 0   # Local Variable

    while(n > 0):
        digit = n % 10      # Extract last digit
        palindrome = palindrome * 10 + digit   # Build reverse number
        n = n // 10         # Remove last digit
    if(original == palindrome):
     print("palindrome")
    else:
       print("not palindrome")
  # Return reversed number
palindrome(n)
#🟢 Problem 3 – Count Even and Odd Digits
n = 12345678
def numbers(n):
    even = 0
    odd = 0
    while(n>0):
      digit = n % 10
      if(digit%2==0):
         even+=1 
      if(digit%2!= 0):
         odd +=1
      n = n // 10
    return(even,odd)
x = numbers(n)
print(x)
#🟢 Problem 4 – Sum of Digits Until Single Digit
n = 9875510
def sum(n):
   while(n>=10):
    sum1 = 0 
    while(n>0):
      digit = n % 10
      sum1 += digit

      n //=10
    n = sum1
   return sum1
    
x = sum(n)
print(x)

#🟢 Problem 5 – Factorial 
n = 5
def factorial(n):
    fact = 1
    for i in range(n,0,-1):
      fact = fact * i
    return(fact)

x = factorial(n)
print(x+2)
###prime numbers
print("--------")
def prime_range(a,b):
   for i in range(a,b+1):
      is_prime = True
      for j in range(2,i):
         if(i%j==0):
          is_prime = False
          break
      if(is_prime):
         print(i)
prime_range(10,30)

####second_largest
num = [10,25,8,40,15]
def second_largest(num):
   second = num[0]
   largest = num[0]
   for n in num:
      if(n > largest):
         second = largest
         largest = n
      elif (n > second):
         second = n
   return second

x = second_largest(num)
print("second largest Number is :",x)

###COPRIME
def coprime_num(a,b):
  coprime = True

  for i in range(2,a):
      if(a%i==0) and (b%i==0):
         coprime = False
         break
         print(i)
  return coprime
         
print(coprime_num(8,15))