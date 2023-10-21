#3. Write a python program to square the elements of the list using map() function.
l = [10,15,20,25,30,35,40]
Squared = list(map(lambda i:i**2,l))
print(Squared)

#Method2:Take inputs from user.
input_list = input("Enter the numbers with spaces: ").split()
l = []
for i in input_list:
    i = int(i)
    l.append(i)
Squared = list(map(lambda i:i**2, l))
