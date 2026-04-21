# factorial of the given number using while loop
num = int(input("Enter a number below 100 :: "))
fact = 1
n = num
while num>1:
  fact *= num
  num -= 1
print("Factorial of ",n," is = ",fact)