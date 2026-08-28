# BASIC PYTHON OPERATIONS

name = "Swarnit"
age = 19
height = 6.1

print("Name:", name)
print("Age:", age)
print("Height:", height)


user_name = input("\nEnter your name: ")
number = int(input("Enter a number: "))

print("Hello", user_name)
print("Your number is:", number)

a = 10
b = 3

print("\n--- Arithmetic Operations ---")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Power:", a ** b)

print("\n--- Comparison Operations ---")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

x = 10

print("\n--- Logical Operators ---")
print(x > 5 and x < 20)
print(x > 20 or x == 10)
print(not(x > 5))

x = 10

print("\n--- Assignment Operators ---")

x += 5
print("x += 5 :", x)

x -= 2
print("x -= 2 :", x)

x *= 3
print("x *= 3 :", x)

x /= 2
print("x /= 2 :", x)

x //= 2
print("x //= 2 :", x)

x %= 3
print("x %= 3 :", x)

x **= 2
print("x **= 2 :", x)


print("\n--- Bitwise Operators ---")
print("a & b  :", a & b)   
print("a | b  :", a | b)    
print("a ^ b  :", a ^ b)  
print("~a     :", ~a)   
print("a << 1 :", a << 1)   
print("a >> 1 :", a >> 1) 

print("Identity Operators")
print(a is not b)
print(a is b)


print("Membership operators")
print("a" in "apple")




