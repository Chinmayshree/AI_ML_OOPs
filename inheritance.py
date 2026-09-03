

class animal:
    
    def __init__(self,name):
        
        self.name=name
    
    def speak(self):
        
        print(f"{self.name} makes the sound")

class Dog(animal):
    
    def speak(self):
        print(f"{self.name} barks")
    
    

ani =animal("Elephant")
ani.speak()

dog = Dog("dog")
dog.speak()
        
       