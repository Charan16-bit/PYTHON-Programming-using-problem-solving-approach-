##Remove Vowels
def remove_vowels(s):


    new_str =""

    for i in s:

        if(i in "aeiouAEIOU"):
            pass

        else:
            new_str += i
    return new_str

str = input("enter the input :")
print(remove_vowels(str))

##### 🟡 Medium 6.7 Find Character (without find)

def find_ch ( s, c ):
    
    index = 0 
    
    while ( index < len(s)):

        if(s[index] in c):
            print(c,"this is the word that ur looking at ",index)
        
        else:
            pass

        index+=1
    

text1 = input("\n the string u want to enter: ")

find = input( "\n the word u want to find in the string")

find_ch(text1,find)


###6.9 Count Character

def count_ch(s,c):

    count1 = 0

    for i in s:
        if(i == c ):
            count1 += 1

    return count1

str1 = input ("enter the strings ")

find = input("enter the word that ur looking for ")

count = count_ch(str1,find)

print("in", str1 , find , "occurs", count,"time")

#6.11 — Reverse String 🔥

def manual_reverse(s):
    new_str = ""
    
    i = len(s) -1 
    
    while(i>=0):

        new_str += s[i]

        i-=1

    return new_str

str1 = input("enter the string")

print(manual_reverse(str1))


# 6.3 Caesar Cipher

def shift_words(s):

  for i in range(len(s)):
    new_str = s[i]
    print(chr(ord(new_str)+3),end = " ")

str1 = input("enter the string")

(shift_words(str1))

#### this code is same as above one 

def shift_ch(s):

  new_str = ""

  for i in range(len(s)):

    new_str += chr(ord(s[i])+3)
    
  return new_str

str1 = input("the input")
print(shift_ch(str1))