#problem 1
n = 10 
i = 2
total = 0
while (i<= n):
     total = total + i
     i = i + 2 
print(total)
print("/n")
#problem 2
n1 = 7 
i1 = 2 
total_1 = 0
while(i1 <= n1):
     total_1 = total_1  + i1
     i1 = i1 + 2
print(total_1)
print("/n")
#problem 3
n2 = 7
i2 = 1
total2 = 1
while(i2 <= n2):
     total2 = total2 * i2
     i2 += 2
print(total2)
print("/n")
#problem 4 
n3 = 10
i3 = 2
count1 = 0
while( i3 <= n3):
    count1 = count1 + 1
    
    i3 += 2
print("/n")
print(count1)
print("/n")
# problem 5
n4 = 10 
i4 = 1
while ( i4 <= n4):
     if  i4 % 3 == 0 and i4 % 2!= 0:
          print(i4)
     i4 = i4 + 1
print("/n")
#problem 6
n4 = 20 
i4 = 1
while ( i4 <= n4):
     if  i4 % 3 == 0 and i4 % 2!= 0:
          print(i4)
     i4 = i4 + 1
print("/n")
n5 = 10
i5 = 1
count3 = 0
while (i<=n):
    count3 = count3 + 1
    i5 = i5 + 2
print(count3)
print("/n")    
#Print numbers from 1 to 5 using a while loop.
i = 1
while (i <= 5):
     print(i)
     i = i + 1
print("/n")
#Print numbers from 5 to 1 using a while loop.
i = 5 
while( i>= 1):
     print(i,"Print numbers from 5 to 1 using a while loop.")
     i = i -1 
print("/n")
#🏆 Question 3 (New Concept) This introduces skipping numbers.
i = 2 
while (i <= 10):
     print(i,"i += 2 :Skipping number")
     i = i+ 2
print("/n")
#Question 4 This introduces skipping numbers.
i = 1 
while (i <= 9):
     print(i,"i += 2:Skipping number")
     i += 2 
print("/t")     
#use a negative update.
i = 10 
while (i >= 2):
     print(i,"i -= SUB:Skipping number")
     i -= 2 
print("/t")   

#use a POSTIVE update.
i = 1
while (i <= 10):
     if (i % 2 == 0):
      print(i,"i += POS:Skipping number")
     i+=1
    

#Print only the odd numbers from 1 to 10.

i = 1
while (i <= 10):
     if (i % 2 != 0):
      print(i,"i += POS:Skipping number")
     i+=1
    
#Now let's learn a different style of if.
i = 1 
while (i <= 9):
        if (i == 3 or i == 6 or i == 9):
            print(i,"not modulus")
        i += 1

#Find the sum of numbers from 1 to 5.

n = 5
i = 1
total = 0
while (i<=n):
     total = total + i
     i = i + 1
print(total)

#Find the sum of even numbers from 1 to 10.
i = 1
total7 = 0
while(i <=  10):
    
     if(i % 2 == 0):
           total7 = total7 + i
     i = i + 1
print(total7)

#Count how many even numbers are present from 1 to 10.
i = 1
total7 = 0
while(i <=  10):
    
     if(i % 2 == 0):
           total7 = total7 + 1
     i = i + 1
print(total7)
print("/n")
#Count how many odd numbers are present from 1 to 15.

#Maximum while loop
largest = 0
i = 2
while (i <=10):
    if i > largest:
        largest = i
    i += 2
print(largest)

smallest = 10
i = 2
while (i <= 10):
    if ( i < smallest):
        smallest = i
    i += 2
print(smallest)

# Question 1 - Sum of Numbers
i = 1 
total = 0
while(i<=5):
     total = total + i
     i = i + 1
print(total,"SUM of Number")

#Question 2 - Count Even Numbers
n = 10 
i = 1
count = 0
while( i <= n):
    if ( i % 2 == 0):
          count = count + 1
    i = i + 1
print(count)
#Question 3 - Product of Odd Numbers
i = 1
n = 7
count = 1
while( i <= n):
    if ( i % 2 != 0):
         count = count *i
    i += 1
print(count) 

#write a program to print 20 horizontal asterisks(*)

a = 1 
b = 20
while (a <= b):
    print("*",end = " ")
    a = a + 1 
print("/n")
# to calculate the sum and average of first 10 number
i = 1 
s = 0
while(i <= 10):
    s = s+i 
    i += 1
avg = float(s)/ 10 
print("the sum of the 10 number is:",s)
print("the avg of the first 10 num:", avg)
####
n = 7
i = 1
sum = 0
while (i<= n):
     sum = sum + i 
     i = i + 2
print(sum)

n = 10
i = 1 
total = 0 
while( i <= n):
     total = total + i
     i = i + 2
print(total)
########
n = 12
i = 1
div = 0
while (i<=n):
     if (i % 2 == 0) and (i % 3==0):
         div = div + i 
     i = i + 1
print(div)
#
n = 20
i = 1
count = 0
while(i<=n):
     if ( i % 2 == 0) and (i % 5 == 0):
          count = count + 1 
     i = i + 1 
print( count )


###
n = 15
i = 1
largest = 0
while( i <= n):
     if ( i % 4 == 0):
          if i > largest :
            largest+= i
     i = i + 1
print("largest:",largest)

smallest = n
i = 1
while (i <= 10):
    if ( i < smallest):
        smallest = i
    i += 2
print(smallest)

n = 20
i = 1
total = 0
while(i<=n):
     if ( i % 3==0) and ( i % 5== 0):
          total = total + i
     i = i + 1 
print(total)

#Write a program to calculate the average of the first n natural numbers using a while loop.
n = 10
i = 1
sum = 0 
while(i <= n):
     sum += i
     i = i + 1

print(sum)
print(sum/n)
#Write a program to find the sum of numbers from m to n (both inclusive).
m = 5
n = 10
sum = 0
while(m<=n):
     sum = sum + m
     m = m + 1 
print(sum)

#Given two numbers m and n, find the sum of only the even numbers between m and n (inclusive).
m = 2
n = 12
sum = 0
while ( m <= n):
     sum = sum + m
     m = m + 2

print(sum)

#Given two integers m and n, count how many numbers are divisible by both 3 and 4 between m and n (inclusive)
m = 5 
n = 30 
count  = 0 
while (m <= n):
     if ( m % 3 == 0) and ( m % 4 == 0):
          count = count + 1
     m = m + 1
print("int",count)

#🏆 HackerRank Level 2 - Question #4 (Harder)
m = 10 
n = 40
largest = 0
while(m <= n ):
     if ( m % 7== 0):
          if(largest<m):
               largest = m
     m = m + 1 
print(largest)

#HackerRank Level 2 - Question #5
m = 10
n = 30
count = 0
sum = 0
while(m<=n):
     if( m % 5 == 0):
         sum = sum + i
         count = count + 1 
     m = m + 5
print("sum",sum)
print("count",count)

#🏆 HackerRank Level 3 - Question #1 ⭐⭐⭐⭐
m = 7
n = 20 
largest = 0
count = 0
while(m<=n):
     if(m % 2 == 0):
        count = count + 1

        if (largest <m):
          largest =  m 
          
     m = m + 1
print(largest)
print(count)
#This combines Count + Sum + Maximum in one program.
m = 10 
n = 50
count = 0
sum = 0 
largest = 0
while(m <= n):
     if (m % 3 ==0):
          count = count + 1

          if(m % 3 == 0):
               sum = sum + m

               if( m % 3 == 0):
                    if (m > largest):
                         largest = m
     m = m + 1
print(count)
print(sum)
print(largest) 

#Final Boss (HackerRank Level 3)
m = 1
n = 30
count = 0
sum = 0
largest = 0
average = 0
while(m <= n):
     if( m % 2 != 0):
        count = count + 1
        sum = sum + m 
           
        if(m > largest):
           largest = m
     m = m + 1
print("",count)
print(sum)
print(largest)
print(sum / count) 

#LEVEL 3 – DSA Foundation
n = 53892
count = 0 
while n > 0:
     count = count + 1 
     n = n // 10
print(count)
######
i = 1 
count = 0
total = 0
while( i<=10):
     if (i % 2 == 0):
          count+=1
          total += i
     i = i + 1
average = (total//count)
print("average",average)
print(4 * "*")
#📖 Topic 2 – Sum of Digits
n = 53892
total = 0
while( n > 0):
     digit = n % 10
     total = total + digit
     n = n // 10
print(total)
#Mock Test 1 – Sum of Digits (Level: Medium)
n = 876543
total = 0
while ( n > 0):
     digit = n % 10
     total = total + digit 
     n //= 10
print(total)

n = 90081
total = 0
while ( n > 0):
     digit = n % 10
     total = total + digit 
     n //= 10
print(total)

n = 482731
total = 0
while ( n > 0):
     digit = n % 10

     if(digit % 2 == 0):
          total = total + digit 
     n //= 10
print(total)
#######
n = 988751
count = 0
while ( n > 0):
     digit = n % 10

     if(digit % 2 != 0):
          count  = count  + 1 
     n //= 10
print(count)
##########
n = 593482
sum = 0 
count = 0
largest = 0 
while( n > 0):
     digit = n % 10
     sum = sum + digit

     if (digit % 2 == 0):
          count = count + 1 

     if (digit > largest):
          largest = digit
            
     n = n // 10
print("Sum =",sum)
print(count)
print(largest)

#📘 Level 3 – Topic 3: Product of Digits
n = 538 
product = 1
while (n > 0):
     digit = n % 10
     product = product * digit
     n = n // 10
print(product)

#
n = 234
product = 1
while (n > 0):
     digit = n % 10
     product = product * digit
     n = n // 10
print(product)

n = 482731
product = 1
while (n > 0):
     digit = n % 10
     if(digit % 2 != 0):
      product = product * digit
     n = n // 10
print(product)

###
n = 987654
count = 0
while(n > 0):
     digit = n % 10
     if( digit >5):
      count = count + 1
     n = n // 10
print(count)
####
n = 594832
product = 1
count = 0
smallest = 10
while(n > 0):
     digit = n % 10
     product *= digit
     if(digit % 2 != 0):
          count = count + 1
     if(digit< smallest):
          smallest = digit 
     n = n // 10
print(product)
print(count)
print(smallest)

#######📘 Level 3 – Topic 4: Reverse Number
n = 12345
reverse = 0
while (n>0):
     digit = n % 10
     reverse = reverse * 10 + digit 
     n = n // 10
print(reverse)
##########
n = 90810
reverse = 0
while (n>0):
     digit = n % 10
     reverse = reverse * 10 + digit 
     n = n // 10
print(reverse)

##########

n = 123
reverse = 0
while (n>0):
     if(n >= 1):
      digit = n % 10
      reverse = reverse * 10 + digit 
     n = n // 10
print(reverse)

n = 123
reverse = 0
while (n>0):
     if(n >= 1):
      digit = n % 10
      reverse = reverse * 10 + digit 
     n = n // 10
print(reverse)

##
n = 121

original = n
reverse = 0

while n > 0:

    digit = n % 10

    reverse = reverse * 10 + digit

    n //= 10
if (reverse == original):
     print("palidrome")

n = 151
original = n 
reverse = 0
while (n>0):
     digit = n % 10
     reverse = reverse * 10 + digit 
     n = n // 10
if (reverse == original):
     print("palidrome")

##
n = 123
original = n 
reverse = 0
while (n>0):
     digit = n % 10
     reverse = reverse * 10 + digit 
     n = n // 10
if (reverse == original):
     print("palidrome")
else:
     if (reverse !=original):
       print("not palidorome")
     
##
n = 1441
original = n 
reverse = 0
while (n>0):
     digit = n % 10
     reverse = reverse * 10 + digit 
     n = n // 10
if (reverse == original):
     print("Valid")
else:
   if (reverse !=original):
       print("invalid PIN")

#######
n = 9889
original = n 
reverse = 0
sum = 0
count = 0
while (n>0):
     digit = n % 10
     reverse = reverse * 10 + digit 
     sum = sum + digit
     if(digit % 2 == 0):
          count = count + 1
     n = n // 10
if (reverse == original):
     print("palidrome")
else:
     if (reverse !=original):
       print("not palidorome")

print(sum) 
print(reverse,count)

#An ancient temple stores a 3-digit secret code to unlock its treasure chamber.
##### ARM STRONG
n = 153
ordinary = n
sacred = 0
while (n>0):
     digit = n % 10
     sacred += digit ** 3
     n = n // 10
if( ordinary == sacred):
     print("sacred")
else:
     print("ordinary") 

#Prime number
n = 29
count = 0
i = 1
while i<=n:
     if ( n % i == 0):
          count = count + 1
     i = i + 1
if(count == 2):
     print("primeghgh")
else:
     print("not prime")
######ff
num = str(121)
if num == num [::-1]: 
     print("okya")
else:
     print("j")
#GCD
a = 12 
b = 18
i = 1
gcd = 1
while (i <= a) and (i <= b):
     if (a % i) and ( b % i):
        gcd = 1
     i += 1
print("GCD",gcd)
#LCM (Least Common Multiple)
a = 12
b = 18

lcm = 1
while True:
     if (lcm % a == 0) and (lcm % b == 0):
          break
     lcm += 1 
     
print("LCM", lcm)

a = 12
b = 18
i = 1 
while i<= a*b:
     if(i%a==0) and (i%b==0):
          lcm = i
          print("LCM11",lcm)
          i = a * b + 1
     else:
          i += 1