####🛒 Q1. Supermarket Billing System ⭐
m = 100
n = 500
total = 0
count = 0
while( m <= n ):
        total = total + m
        count = count + 1
        m += 1
average = (total // count)
print(total)
print(count)
print(average)

#🏃 Q2. Marathon Registration ⭐⭐
m = 1 
n = 200
count = 0
sum = 0
largest = 0
while(m<=n):
        if ( m % 5 == 0):
         count = count + 1
         sum = sum + m
         if (m > largest):
               largest = m
        m = m + 1
print(count)
print(sum)
print(largest)
#🏦 Q3. ATM Cash Machine ⭐⭐⭐
m = 100
n = 1000
count = 0
sum = 0
largest = 0 
while(m<=n):
    if(m % 200 == 0):
            count = count + 1
            sum = sum + m
            if ( m > largest ):
                  largest = m
    m = m + 1
print("",count)
print(sum)
print(largest)

##🎓 Q4. Student Marks Analysis ⭐⭐⭐
n = 984751
sum = 0
product = 1
largest = 0
smallest = n
odd = 0
while n > 0:
    digit = n % 10
    sum = sum + digit
    product *= digit
    if(digit > largest ):
            largest = digit
    if(digit < smallest):
          smallest = digit
    if( digit % 2 != 0):
          odd = odd + 1
    n = n // 10
print("",sum)
print(product)
print(largest)
print(smallest)
print(odd)
      
#🚦 Q6. Traffic Fine System ⭐⭐⭐⭐
n = 753826
reverse = 0
count = 0
largest = 0
original = n
while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit 
    if(digit % 2 == 0):
        count = count + 1
    if(digit > largest):
          largest = digit
    n = n // 10
if (reverse > original):
      print("High risk")
else:
      print("Ssafe")

print("",reverse)
print(count)
print(largest)
print(original)
#🏏 Q8. Cricket Jersey Selection ⭐⭐⭐⭐⭐
m = 1 
n = 99
count7 = 0
count9 = 0 
largest = 0
sum = 0
while m <= n:
    if (m % 7 ==0 ):
         count7 = count7 + 1

    if (m % 9 == 0):
     count9 = count9 + 1

    if m % 3 == 0 and m % 5 == 0:
       if(m > largest):
          largest = m
    if(m%2==0):
     sum = sum + m
    m = m + 1
print("#🏏 Q8. Cricket Jersey Selection ⭐⭐⭐⭐⭐",count7,count9,largest,sum)
      
#🏢 Q9. Employee ID Verification ⭐⭐⭐⭐⭐
n = 897654
reverse = 0
sum = 0
product = 1
largest = 0
smallest = n
count = 0
while n > 0 :
     digit = n % 10
     reverse = reverse * 10 + digit
     sum += digit
     if( digit % 2 == 0):
          product = product * digit
     if(digit > largest):
          largest = digit
     if(digit < smallest):
          smallest = digit
     if(digit > 5):
          count = count + 1
     n = n //10
print("🏢 Q9. Employee ID Verification ⭐⭐⭐⭐⭐",reverse,sum, product,largest,smallest,count)
## 🏦 Q1 – Bank Security ⭐
n = 37
i = 1 
count = 0
while i<=n:
      if n % i==0:
         count += 1
      i +=1
if count == 2 :
     print("secure")
else:
     print("Rejected")

#🏛️ Q2 – Temple Donation ⭐
donation = 28
i = 1 
total = 0
while i < donation :
      if (donation % i == 0):
         total += i 
      i = i + 1
if(total == donation  ):
     print("balanced")
else:
     print("inbalance")

##⚡ Q3 – Electricity Board ⭐⭐
n = 100
i = 1 
count = 0
while i<=n:
      if n % i==0:
         count += 1
      i +=1
print(count)
#🏥 Q4 – Hospital System ⭐⭐
n = 1000
i = 1 
total = 0
while i < n :
      if n % i==0:
         total += i
      i +=1
print("Balanced IDs:",total)

#🚀 Q5 – Space Mission ⭐⭐⭐
n = 496
i = 1 
total = 0
while i < n:
      if n % i==0:
         total += i
      i +=1
if(total == n  ):
     print("balanced")
else:
     print("inbalance")

#🏢 Q6 – Company Recruitment ⭐⭐⭐
n = 150
i = 50
count = 0
largest = 0
while i <= n:
      if n % i==0:
         count += 1
      i +=1
if(n > largest):
      largest = n

print("Secure ID",count)
print(largest)
#🧩 Q7 – Mixed Logic ⭐⭐⭐⭐
n =29
count = 0
sum = 0
i = 1
while( i < n) or (i <= n):
      if( n % i ==0):
          count += 1
          sum += i
      i = i + 1
if ( count == 2 ):
     print("Whether it is Secure")
else:
     print("insecure")

print("Number of factors:",count)
print("sum of proper factors",sum)
     
#🏆 Q8 – Interview Challenge ⭐⭐⭐⭐⭐
m = 1
n = 100
count = 0
sum =0
while( m < n) or (m <= n):
      if( m % n ==0):
          count += 1
          sum = count + i
      m = m + 1
if ( sum == m ):
     print("Whether it is Secure")
else:
     print("insecure")

print("Count of Secure numbers:",count)
print("Count of Balanced numbers",sum)
#########     
n = 7
first = 0 
second = 1
count = 0
while count <= n:
     print("+",first,end = "")
     print()
     next = first + second 
     first = second 
     second = next 
     count +=1
#🚀 Q1 – Rocket Fuel System ⭐
n = 12
first = 0
second = 1
count = 0
while count < n :
     print(first,end = " " )
     
     next = first + second 
     first = second 
     second = next 
     count = count + 1
print("\n")
#🏦 Q2 – Bank Interest Prediction ⭐⭐
interestvaule_year = 15
year1 = 0
year2= 1
count = 0
largest = 0
while count <= interestvaule_year:
     every_year = year1 + year2
     year1 = year2
     year2 = every_year
     count += 1
if(year1 > largest  ):
     largest = year1
print("",largest)

#🤖 Q3 – Robot Battery System ⭐⭐⭐
bat = 10
bat_1 = 0
bat_2 = 1
count = 0 
largest = 0
while count <= bat:

     every_newbat = bat_1 + bat_2
     bat_1 = bat_2
     bat_2 = every_newbat
     count += 1
     print( bat_1,end = " ")
if(bat_1 > largest ):
     largest = bat_1
print("Total Enegry = ",largest)
###🏭 Factory Machine Design GCD
a = 24
b = 36
i = 1 
gcd = 1
while (i<=a) and (i<=b):
      if(a % i==0) and (b % i==0 ):
          gcd = i 
      i += 1
print("GCD", gcd)

#Q2 – Chocolate Distribution ⭐⭐
a = 54
b = 90
i = 1 
gcd = 1
while (i<=a) and (i<=b):
      if(a % i==0) and (b % i==0 ):
          gcd = i 
      i += 1
print("GCD2", gcd)

#🪢 Q3 – Rope Cutting Challenge ⭐⭐⭐
a = 24
b = 60
c = 84
i = 1
gcd = 1 
largest = 0
while i<= (a) and (b) and (c) :
      if(a%i==0) and (b%i==0) and (c%i==0):
          gcd = i
      i += 1
if(gcd > largest ):
     largest = gcd
print("GCD3",largest)
#🏥 Hackathon – Smart Hospital ID Verification System
n = 947531
sum = 0
product = 1
largest = 0
smallest = n
reverse = 0
original = n
odd_count = 0
armstrong = 0 
i = 1
while n > 0:
     digit = n % 10
     sum += digit 
     product *= digit 
     armstrong += digit ** 3
     reverse = reverse * 10 + digit
     if(digit > largest):
          largest = digit
     if(digit < smallest):
          smallest = digit    
     if(digit % 2 != 0):
          odd_count += 1
     
     n = n // 10
if(reverse==original):
          print("palidrome:")
else:
          print("Not palidrome")

while(i<=n) ^ (i<n):
     if(n%i==0):
         total += i
     i += 1
if(n == 2 ):
      print("PRIME NUMBER")
else:
      print("Perfect number")
print(total)
print(product)
print(largest)
print(smallest)
print(reverse)
print(count)
print(sum)


#📱 Mobile Recharge Company

Transaction_ID = 987654

count = 0
while Transaction_ID > 0:
     digit = Transaction_ID % 10
     count = count + 1
     Transaction_ID = Transaction_ID // 10
print("thrfhrthrt",count)        
     
#🏦 ATM Cash Audit

Transaction_Code = 482731

total = 0
while Transaction_Code > 0:
     digit = Transaction_Code % 10
     total = total + digit
     Transaction_Code = Transaction_Code // 10
print("Digit Total = ",total)   

#🛒 Supermarket Billing System
Transaction_Code = 538

total = 1
while Transaction_Code > 0:
     digit = Transaction_Code % 10
     total = total * digit
     Transaction_Code = Transaction_Code // 10
print("Digit Total = ",total)   
     
     
#🏢 Company HR System
Transaction_Code = 594832

total = 0
while Transaction_Code > 0:
     digit = Transaction_Code % 10
     if(digit > total):
          total = digit
     Transaction_Code = Transaction_Code // 10
print("Digit Total = ",total)   


#🏥 Hospital Patient ID System
Transaction_Code = 594832
total = Transaction_Code
while Transaction_Code > 0:
     digit = Transaction_Code % 10
     if(digit < total):
          total = digit
     Transaction_Code = Transaction_Code // 10
print("Digit Total = ",total)

#🏆 Hackathon Q6 ⭐⭐⭐⭐⭐
n = 864213
reverse = 0
while n > 0 :
     digit = n % 10
     reverse = reverse * 10 + digit
     n = n // 10
print("Encrypted Code = ",reverse)

#🛂 Airport Immigration System

n = 1221
reverse = 0 ;original = n
while n > 0 :
     digit = n % 10
     reverse = reverse * 10 + digit
     n = n // 10

if(reverse == original):
     print("Verified")
else:
     print("Rejected")


#🏛️ Ancient Temple Authentication

n = 153
original = n
mat_rule = 0 
while n > 0 :
     digit = n % 10
     mat_rule = mat_rule + digit ** 3
     n = n // 10
print(mat_rule)

if(mat_rule == original):
     print("sarced")
else:
     print("ordinary")

#🏆 Hackathon Q9
n = 97
i = 1
count = 0
while (i <= n):
     if(n % i ==0):
      count += 1
     i = i + 1
print(count)

if(count == 2):
     print("secure ID")
else:
     print("In secured")


#🏛️ National Identity Verification System
n = 28
i = 1
perfect = 0
while (i <  n):
     if(n % i ==0):
       perfect += i
     i = i + 1
print(perfect)

if(perfect == n):
     print("Verified Citizen")
else:
     print("Unverified Citizen")



          