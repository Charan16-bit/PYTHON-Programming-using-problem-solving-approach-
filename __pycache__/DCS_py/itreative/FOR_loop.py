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
         print("Secure ID")
else:
        print("Insecure ID")

