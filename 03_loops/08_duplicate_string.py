list1 = ["anar","banana","milk","grapes","banana","eko"]

setList = set()

for li in list1:
  if li in setList:
    print("duplicate string is :: ",li)
    break
  else:
    setList.add(li)