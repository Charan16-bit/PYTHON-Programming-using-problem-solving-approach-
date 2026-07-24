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

####### find the factor
for i in range(1,6):
    print(i,":",end =" ")
    for j in range(1,i+1):
        if(i % j == 0):
            print(j,end =" ")
    print()
print("""""")
#prime number

for i in range ( 1,11):
    count = 0
    for j in range( 1 , i + 1):
        if ( i % j ==0 ):
            count += 1
    if (count==2):
        print(i)