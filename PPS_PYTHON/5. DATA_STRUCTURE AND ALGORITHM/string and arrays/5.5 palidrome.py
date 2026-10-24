
arr=47974
reverse = 0 
while arr>0:
    digit = arr % 10 
    reverse = reverse * 10 + digit 
    arr = arr // 10
print(reverse)


arr1 = [4,7,9,7,4]
palidrome = True or False
left = 0 
right = len(arr1)-1

while left < right:
    if(arr1[left] == arr1[right]):
        arr1[left],arr1[right] = arr1[right],arr1[left]
        left+=1
        right-=1

if(arr1 == palidrome):
    print(palidrome)