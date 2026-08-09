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