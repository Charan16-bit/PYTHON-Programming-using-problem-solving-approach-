# 11

s = "hello"

s = "y" + s[1:]

print(s.upper())

##Q13 — Remove Vowels (20)

def role (s):
    
    new_str = ""

    for i in s:
        if(i in "aieouAIEOU"):
            pass

        else:
            new_str+= i 
    
    return new_str

str1 = input("remove vowels")

print(role(str1))

#Q14 — Caesar Cipher (20)

def shift (s):

    for i in range(len(s)):

        new_str = s[i]

        print(chr(ord(new_str)+2),end = "",)
    
str2 = input("Q14 — Caesar Cipher ")
shift(str2)

#### debug 

s = "python"

for i in range(len(s)):
    print(s[i].upper(),end="")

#### reverse

def reverse(s):

    result =""
    i = len(s) -1

    while i>= 0:

        result += s[i]

        i-=1
    
    return result

str1 = input("the string will be reversed in the order of this following problem")

print(reverse(str1))

print("/n")

#Q13 — Reverse String (20)

def reverse1(s):

    result1 =""
    i = len(s) -1

    while i>= 0:

        result1 += s[i]

        i-=1
    
    return result1

str2 = input("the string will be reversed in the order of this following problem")

print(reverse(str2))

##Q14 — Caesar Cipher V2 (20)

def shift1(s,k1):

    new_str1 = ""
    
    for i in range(len(s)):
         
         new_str1 += chr(ord(s[i])+k1)

    return new_str1

str0 = input("the string reverse the give input for second version fo caesar cipher")
k1 = int(input("for the shift"))
print(shift1(str0,k1))####


#####
course = "PyTHon"
print(course.count(course))