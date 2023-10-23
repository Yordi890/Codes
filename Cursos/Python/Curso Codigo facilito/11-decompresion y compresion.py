tuple1 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
zero, one, *all = tuple1

print(zero)
print(one)
print(all)

objectzip = zip(tuple1, list)

print(tuple(objectzip))