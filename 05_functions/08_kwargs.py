# def print_kwargs(power,name):
    # print("Name :: ",name," Power :: ",power)


def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : ",f"{value}")


print_kwargs(name="Shaktiman",power="lazer")
print_kwargs(name="Shaktiman",power="lazer",enemy="Dr Jaikaal")
