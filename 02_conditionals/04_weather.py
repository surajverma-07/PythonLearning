weather = input("Enter Weather sunny/rainy/cloudy ::  ")

weather = weather.lower()

if weather=="sunny":
  activity = "Play Cricket "
elif weather == "rainy":
  activity = "Go for walk "
elif weather == "cloudy":
  activity = "Go for drive"
else :
  print("Jo bola usme se hi type kr ")
  exit()

print(activity)