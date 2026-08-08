a=int(input())
b=int(input())
c=int(input())
d=a*b*c
e=a+b+c
f=d/e
print(d)
print(e)
print(f)
#####################
name = input()
score = int(input())
department = input()

print("name:",name)
print("CGPA:",score/10)
print("DEPT:",department)

###########
n = 947531

original = n

sum = 0
product = 1
largest = 0
smallest = 9
reverse = 0
odd_count = 0
armstrong = 0

while n > 0:

    digit = n % 10

    sum += digit
    product *= digit
    reverse = reverse * 10 + digit
    armstrong += digit ** 3

    if digit > largest:
        largest = digit

    if digit < smallest:
        smallest = digit

    if digit % 2 != 0:
        odd_count += 1

    n //= 10

print("Sum =", sum)
print("Product =", product)
print("Largest =", largest)
print("Smallest =", smallest)
print("Reverse =", reverse)
print("Odd Count =", odd_count)

if reverse == original:
    print("Palindrome")
else:
    print("Not Palindrome")

if armstrong == original:
    print("Armstrong")
else:
    print("Not Armstrong")

# Prime Number

i = 1
factor_count = 0

while i <= original:

    if original % i == 0:
        factor_count += 1

    i += 1

if factor_count == 2:
    print("Prime Number")
else:
    print("Not Prime Number")

# Perfect Number

i = 1
factor_sum = 0

while i < original:

    if original % i == 0:
        factor_sum += i

    i += 1

if factor_sum == original:
    print("Perfect Number")
else:
    print("Not Perfect Number")