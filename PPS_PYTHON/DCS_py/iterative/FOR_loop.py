#🚀 Let's Start – Problem 1
#🏫 School Attendance System
for i in range (1,21):
    print("Student Roll No:",i)

#🏥 Hospital Appointment System
for i in range (2,21,2):
    print("Patient Token :",i)

### OR 
for i in range(1,21):
   if (i % 2 == 0):
       print("Patient Token :",i)

#💰 Bank Salary System
for i in range(1 ,13):
    print("Salary Month : ",i)

#🏫 University Scholarship System
for i in range(1,26):
    if(i % 2 != 0):
        print("Scholarship Candidate : ",i)

#🏭 Factory Quality Check
for i in range(5,31):
    if(i % 5 == 0):
        print("Quality Check :",i)


#🚀 Algorithm 1 – Prime Number using for
count = 0
i = 1
n = 37
for i in range(i,n +1 ):
    if(37%i==0 ):
     count = count + 1
if(count == 2):
         print("Secure ID")
else:
        print("Insecure ID")

#🏆 Algorithm 2 – Perfect Number using for
count = 0
i = 1
n = 28
for i in range(i,n +1 ):
    if(i<n):
     if(n%i==0 ):
      count = count + i
if(count == n):
         print("Perfect ID")
else:
        print("imperfect ID")

#🏆 Algorithm 3 – GCD using for
a = 24 
b = 36
gcd = 1
for i in range(1,min(a,b)+1):
    if(a % i ==0) and (b % i ==0):
        gcd = i
print(gcd)
#🏆 Algorithm 4 – LCM using for
a = 12
b = 18
lcm = 0 
for i in range (max(a,b),a*b+1):
    if(i % a == 0) and (i % b ==0):
        lcm = i
        break
print(lcm)

#🤖 Robot Energy Generation
n = 10
first = 0
second = 1 
for i in range(first , n ):

    print(first,end = " ") 
    sum = first + second
    first = second
    second = sum 
print("/a")
#🏆 Algorithm 6 – Reverse Number using for
n = 947531
reverse = 0 
digit = len(str(n))
for i in range(digit):
    digit = n % 10
    reverse = reverse * 10 + digit 
    n = n // 10
print(reverse)

#🏆 Algorithm 7 – Multiplication Table (for)
n = 7
for i in range(1 , 11):
    print(n, "x",i,"=",n*i)
    
#🏆 Algorithm 8 – Factorial using for
n = 5
product = 1
for i in range (1, n + 1 ):
    product = product * i
print(product)
#🚀 Next Algorithm 9 (Slightly Harder)
num = [12,7,5,18,9,4]
count_even = 0
count_odd = 0
for i in (num):
    if (i % 2 ==0):
        count_even += 1
    if(i % 2!= 0):
        count_odd +=1

print(count_odd)
print(count_even)


#🏆 Algorithm 10 – Sum of Natural Numbers (for)
n = 10
total = 0
for i in range(1,n+1):
    total += i
print(total)

#🏆 Algorithm 11 – Sum of Squares
n = 5
sum = 0
for i in range(1,n+1):
    sum = sum + i ** 2
print("",sum)

#🏆 Algorithm 12 – Count Multiples of 3
n = 20
count = 0
for i in range(1,n+1):
    if(i % 3 == 0 ):
        print("numbers are :",i)
        count += 1;print()
print("the count:",count)

#🏆 HackerRank Challenge #1
n = 8
count = 0
for i in range(1 , n + 1):
         count += 1
print("Positive Number = ",count)

#🏆 HackerRank Challenge #2 – Count Even Numbers

n = 15
count = 0
for i in range(2,n+1,2):
    count += 1
print("Even Number :",count)


##
n1 = 248642
n2 = 248641
n1_rs = 0
n2_re = 0
while(n):
    digit = n % 10
    
    if (n1 % 2 ==0):
        print("Strong password")
    else:
        print("weak Password")
    
    n = n // 10
print("/a")
#🏆 HackerRank Challenge #1

transaction_action = 131 

digit_count = 0
digit_sum = 0
digit_product = 1
largest_digit = 0
smallest_digit = 9
reverse = 0
original = transaction_action
prime = 0
###condition 

while(transaction_action > 0):
    digit = transaction_action % 10
    digit_count += 1
    digit_sum += digit 
    digit_product *= digit
    reverse = reverse * 10 + digit
    if(digit > largest_digit):
        largest_digit = digit 
    if (digit < smallest_digit):
        smallest_digit = digit

    transaction_action = transaction_action // 10
if(reverse == original):
 print("palindrome = true")
else:
    print("palindrome = false")

for i in range (1, original+1):
    if(original % i == 0 ):
          prime += 1
if(prime == 2):
 print("Prime = True")
else:
 print("Prime = False")



print("Digit Count43:",digit_count)
print(digit_sum)
print(digit_product)
print(largest_digit)
print(smallest_digit)
print(reverse)

#Employee Bonus
n = 50
for i in range(1 , n + 1):
    if(i % 4 == 0):
        print("Employee Bonus",i)

#Banking System

n = 100
sum = 0 
for i in range ( 1 , n + 1):
    sum = sum + i 
print("Banking System",sum)

#🏆 Problem 3 ⭐⭐⭐
n = 200
count = 0
for i in range (1 , n + 1):
    if(i % 7 == 0):
        count = count + 1
print("Student Portal",count)


#Security Check

n = 100
for i in range(1,n + 1):
    if(i % 3 == 0 ) and (i % 5==0 ):
        print("Student Portal:",i)

#ATM system
largest = 0
for i in range(1 ,36 ):
    if(36 % i ==0 ):
        largest = i
print("largest factor",largest)

#problem 6
sum = 0
for i in range( 1 , 101):
    if(i % 3 ==0) or ( i % 5 == 0):
        sum += i
print("SUM of 1 to 100 that re divisbile by 3 or 5 ",sum)

#problem 7
n= 50
for i in range(1 ,n+1):
   if ( 50 % i == 0):
       print("prime number",i)


#🏆 Problem 8 ⭐⭐⭐⭐⭐
perfect = 0
count = 0 
n = 100
for i in range(1 , n ):
    if(i<n):
     if (n % i == 0 ):
        perfect += i
        print("",perfect)
    
#🏆 Problem 9 ⭐⭐⭐⭐⭐⭐
gcd = 0 
a = 24
b = 36
for i in range( 1, min(a,b)+1):
    if(a % i == 0) and ( b % i ==0 ):
        gcd = i
print(gcd)

#######
lcm = 0 
a = 24
b = 36
for i in range( max(a,b),a *b + 1):
    if(i % a == 0) and ( i % b ==0 ):
        lcm = i
        break
print(lcm)
       

#problem 10
even = 0
odd = 0
even_sum = 0
odd_sum = 0 
n  = 100
for i in range(1 , n+1 ):
    if( i % 2 ==0 ):
        even +=1 
        even_sum += i
    if(i % 3 ==0 ):
        odd += 1
        odd_sum+= i
print(even,odd,even_sum,odd_sum)
##
for i in range( 10,0,-2):
    print("*"*i)    