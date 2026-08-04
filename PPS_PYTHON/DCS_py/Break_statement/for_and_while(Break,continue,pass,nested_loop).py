## while loop 
i = 1
while (i<=5):
    if(i==4):
     break 
    print("checking attempt : ", i,)
    
    i+=1
if(i==4):
    print("PIN verified")
########
for i in range(1,21):
       if(i==17):
        break
       print("checking box:",i)
if(i==17):
   print("treasure found in the 17th box")
####
for i in range(1 ,101):
     if(i % 17 ==0):
        print(i," is divisible by 17",)
        break
     print(i)
#🏆 HackerRank Challenge #1 – Security Gate
i = 1
while ( i<=20):
    if ( i == 7):
        print("Manager ID",i)
        i+=1
        continue
    print("Checking ID",i)
    i+=1

#🏆 HackerRank Challenge #2 – ATM Transactions
i =1 
while(i<=30):
    if(i % 5==0):
        print("SKIP THE ",i," % 5 ==0",i)
        i+=1
        continue
    print("allowed for divisble by 30",i)
    i+=1
#🏆 HackerRank Challenge #3 – Even Numbers Only
i = 1
while(i<=20):
    if(i%2!=0):
        i+=1
        continue
    print(i)
    i+=1

#🏆 HackerRank Challenge #4 – Student Attendance
i = 1
while(i<=15):
    if(i == 4) or (i==9) or (i== 13) and i in [4,9,13] :
        print("absent students:",i)
        i+=1
        continue
    print("Present students:",i)
    i+=1

#🏆 HackerRank Challenge #5 – Prime Numbers
i = 1
while(i<= 30):
    count = 0
    
    j = 1
    while(j<=i):

        if(i%j==0):
            count +=1
        
        j+=1

    if(count != 2):
        i+=1 
        continue
    print(i,"-> prime number:" )
    i+=1


for i in range(1,31):
    count = 0 
    for  j in range(1,i+1):
        if(i%j==0):
            count +=1 
    if(count !=2):
        continue
    print(i)

#hackerrank challenge (pass)
i = 1 
while(i<=10):
    if(i==5):
        
        pass
    print(i)
    i+=1
    