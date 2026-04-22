# create a fn to return area and circumference fo a circle given it's radius
import math
def circum_area(r):
    area = math.pi * r **2
    circum = 2 * math.pi * r
    return f"{area:.2f}",f"{circum:.2f}"

a,c = circum_area(5)
print("Area :: ",a," Circumference :: ",c)