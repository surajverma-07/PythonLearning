age = input("Provide your age :  ")

age_in_int = int(age)
type_of_age = type(age_in_int)

if age_in_int < 13:
    print("You are a child")
elif age_in_int >= 13 and age_in_int < 20: 
    print("You are a teenager")
elif age_in_int < 60:
    print("You are an adult")
else:
    print("You are a senior" )