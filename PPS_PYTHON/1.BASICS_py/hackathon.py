#Problem 1: Student Registration
student = {
    "name":"charan",
    "age" : 20,
    "cgpa":8.5
}
print(student.get("cgpa"))

#Problem 2: Duplicate Removal
sets = {10,20,30,20,10,40,50,40}
print(len(sets,))

#Problem 3: Product Inventory
list = ["Laptop","Mouse","Keyboard"]
list.append("Monitor")
print(list)

#Problem 4: Security System
security_s = {
    "Username" : "admin",
    "Password" : "python123"
}
print(security_s.get("Password"))

#Problem 5: Reverse Shipment IDs
tuples = (1001, 1002, 1003, 1004 ,1005)
print(tuples[::-1])

#Problem 6: Employee Records
emp ={
    "Name" : "Ravi",
    "Age" : 25,
    "Department" : "IT"
}
emp.update({"Age":26})#emp["Age"] = 26
print(emp)

#Problem 7: Library System
sets_1 = {"Python","java","C++","Python","java"}
print(sets_1)

#Problem 8: String Analytics
p =  "PROGRAMMING"
print(p[0])
print(p[-1])
print(len(p))

#Problem 9: Student Marks
l = [50,60,70,80]
print(sum(l))

#Problem 10 (Hackathon Final Boss)]
emp_name = {"charan"}
skills = {"Python","SQL","Java","Python"}
print("Employee Name:",emp_name)
print("Unique Skills:",skills)
print("Number of Unique Skills:",len(skills))