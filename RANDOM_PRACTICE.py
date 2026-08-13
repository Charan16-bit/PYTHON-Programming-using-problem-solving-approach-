i = 1
while(i<=4):

    j = 1
    while(j<=i):
     print("*",end="")
     j+=1

    space = 1
    while(space<=(4-i)*2):
       print(" ",end = "")
       space += 1

    j = 1
    while(j<=i):
       print("*",end="")
       j+=1
    print()
    i+=1
       
i = 3
while(i>=1):
   
    j=1
    while(j<=i):
      print("*",end ="")
      j+=1

    space = 1
    while(space<=(4-i)*2):
       print(" ",end = "")
       space+=1

    j =1
    while(j<=i):
       print("*",end = "")
       j+=1
    print()
    i-=1


    
for i in range(1,4):
   
   for j in range(1,i+1):
      print("*",end="")
   print()

n = 9
def strong_num(n):
   original = n
   total = 0
   while n > 0:
      
      square = n * n 
      digit = square % 10
      square = square + digit
      square //= 10

   if( total == original):
    return total
   
x = strong_num(n)
print(x)

      
