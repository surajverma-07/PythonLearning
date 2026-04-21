
from math import sqrt
num = int(input("Enter the number "))
isPrime = True
if num > 1:
  if num == 2 or num == 3 : 
    isPrime = True 
  else:
    for i in range(2,int(sqrt(num))+1):
      if num%i==0 :
        isPrime = False
        break
if isPrime: 
  print(num," is a Prime number ")
else:
  print(num," is not a Prime number ")