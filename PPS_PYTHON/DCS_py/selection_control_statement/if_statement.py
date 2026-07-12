#simple 
x = 10 

if x >= 2:
    x = x + 3

print(x)

#question2 voting eligible 
age = int(input("Enter  Age:"))

if age >= 18:
    print("Eligible to Vote:")
    
print("not eligible")
print("\a")

#Example 3: Positive Number

num = int(input("Enter a number: "))

if num > 0:
    print("Positive Number")
          
print("\a")
#Example 4 (Character Check)
ch = input("Press any key:")

if ch.isalpha():
   print("Alphabet")

if ch.isdigit():
    print("Number")

if ch.isspace():
    print("White space")

