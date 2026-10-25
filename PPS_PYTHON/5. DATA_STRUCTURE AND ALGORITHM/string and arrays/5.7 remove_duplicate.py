def duplicates_remove(arr):
    if len(arr) == 0:
       return 0 
    
    i = 0 
    for j in range(1,len(arr)):
       if(arr[j] != arr[i]):
          i+=1
          arr[i] = arr[j]
          pass
    return i+1

arr = [1, 1, 2, 2, 3, 4, 4]
k = duplicates_remove(arr)

print(k)       # 4
print(arr[:k]) # [1, 2, 3, 4]