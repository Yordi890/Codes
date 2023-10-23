l = [1,2,3,4] if False  else (1,2,3,4)

for i, v in enumerate(l):
    print(i, v)
else:
    print("End loop")