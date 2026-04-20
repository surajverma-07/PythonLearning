n = int(input("Enter a number "))

sum = 0

for i in range (2,n+1,2):
  sum+=i

print("Sum of the even number upto ",n," is =  ",sum)