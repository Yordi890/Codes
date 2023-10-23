class Cat:
    
    def __init__(self,name:str = "este es mi nombre")-> None:
        self.__name=name
        
    def __str__(self):
        return self.__name