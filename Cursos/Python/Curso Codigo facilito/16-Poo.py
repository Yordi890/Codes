class Animal:
    
    slogan = "The world is beautiful"
    
    def __init__(self,name,age, sound):
        self.__name=name
        self.__age=age
        self.__sound=sound
        
    @staticmethod
    def say_some_pretty():
        print("Some pretty")
        
    @classmethod
    def say_some_pretty(cls):
        print(cls.slogan)#accediendo a la variable de clase
        
    def say_hello(self):
        print(self.__sound)
        
    def __str__(self):
        return self.__name
        
class Dog(Animal):
    
    def __init__(self,name,age, sound="woof,woof"):
        Animal.__init__(self,name,age,sound)
    
    def say_hello(self):
        print("Woof,woof")
        Animal.say_hello(self)
        
Dog.say_some_pretty()

dog = Dog("Panfilo", 5)

print(dog)

dog.say_hello()
    
    
    

#nota si exite un metodo comun de 2 clases que se esten usando en herencia multiple ejecutara en la primera clase padre 