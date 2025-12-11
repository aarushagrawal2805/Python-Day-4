#Count the total number of digits in a number
count =  0
num=int(input("Enter any Number :"))
while(num!=0):
    num=num//10 #Reduce Number from last digit
    count+=1
print(count)