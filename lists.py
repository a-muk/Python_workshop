x = [1, 2, 3, 4, 5, "abc"]
x.append(6)
x.insert(0, 4)
x.remove("abc")  # removing an element
x.pop(0)  # removing an element at a particular location

print(x[1:3])  # [2,3]
print(x[2:100])
print(x[1::])
print(x[::-1])
print(x)
