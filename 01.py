a = [1, 2, 3]
b = a[:]

print(id(a))
print(id(b))
# a[:] = a[::-1]
# print(a)

a = [1, 2, 3, 4]
print(id(a))
print(id(a[:]))
a.remove(2)
print(a)
print(id(a))
print("-----")
print(id([1, 2]))
print(id([1, 2]))

