#Print multiplication table of a given number
num =int(input("Enter Any Number :"))

for i in range(1,11):
    product=num*i
    print(num,"X",i,"=",product)