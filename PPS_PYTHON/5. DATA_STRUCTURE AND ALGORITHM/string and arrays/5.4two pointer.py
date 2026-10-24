######## using for loop 

arr = [ 1,2,3,4,56,3]

target = 5

n = len (arr)

for i in range(n):

    for j in range(len(arr) - 1 , i, -1):

        if(arr[i]+arr[j] == target):

            print(arr[i], arr[j],True)

####### using while loop
print("while")
arr1 = [1, 2, 3, 4, 6, 8]

target = 9

left = 0 
right = len (arr)-1

while left < right:
    total = arr1[left] + arr1[right]

    if total == target:
        print(arr[left], arr[right],"=",target)
        break
    elif (total < target):
        left += 1

    else:
        right += 1
