def check_upper(s):

    count1 =0

    for i in s:
        if(i.isupper()):
            count1 += 1

    return count1

print(check_upper("PyTHon"))

###

def reverse(s):

    new_str =""
    original = s
    i = len(s)-1

    while(i>=0):
       
        new_str+=s[i]
        i-=1

    if(s==original):
        return True
    else:
        return False
    
    

print(reverse("LEVEL"))


def shift(s1,k):

    new_str =""

    for i in range(len(s1)):

        if(s1[i].isalpha()):
            new_str += chr(ord(s1[i])+k)
        else:

          new_str+= s1[i]
    return new_str

print(shift("AI2026",2))



###Count how many digits are present.

def countdig(s):

    count = 0 

    for i in s:

        if(i.isdigit()):
            count +=1

    return count

print(countdig("AI2026"))

####Q12 (Medium)

#Reverse every second character.

def reverse(s):

    new_str=""
    i=len(s)-1

    while i>= 5:

        new_str += s[i::-2]

        i-=1

    return new_str
print(reverse("PYTHON"))

## Q13 (Hard) Write a function that checks whether an email is valid.
def email(s):

        if("@" in s and s.endswith("gmail.com")):
            return "valid"
        
        return "invalid"
        
print(email("charan@gmail.com"))