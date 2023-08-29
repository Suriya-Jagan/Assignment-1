# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

def count_upper_lower(string):
    low_count = 0
    up_count = 0
    for i in string:
        if i.isupper():
            up_count += 1
        elif i.islower():
            low_count += 1
    Upper_count = f"No. of Upper case characters : {up_count}"
    Lower_count = f"No. of Lower case Characters : {low_count}"
    return Upper_count, Lower_count

result = count_upper_lower(input("Enter the string to find the how many upper & lower words: "))
for item in result:
    print(item)
