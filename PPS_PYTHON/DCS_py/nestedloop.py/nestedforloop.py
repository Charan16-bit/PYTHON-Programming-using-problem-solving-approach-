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