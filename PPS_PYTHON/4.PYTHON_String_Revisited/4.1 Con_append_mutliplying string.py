##concation
fname = "charan"
llast = "raj"

print(fname + llast)

###Mutliplying 

s = "***"
print(s*2)

#### append

s = "Raj"

s1 = " RA231100312384"

s = "charan" + s + s1
print(s)
### string immutable 
s = "python"

print(s[0])
###

s2 = "PYTHON"
s2 = "j" + s[1:]

print(s2)

###

course = "python"

course = course[:3] + "j" + course[4:]

print(course)

#🔥 ROUND 3 — PREDICT THE OUTPUT
#1
s = "banana"
print(s.count("an"))

#2

s = "banana"
s = s[:2] + "x" + s[3:]

#3

text = "Python Is Easy"

print(text.lower().replace("easy","fun"))

#4
data = "A,B,C"
x = data.split(",")
print(x)
print(len(x))

#5
letters = ["A","B","C","D","E","G"]
print(" ".join(letters))

#6
s = "123"
print(s.isdigit(),s.isalnum())

###💻 ROUND 4 — CODING CHALLENGE#

name = "charan raj"
print(name.upper().replace(" ","_"))

##2

course_feedback = "python is very easy"

cout = course_feedback.split()
print(cout)
print(len(cout))

#Q23
email = " charan@gmail.com"

if email.find("@") != -1:
    print("valid")

else:
    print("invalid")


#q24

h = "   hello Python  "

print(h.strip())