import time
print("Jay Shree Ram")
username = "Suraj Kumar Verma"
print(username)

# f = open('filename.py')
# f.readline() -> to read first line, then read next line..upto end of list 
# f is same as iter(f)
# f.__next__() -> this next function return the current line and move to next and at the end it throw StopIteration exception
# however readline also use __next__() internally but bit optimization is done to handle exception so we seen '' instead of exception

# in case of list like myList = [1,2,3,4] iter(myList) != myList
# I = iter(myList) I always point the first memory reference of the list , for iteration __next__() changes it's reference

# next() == __next__() and iter() == __iter__()

# every iteratble object like list , dictionary , range .. can be accessed via I = iter(object) , then next(I).. or I.__next__()