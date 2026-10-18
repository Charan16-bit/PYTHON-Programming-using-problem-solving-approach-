def second_element_(arr):

    largest = arr[0]

    second = arr[0]

    for i in range(len(arr)):

        if(arr[i] > largest):

            largest = arr[i]

        elif(arr[i]< largest):

            second = arr[i]
    return second

arr = [12, 3, 23, 5, 59, 23]
print(second_element_(arr))