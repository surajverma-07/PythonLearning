# Count positive number in a list 
# numbers = [1,-2,4,5,-3,-22,-56,4,3,0,34]
numbers = []
print("enter 10 numbers ")
for i in range(0,10):
    num = int(input("enter num "))
    numbers.append(num)

count = 0
for i in numbers:
  if i>0:
    count+=1

print("Positive values count in numbers list is ::  ",count)