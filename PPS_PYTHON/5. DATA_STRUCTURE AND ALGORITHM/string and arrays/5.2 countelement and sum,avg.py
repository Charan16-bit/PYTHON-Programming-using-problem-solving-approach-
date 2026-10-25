def count_element(arr):

    odd = 0 

    for i in range(len(arr)):

        if(arr[i] % 2 != 0):
            odd = odd + 1
    return odd

arr = [2,5,7,8,11,14,19]
print(count_element(arr))


def sum_avg(arr1):

    sum = 0
    avg = 0

    for i in range(len(arr1)):

        sum = sum + arr1[i]

    avg = sum / len(arr1)
    return sum,avg
    
arr1 = [10,20,30,40,50]
print(sum_avg(arr1))