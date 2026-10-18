def largestelement(arr):

    largest = arr[0]

    for i in range(1,len(arr)):

        if(arr[i] > largest):

            largest = arr[i]
    return largest
arr = [12,3,23,5,59]
print(largestelement(arr))


def smallest_element(arr1):

    smallest = arr1[0]

    for i in range (1,len(arr1)):

        if(arr1[i] < smallest):

            smallest = arr1[i]

    return smallest

arr1 = [14,7,22,-3,9,5]
print(smallest_element(arr1))      

