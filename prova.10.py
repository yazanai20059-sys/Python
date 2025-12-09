from functools import reduce
l=[3, 0, 8, -5, -7]
x = reduce(lambda n1,n2:n1+n2, l)
print(x)


"""l=[3, 0, 8, -15, -7,]
x = list(filter(lambda x:x>0, l))
print(x)
l=[3, 25, 8, 15, 42, 7, 13]
x = list(map(lambda x:x+10, l))
print(x)"""