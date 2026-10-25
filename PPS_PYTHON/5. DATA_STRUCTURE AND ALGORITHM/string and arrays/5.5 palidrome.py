### ordinary sum of reverse the number 
arr=47974
reverse = 0 
while arr>0:
    digit = arr % 10 
    reverse = reverse * 10 + digit 
    arr = arr // 10
print(reverse)

### used for swapped elelmet if it is same as in same side (left , right ) then palidrome or not
arr1 = [4,7,9,7,4]
palidrome = True 
left = 0 
right = len(arr1)-1

while left < right:
    if(arr1[left] == arr1[right]):
        arr1[left],arr1[right] = arr1[right],arr1[left]
        left+=1
        right-=1

if(arr1 == palidrome):
    print(palidrome)

########## THis is the real paildrome 

arr = [1,2,3,4,3,2,1]
left = 0
right = len(arr)-1
palidrome = True

while(left < right):
    if arr[left] != arr[right]:
        palidrome = False
        break 
    left +=1 
    right -=1

print(palidrome,"orginally")

def is_palidrome(items):

    left = 0 ;right = len(items)-1
    while(left<=right):
        if(items[left]!=items[right]):
            return False
        left += 1
        right -=1
    return True
print(is_palidrome([1,2,3,4,3,2,1]))
