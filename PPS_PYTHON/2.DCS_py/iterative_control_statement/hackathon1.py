#Print all numbers from 1 to 50 that are divisible by 3 or 5.
i = 1
n = 50
while(i<=n):
    if ( i % 3 == 0) or (i % 5 == 0 ):
        print(i)
    i = i + 1

#Find the sum of all even numbers from 20 to 60.
i = 20
sum = 0 
while(i <= 60):
    if( i % 2 == 0):
        sum = sum + i
    i = i + 1
print(sum)

#Count how many numbers between 1 and 100 are divisible by 4 but not by 8
i = 1
count = 0
while( i <= 100):
    if(i % 4 == 0) and (i % 8 != 0):
        count = count + 1
    i = i + 1
print(count)

#Find the largest odd number between 50 and 100.
i = 50 
largest = 0 
while( i <= 100 ):
    if( i % 2 != 0 ):
        if(i > largest):
            largest = i 
    i = i + 1
print(largest)

#Sum of digits,Product of digits,Largest digit
n = 983741
sum = 0
product = 1
largest = 0
while (n > 0):
    digit = n % 10
    sum = sum + digit 
    product = product * digit
    if( digit > largest ):
        largest = digit 
    n = n // 10
print("sum",sum)
print(product)
print(largest)

#Reverse the number.
n = 421

original = n
reverse = 0

while n > 0:

    digit = n % 10
    reverse = reverse * 10 + digit
    n //= 10

print(reverse)

if reverse > original:
    print("Greater")
else:
    print("Smaller")

#Count how many even digits are present.
n = 864927
count = 0
while(n>0):
    digit = n % 10
    if( digit % 2 == 0):
        count  = count + 1
    n = n // 10
print(count)

#Between 100 and 300:
m = 100
n = 300
count = 0
sum = 0
largest = 0
while n > m: 
    if(m % 7== 0):
        count += 1
        sum += m
        if(m > largest):
         largest = m
    m = m + 1
print("",count)
print(sum)
print(largest)

###
n = 864253
reverse = 0
sum = 0
product = 1
smallest = 10
count = 0
while( n > 0):
    digit = n % 10
    reverse = reverse * 10 + digit 
    sum = sum + digit 
    product = product * digit 
    if( digit < smallest):
        smallest = digit 
    if ( digit % 2 != 0):
        count = count + 1 
    n = n // 10 
print(reverse)
print(sum)
print(product)
print(smallest)
print(count)

#
m = 50
n = 150
count = 0
sum = 0
product = 1
largest = 0
while n >= m: 
    if(m % 5== 0):
        count += 1
        sum += m
    if(m % 5== 0) and (m % 2 != 0):
        product = product * m
        if(m > largest):
           largest = m
    m = m + 1
average = sum // count
print("",count)
print(sum)
print(largest)
print(product)
print(average)

#Q1 ⭐ (Variables + Operators)
a = 15 
b = 4 
add = a + b 
sub = a - b
multi = a * b
div = a / b
flrdiv = a // b
mod = a % b
print(add,sub,multi,div,flrdiv,mod)

#Q2 ⭐ (Input + Type Conversion)
a = int(4)
b = int(5)
sum = a + b
product = a * b 
average = ( sum // 2)
diff = (a - b)
print(sum,diff,average,product)

#Q3 ⭐⭐ (Decision Statement)
a = 5
if(a>0):
    print("Positive")
elif(a<0):
    print("Negative")
else:
    print("zero")

#Q4 ⭐⭐ (Nested If)
a = 4
b = 3
c = 5
if(a > b):
    if ( a > c):
        print( " A is the largest ")
    else: 
        print("c is the largest:")
else:
    if( b> c ):
        print("B is the largest :")
    else: 
        print("C is the largest")

###Q5 ⭐⭐ (Logical Operators)
int = 6
if ( int % 4 == 0) and ( int % 6 == 0):
    print("Divisible by both 4 and 6")
else: 
    print("Not divisible")


#Q6 ⭐⭐⭐ (While + Sum)
m = 1
sum = 0
while(m <= 100):
        if m % 7 == 0:
         sum = sum + m
        m = m + 1
print(sum)

#Q7 ⭐⭐⭐ (While + Count)
m = 50
count = 0
while(m <= 150):
        if (m % 5 == 0) or (m % 3 == 0):
         count = count + 1
        m = m + 1
print(sum)

#Q8 ⭐⭐⭐ (Digit Problem)
n = 847263
sum = 0 
count = 0 
while(n > 0):
    digit = n % 10
    sum = sum + digit 
    if ( digit % 2 == 0 ):
        count = count + 1 
    n = n // 10 
print(sum)
print(count)
#Q9 ⭐⭐⭐⭐ (Combined)
n = 948531
reverse = 0
product = 1 
largest = 0
smallest = n
while(n > 0 ):
    digit = n % 10
    reverse = reverse * 10 + digit
    product = product * digit 
    if( digit > largest ):
        largest = digit 
    if( smallest > digit ):
        smallest = digit
    n = n // 10 
print("reverse", reverse)
print(product)
print(largest)
print(smallest)

#Q10 ⭐⭐⭐⭐⭐ (Mini Interview)
m = 10
n = 100
count = 0
sum = 0
average = 0
product = 1
while( m <= n):
    if( m % 4 ==0 ):
        count = count + 1
        sum = sum + m
        if(m > largest ):
         largest = m
        if( m % 4 ==0 ) and  ( m % 2 == 0):
         product = product * m 
    m = m + 1
average = (sum // count)

print("count",count)
print(sum)
print(average)
print(average)
print(product)
####🛒 Q1. Supermarket Billing System ⭐
m = 100
n = 500
total = 0
numbers = 0
while( m <= n ):
        total = total + m
        count = count + 1
average = (total // count)
print(total)
print(count)
print(average)