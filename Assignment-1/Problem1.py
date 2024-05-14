# Write a Python program to get the Fibonacci series between 0 to 50

# Note : The Fibonacci Sequence is the series of numbers :
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# Every next number is found by adding up the two numbers before it.
# Expected Output : 1 1 2 3 5 8 13 21 34

user_input = input(int('Enter a number to find a fibonacci series within that: '))
x = 0
y = 1
fibonacci = []
strfib = []

while x <=user_input:
    fibonacci.append(x)
    x, y = y, x + y

for i in fibonacci:
    fib = str(i)
    strfib.append(fib)
    
print(" ".join(strfib))
