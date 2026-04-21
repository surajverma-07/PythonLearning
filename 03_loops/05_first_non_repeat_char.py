# find the first non repeated character in a string 
str1 = input("Enter any string ::  ")
#sdfkjigdfkfjs -> i and g non repeat , i is 1st -> answer i
n = len(str1)
# for i in range(0,n):
#   isRepeated = False
#   for j in range(i+1,n):
#     if(str1[i]==str1[j]):
#       isRepeated = True
#       break
#   if isRepeated==False:
#      print("First Repeated character is :: ",str1[i])
#      exit()

# print("NA")

for ch in str1:
  if str1.count(ch)==1:
    print("First Repeated Character is :: ",ch)
    break