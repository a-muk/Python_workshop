x = {1: "a", 2: "b", 3: "c"}
print(type(x))
x[4] = "d"
for i in x:
    print(i)

for i in x.values():
    print(i)

for i in x.items():
    print(i)
