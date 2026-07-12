#HackerRank Challenge 1: Student Record
stu = {
    "name":"Charan",
    "age": 20,
    "cgpa" : 8.5
}
print(stu.get("age"))
print("\a")

#HackerRank Challenge 2: Unique Elements
sets = {10,20,20,30,40}
print(len(sets))
print("\a")

#HackerRank Challenge 3: Reverse Collection
tuples =(10,20,30,40,50)
print(tuples[::-1])
print("\a")
#HackerRank Challenge 4: List Manipulation

lists = [10,20,30]
lists.append(40)
lists.insert(1,99)
lists.remove(20)
print(lists)

#HackerRank Challenge 5: Dictionary Update\
stu1 ={
    "name":"Charan",
    "age": 20
}
stu1["age"] = 21 #stu1.update({"age":21})
stu1.update({"city":"Chennai"})
print(stu1)
print("\a")

#HackerRank Challenge 6 (Tricky)
list1 = [10,20]   #[10,20],([30,40]) so 3 last list are same lenght which is the paratheses 
list1.append([30,40])
print(len(list1),)
print("\a") 

#HackerRank Challenge 7 (Very Common)
tuples1 = (10,20,10,30,10)
print(tuples1.count(10))
print("\a")

#HackerRank Challenge 8 (Dictionary)
d = {
    "name":"charan"
}
print(d.get("cgpa"))