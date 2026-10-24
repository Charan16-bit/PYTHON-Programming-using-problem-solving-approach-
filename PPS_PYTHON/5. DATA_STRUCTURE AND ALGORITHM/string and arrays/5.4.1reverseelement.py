arr = [10,20,30,40,50,60]

arr1=[]

for i in range(len(arr)-1,-1,-1):
     arr1.append(arr[i])
     
print(arr1)

############ 

arr3 = [100,90,80,70,60,50,40]
left = 0 
right  = len(arr)
while left < right :
     arr3[left],arr3[right] = arr3[right],arr3[left]
     left = left + 1
     right = right -1

print(arr3)
      
arr4 = [7,2,9,4,1]

for i in range(len(arr4)):
     for j in range(i,0,-1):
          if arr4[j] < arr4[j-1]:

               arr4[j],arr4[j-1] = arr4[j-1],arr4[j]

print(arr4)


n1 = 10 
reverse = n1 % 10
n1 = n1//10
print(n1)