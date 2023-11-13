class dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def bark(self):
        print(f"{self.name} barks")
        
#creating objects(instancre) of the dog class
dog1=dog("buddy",5)
dog2=dog("tommy",6)

#accessing attributes and calling methods
print(dog1.name)
dog2.bark()
dog1.bark()
