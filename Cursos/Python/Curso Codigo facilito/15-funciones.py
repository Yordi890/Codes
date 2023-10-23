def function1(default="some",*multiple,**kargs):
    print(default)
    for i in multiple:
        print(i)
    print(kargs)
    
function1(default="lazaro",  first=True, second=False)
    
animal = "Lion"

def showanimal():
    animal="wolf"
    print(animal)
    
print(animal)    

func = lambda x: x*1.8+32 
print(func(32))

def function2():
    def function3():
        print(list(i for i in range(10)))
    return function3

def decorator(func):
    def new_funcion():
        print("********")
        func()
        print("********")
    return new_funcion
    
@decorator
def function4():
    print(list(i for i in range(10)))
    

function4()

def function5():
    for i in range(10):
        yield i
        
print(i for i in function5())# por alguna razon que escapa a mi comprension asi no funciona

for i in function5():
    print(i)
