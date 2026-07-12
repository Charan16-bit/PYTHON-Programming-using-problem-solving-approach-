#Problem 1: Collection Counter.len()
list = [10,20,30]

tuples = (40, 50, 60, 70)

sets = {10, 20, 20 ,30, 30 }

name = "CHARAN"

student = {
    "name": "charan",
    "age" : 20,
    "cgpa": 8.5
}
print(len(list))
print(len(tuples))
print(len(sets))
print(len(student))

#Problem 2: Reverse Everything slice of string.(::-1)
list_1 = [10,20,30,40]

tuples_1 = ( 50, 60, 70)

nm = "CHARAN"

print(list_1[::-1])

print(tuples_1[::-1])

print(nm[::-1])
print("\a")
#Problem 3: Dictionary Updater

student_1 = {
    "name": "Charan",
    "age" : 20
}
student_1["age"] = 21
print(student_1)
print("\a")
#Problem 4: Collection Membership

list1 = [10,20,30,40]

tuples1 = (10, 20, 30)

sets1 = {10, 20, 20 ,30,}

num1 = {
    "num" : str(20)
}

print("num" in num1)
print(10 in list1)
print(10 in tuples1)
print(10 in sets1)
print("\a")
#Problem 5 (Most HackerRank-like)

course = "PYTHON"

print(course[0])
print(course[-1])
print(course[::-1])
print(len(course))

print("\a")

numbers = [30,43,54,65,57,10,20]

num2 = numbers[1:4]

num2.sort()

print(num2)

print("\a")
student = {
    "name":"Charan",
    "age":20
}
student["reg on"] = "RA2311"
print(student)
