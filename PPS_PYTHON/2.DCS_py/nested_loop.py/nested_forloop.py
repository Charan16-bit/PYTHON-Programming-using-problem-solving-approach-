for i in range(1,4):
    print("outer:",i)
    for j in range(1,4):
       print("  inner", j)
##
for i in range(1, 3):      
    for j in range(1, 3):
        print(j)

i = 1
while i <= 3:
    j = 1          # Reset every outer iteration
    while j <= 3:
        print(i, j)
        j += 1
    i += 1

for i in range( 1 ,4):
    for j in range ( 1 ,11):
        print(i,"x",j,"=",j*i)

###1 Fixed rows & fixed columns (***)
for i in range( 1, 4):
    for j in range(1,4):
        print("*",end=" ")
    print()
#
for i in range(1,4):
    for j in range(1,i+ 1):
        print("*")
    print()

for i in range(1, 4):
    for j in range(1, 4):
        print(i)
    print()

#🏆 Q1 – Cinema Seats

#Print 3 rows with 4 seats in each row.
for i in range ( 1, 4):
    for j in range(1,5):
      print("seats",end = " ")
    print()

#🏆 Q2 – Staircase Each floor has one more step than the previous.
for i in range(1,4):
    for j in range(1,i + 1):
       print("steps",1*j,end = " ")
    print()
print("/a")
#🏆 Q3 – Student Roll Numbers
for i in range(1,5):
    for j in range(1 , i + 1):
        print("class roll :",0+j,end = " ")

    print()

# 🏆 Q4 – Countdown Blocks

for i in range (1,5):
    for j in range ( 4, i- 1,-1) :
        print("*",end = " ")
    print()

#🏆 Q5 – Bus Seats
for i in range ( 1, 5):
    for j in range ( i , 5):
        print("seats:",0 + j, end =" ")
    print()

#🏆 Q6 – VIP Queue
for i in range (1,5 ):
    for j in range ( i,5):
        print("VIP member:",i ,end = " ")
    print()

#🏆 Q7 – Reverse Countdown
for i in range( 1, 5):
    for j in range( 4, i -1,-1):
        print("BACKWARD:",j,end = " ")
    print()

#🏆 Q8 – Hotel Floors
for i in range ( 4, 0 ,-1):
    for j in range( 1 , i + 1):
        print("each flr:", j ,end = " ")
    print()

#q🏆 Q9 – Reverse Entry

for i in range(4,0,-1):
    for j in range (i,5):
        print(j,end = " ")
    print("next flr")

#🏆 Q10 – Final Boss
letter = "ABCD"
for i in range ( 1, 5):
    for j in range( i,5):
     print(letter[i-1],end = "")
    print()

#####
# Q1 - Fixed Number Pattern
for i in range ( 1, 4):
    for j in range( 1, 4):
        print(j,end = " ")
    print()
print("NEXT QUESTION")

## Q2 - Repeated Number Triangle
for i in range( 1, 5):
    for j in range( 1, i + 1):
        print(i,end = " ")
    print()
print("NEXT QUESTION")
# Q3 - Multiple Multiplication Tables
# Print multiplication tables from 2 to 5.

for i in range ( 2, 6):
    for j in range(1,11):
        print(i,"x",j,"=",i*j)
print("NEXT QUESTION")
# Q4 - Factors of Multiple Numbers
# Print all factors for numbers from 1 to 10.

for i in range (1,11):
    print(i,":",end=" ")
    for j in range(1,i+1):
        if(i % j == 0 ):
            print(j,end=" ")
    print()
print("NEXT QUESTION")
## Q5 - Prime Numbers in a Range
# Print all prime numbers between 1 and 30.

for i in range(1,31):
    count = 0
    for j in range(1,i+1):
     if (i % j == 0):
            count += 1
    if(count == 2 ):
     print(i)  

## Q6 - Diamond Number Pattern

for i in range( 1, 6):
    for j in range ( 1, i+1 ):
        print(j,end ="")
    print()
for m in range(5,0,-1):
    for k in range(1, m+1):
     print(k,end = "")
    print()
    
    ###########
for i in range(1,4):

    if i == 1:
        print(i, "Monday")

    if i == 2:
        print(i, "Tuesday")

    if i == 3:
        print(i, "Wednesday")

    for j in range(1,4):

        if j == 1:
            print(i, j, "first hr")

        if j == 2:
            print(i, j, "second hr")

        if j == 3:
            print(i, j, "third hr")