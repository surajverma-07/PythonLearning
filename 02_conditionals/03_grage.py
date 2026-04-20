score = int(input("enter your score ::  "))

if score > 100:
  print("Please verify your grade again !")
  exit()
if score >= 90:
  print("Grade A")
elif score >= 80:
  print("Grade B")
elif score >=60:
  print("Grade C")
elif score >=45:
  print("Grade D")
else:
  print("Fail")