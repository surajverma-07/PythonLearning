strA = str(input("Enter a string :: "))
rev_str = ""
n = len(strA)-1
for i in range(n,-1,-1):
  rev_str+= strA[i]

print("Reverse string is :: ",rev_str)