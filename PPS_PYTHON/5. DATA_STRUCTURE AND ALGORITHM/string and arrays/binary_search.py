def binary_search(arr,target):
    left = 0 #0,2
    right = len(arr)-1#6,2

    while ( left <= right ):

        mid = (left+right) // 2
        print(mid)
        if( arr[mid] == target):
            return ("answer",mid)
        elif arr[mid] < target:
           left = mid + 1
        else:
            right = mid - 1
    return - 1

arr = [3, 8, 12, 17, 23, 31, 42]

print(binary_search(arr,12))
print(len(arr))



arr = [12,3,23,5,59]

temp = 0 

for i in range(len(arr)-1):
    if(arr[i]>arr[i+1]):
        
        temp = arr[i]
    elif temp <arr[i-1]  or arr[i+1]:
        temp = arr[i]
        
print(temp)