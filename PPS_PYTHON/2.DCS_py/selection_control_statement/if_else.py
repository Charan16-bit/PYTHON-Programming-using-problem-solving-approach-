#Question 1 (Voting Eligibility)
age = int(input("Enter ur age:"))
if (age >= 18):
    print("Your Eligible To Vote:")
else:
    yrs = 18 - age
    print("you have to wait for anothor",str(yrs), "to cast your vote")

#Question 2 (Larger Number)
a = int(input("enter the value of a:"))   
b = int(input("enter the value of b:"))  
if (a > b):
    print("Largest number is a :",a)
else:
    print("Largest number is b :",b)

#Question 3 (Even or Odd)
num = int(input("Enter the number:"))
if (num%2 == 0):
    print("Even")
else:
    print("Odd")

#Question 4 (Character Conversion)
ch = input()
if(ch>='A' and ch <= 'Z'):
    ch = ch.lower()
    print("If it is uppercase, convert it to lowercase and print it."+ ch)

else:
    ch = ch.upper()
    print("If it is lowercase, convert it to uppercase and print it."+ ch)

#Question 5 (Employee Bonus)
ch = input("Enter the sex of employee(m or f):")
sal = int(input("Enter the Salary:"))
if ch=='m':
    bonus = 0.05*sal

else:
    bonus = 0.10*sal
amt_to_be_paid = sal+bonus
print("Salary = ",sal)
print("bonus = ",bonus)
print("***********************")
print("Amount to be paid (Salary + Bonus)",amt_to_be_paid)