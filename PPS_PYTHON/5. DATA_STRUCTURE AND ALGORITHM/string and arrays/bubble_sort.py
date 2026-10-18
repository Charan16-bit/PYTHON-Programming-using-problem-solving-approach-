def bubble_sort(arr):
    n = len(arr)

    for i in range(n -1):
        print(arr,i)
        for j in range(n - 1 -i):

            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

    return(arr)

arr = [3,7,5,10,13,2]

print(bubble_sort(arr))