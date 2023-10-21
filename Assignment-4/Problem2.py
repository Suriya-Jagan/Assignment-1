#2. Write a python program to triple all numbers of a given list of integers. Use python map.
l = [10,15,20,25,30,35,40]
triple = list(map(lambda i:i*3,l))
print(triple)

#Method2:Take inputs from user.
input_list = input("Enter the numbers with spaces: ").split()
l = []
for i in input_list:
    i = int(i)
    l.append(i)
triple = list(map(lambda i:i*3, l))
print(triple)