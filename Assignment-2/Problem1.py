# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

tuples = int(input("Enter the number of tuples: "))
l = []
for i in range(1, tuples+1):
    l2 = []
    tup = input(f"Enter the 1st ele in tuple for list {i}: ")
    tup1 = input(f"Enter the 2nd ele in tuple for list {i}: ")
    t = (tup,tup1)
    l.append(t)
    
for i in range(len(l)):
    for j in range(i+1, len(l)):
        if l[i][1] > l[j][1]:
            l[i], l[j] = l[j], l[i]
print(l)
