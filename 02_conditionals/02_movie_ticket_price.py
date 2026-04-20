age = int(input("What is your age ? : "))
isWed = input("Is today is wednesday y/n ? :  ")

# if age<18:
#   price = 8
# else:
#   price = 12

price = 12 if age>=18 else 8
if isWed=='y' or isWed=='Y':
   price -= 2

print("movie ticket price is :: ", price);