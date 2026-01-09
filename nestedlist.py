nestedlist = [[8,6,4],[4,5,6],[7,8,9]]
print(nestedlist)
print(nestedlist[0][1])

nestedlist.sort()
print(nestedlist)

nestedlist.sort(reverse=True)
print(nestedlist)

stringlist = [["dog","elephant","frog"],["apple","banana","cherry"],["grape","honeydew","kiwi"]]
stringlist.sort()
stringlist.sort(reverse=True)
print(stringlist)

stringlist.pop(2)
print(stringlist)