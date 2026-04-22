# username = "outerfunction"

# def func1():
#   username = "innerFunc1"
#   print(username)

# print(username)
# func1()

x = 99
# def func2(y):
#    z = x + y
#    return z
# res = func2(1)
# print(res)

# conclusion of above is inner most block has aaccess to outer but outer doesnot has access of inner

# def func3():
#   # x = 88
#   # to change global value use below but do not do it
#   global x
#   x = 10
# func3()
# print(x)

# def f1():
#   x = 88
#   def f2():
#     print(x)
#   return f2
# if we use variable at any level then it search for it by climbing in outer level from current level
# myResf2 = f1()
# myResf2() 

def chaicoder(num):
  def actual(x):
    return x ** num
  return actual

squre = chaicoder(2)
cube = chaicoder(3)
print(squre)
print(cube)
print(squre(4))
print(cube(3))