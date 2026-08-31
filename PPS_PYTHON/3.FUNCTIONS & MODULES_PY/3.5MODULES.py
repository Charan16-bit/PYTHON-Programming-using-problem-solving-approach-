# 5.11.2 — __name__ (Name of Module)

if __name__ == "__main__":
    print("This runs only when I run this file directly",__name__)

#5.11.3 — Making Your Own Module
def add (a,b):
    return a + b

import maths

print(maths.add(10, 20))


#5.11.4 — dir() Function

import maths 
print(maths.add(23,23))

#Your own module = a separate .py file that you import.


x = 10

print(globals())

def show():
    y = 20
    print(locals())

show()