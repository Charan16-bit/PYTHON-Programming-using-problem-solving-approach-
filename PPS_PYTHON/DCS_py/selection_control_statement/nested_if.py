ps_code = int(input("enter ur Code:"))
if ps_code > 78 and ps_code < 80:
    print("Access Granted")
      
if ps_code <= 77 or ps_code >= 99: 
    print("Nee yaaruna therila")

#Problem 1: Placement Check

cgpa = float(input("Enter the CGPA:"))
arrear = int(input("Enter the Arrear:"))
if cgpa >= 8:
    
    if arrear == 0:
        print("Eligible")

#Problem 2: Placement Check

cgpa1 = float(input("Enter the CGPA:"))
arrear2 = int(input("Enter the Arrear:"))

if cgpa1 >= 7:
    if arrear2 == 0:
        print("not eligible")

#Problem 3: Login System

username = str(input("Enter the username:"))
password = str(input("Enter the Password:"))

if username == "charan":
    if password == "python":
        print("Login Success")

#Problem 4: Login System

username1 = str(input("Enter the username:"))
password2 = str(input("Enter the Password:"))

if username1 == "charan":
    if password2 == "python":
        print("Login Succed")

    else:
        print("login failed")

#Problem 5: Scholarship
cgpa = float(input("Enter ur cpga:"))
attendance = int(input("Enter ur attendance:"))

if cgpa >= 9:
    if attendance >= 90:
        print("Scholarship Approved")

else:
    print("Not Scholarship Approved")

# Problem 6: Scholarship

cgpa = float(input("Enter ur cpga:"))
attendance = int(input("Enter ur attendance:"))

if cgpa >= 9:
    if attendance >= 90:
        print("Scholarship Approved")

    else:
        if attendance <= 89:
            print("Scholarship Rejected")

#Problem 7: Club Membership

student = str(input()) 
if "python" in student and "SQL"in student :
        print("Member Accepted")

#Problem 8: Club Membership

student = str(input()) 
if "python" in student and "SQL"in student :
        print("Member Accepted")

else:
    print("Member Rejected")

#Problem 9: Final Boss
name_length = (input("enter the length:"))
CGPA1 = float(input())
arrears2 = int(input())
if len(name_length)== 6:
    if CGPA1 >=8:
        if arrears2 == 0:
            print("Selected")

#Problem 10: Final Boss
name_length = (input("enter the length:"))
CGPA1 = float(input())
arrears2 = int(input())
skills = input()
if len(name_length)== 6:
    if CGPA1 >=8:
        if arrears2 == 0:
            if skills == "python":
             print("Selected")

