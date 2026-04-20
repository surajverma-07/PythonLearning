year = int(input("Enter the year :: "))

if year%400 == 0:
  leap = True
elif year%4==0 and year%100 != 0:
  leap = True
else:
  leap = False

print("year ",year," is a leap year ") if leap else print("year ",year," is not a leap year ")