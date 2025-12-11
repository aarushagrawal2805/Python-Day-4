# Calculate sum of all numbers from 1 to a given number
sum = 0
s = int(input("Enter a number:"))
# Using while loop
'''while i <= s:
    sum += i
    i += 1
print("Sum of Number", s, "is :", sum)'''

# using for loop
for i in range(0, s + 1):
    sum += i
print("Sum of Number", s, "is :", sum)
