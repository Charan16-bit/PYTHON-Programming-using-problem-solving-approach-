
# NESTED wHile  LOOP
i = 1

while i <= 3:

    if i == 1:
        print(i, "Monday")

    if i == 2:
        print(i, "Tuesday")

    if i == 3:
        print(i, "Wednesday")

    j = 1

    while j <= 3:

        if j == 1:
            print(i, j, "first hr")

        if j == 2:
            print(i, j, "second hr")

        if j == 3:
            print(i, j, "third hr")

        j += 1

    i += 1 

# fixed rows "***" *3
i = 1 

while (i <=3 ):
    j = 1
    while(j<=3 ):
        print("*",end = "")
        j +=1 
    print()
    i +=1

#🟢 Challenge 2 – Increasing Stars
i = 1
while( i <= 5):
    j = 1
    while(j<= i):
        print("*",end ="")
        j +=1
    print()
    i+=1
#reverse

i = 5
while (i >= 1):
    j = 5
    while(j>=6-i):
        print(j,end ="")
        j -=1
    print()
    i -= 1

### ABCD
i = 5
while (i>=1):
    j = 0 
    while(j<i):
        print(chr(65+j),end="")
        j +=1
    print()
    i -=1

#🟢 Challenge 1 – Fixed Numbers
i = 1
while(i <= 4):
    j = 1
    while(j<=4):
        print(i,end = " ")
        j+=1
    print()
    i+=1

#🟢 Challenge 2 – Growing Numbers
i = 1
while(i <= 5):
    j = 1
    while(j<=i):
        print(i,end ="")
        j+=1
    print()
    i+=1

#🟡 Challenge 3 – Reverse Numbers

i = 5
while(i >= 1):
    j = 5
    while(j >= 6-i):
        print(j,end = "")
        j-= 1
    print()
    i-=1

#🟡 Challenge 4 – Growing Letters
print("#🟡 Challenge 4 – Growing Letters")
i = 1
while(i<=5):
    j = 1
    while(j<=i):
        print(chr(64+j),end ="")
        j+=1
    print()
    i+=1

#🟠 Challenge 5 – Reverse Letters
print("#🟠 Challenge 5 – Reverse Letters")
i = 1
while(i<=5):
    j =1 
    while(j<=6-i):
        print(chr(64+j),end ="")
        j +=1
    print()
    i+=1

#🔴 Challenge 6 – Multiplication Grid
print("#🔴 Challenge 6 – Multiplication Grid")
i = 1

while(i<=4):
    j = 1
    while (j<= 4):
        print(i*j,end =" ")
        j += 1
    print()
    i +=1 
#🔴 Challenge 7 – Continuous Numbers
print("🔴 Challenge 7 – Continuous Numbers")
count = 0
i = 1
while(i <= 5):
    j =1 
    while(j <= i):
        count +=1
        print(count,end = " ")
        j += 1
    print()
    i +=1 
#🔴 Challenge 8 – Prime Numbers
print("#🔴 Challenge 8 – Prime Numbers") 
i = 1
while(i <= 50):
    j = 1
    prime = 0
    while(j <= i):
        if(i % j ==0 ):
         prime += 1
        j += 1            
    if(prime == 2):
        print(i)
    i+=1

#🏆 Boss Challenge – Butterfly Pattern
print("🏆 Boss Challenge – Butterfly Pattern")
i = 1
while( i <= 4):
####right wings,
    j = 1
    while(j<=i):
        print("*",end = "")
        j +=1 

#spaces for each wings
    space = 1
    while(space <= (4-i)* 2):
       print(" ",end ="")
       space += 1 

#left wings
    j = 1
    while(j <= i):
        print("*",end ="")
        j += 1
    print()
    i+=1 


i = 3 
while(i >= 1):
    j = 1
    while(j<=i):
        print("*",end = "")
        j+= 1
    

    space = 1
    while(space<= (4 -i )*2):
        print(" ",end ="")
        space += 1

    j = 1 
    while(j<=i):
        print("*",end = "")
        j+= 1
    print()
    i-=1 