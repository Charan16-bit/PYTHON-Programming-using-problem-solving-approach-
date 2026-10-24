def second_element_(arr):

    largest = arr[0]

    second = arr[0]

    for i in range(len(arr)):

        if(arr[i] > largest):

            largest = arr[i]

        elif(arr[i]< largest):

            second = arr[i]
    return second,largest

arr = [12, 3, 23, 5, 59, 20]
print(second_element_(arr))




arr1 = [12, 3, 23, 5, 59, 23]

largest = float('-inf')
second = float('-inf')

for num in arr1:

    if(num > largest):

        second = largest 

        largest = num

    elif( num < largest and num > second ):

        second = num 
print(second)
