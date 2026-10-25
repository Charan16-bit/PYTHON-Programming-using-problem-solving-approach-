def duplicates_remove(arr):
    if len(arr) == 0:
       return 0 
    arr1 = []
    i = 0 
    for j in range(1,len(arr)):
       if(arr[j] != arr[i]):
          i+=1
          arr1.append(arr[j])
          pass
    return i+1

print(duplicates_remove([1,1,2,2,3,4,4]))