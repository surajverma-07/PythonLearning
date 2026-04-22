def sum_all(*args):
    print(args)
    # print("Type of *args :: ",type(args)) -> tuple

    for i in args:
        print(i*2)
    return sum(args)

# print(sum_all(1,2,3))
print(sum_all(3,4,6,7,8,8))
