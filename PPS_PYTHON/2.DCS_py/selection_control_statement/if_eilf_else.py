#Problem 1: Skill Verification
name = "CHARAN"
skills = "python"

if len(name) == 6 and "python" in skills:
   print("Selected")
else:
    print("Rejected")

#Problem 2: Placement Round
cgpa = float(input("enter the CGPA:"))

if cgpa >= 9:
    print("Top candidate")
elif cgpa >= 8:
    print("Eligible")
else:
    print("Not Eligible")

#Problem 3: Unique Skills
skills = {"Python","SQL","Python","Java"}
print(len(skills))

#Problem 4: Student Analytics
name = "CHARAN"
print(name[0])
print(name[-1])
print(len(name))

#Problem 5: Marks Evaluation
list = [90,85,95]

if(sum(list)>270):
    print("Excellent")

elif(sum(list)>250):
    print("Good")

else:
    print("Average")

#Problem 6: Dictionary Validation
dict = {
    "name" : "Charan",
    "cgpa" : 8.5
}
if dict ["cgpa"] >=  9:
    print("Topper")
elif dict["cgpa"] >= 8:
    print("Eligible")
else:
    print("Average")

#Problem 7: Nested Validation
name = "CHARAN"
if len(name) == 6:
    if name[-1] == "N":
        print("vaild")
    else:
        print("Invalid")
else:
    print("Invaild")
    
#Problem 8: Final Boss
Name  = "CHARAN"
CGPA  = 8.5
Skill = "Python"
Marks = [90,85,95]

if len(Name)==6:
    if Skill == "Python":
        if sum(Marks) >250:
            if CGPA >= 8:
                print("Selected")
else:
    print("Rejected")

