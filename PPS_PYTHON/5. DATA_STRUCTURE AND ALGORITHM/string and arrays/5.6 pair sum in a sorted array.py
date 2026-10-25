def pairsumofsortedarray0(arr,target):
    left = 0
    right = len(arr)-1
    while(left<right):
        if(arr[left] + arr [right] == target):
            return(arr[left] , arr[right])
        elif(arr[left] + arr [right] < target):
            left += 1 
        else:
            right -= 1
print(pairsumofsortedarray0([1,2,3,4,6,8],10))




def pairsumofsortedarray(arr1,target1):
    for i in range(len(arr1)):
        for j in range(1+i,len(arr1)):
           if(arr1[i] + arr1 [j] == target1):
                return(arr1[i] , arr1[j])
           
            
print(pairsumofsortedarray([1,2,3,4,6,8],10))