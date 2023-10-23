def function1(default="some",*multiple,**kargs):
    print(default)
    for i in multiple:
        print(i)
    print(kargs)
    
function1(default="lazaro",  first=True, second=False)

# comentario de rama temp linea 9

animal = "Lion"

def showanimal():
    animal="wolf"
    print(animal)
    
print(animal)    

func = lambda x: x*1.8+32 

print(func(32))
