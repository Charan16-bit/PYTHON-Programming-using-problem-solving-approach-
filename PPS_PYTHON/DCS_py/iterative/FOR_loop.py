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
n = 10 
mutliply = 1
for i in range(1,n+1):
    if(n * i == 7):
     mutliply = mutliply * 7
     print("7","x",i,"=",mutliply)