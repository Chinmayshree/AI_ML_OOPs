class employee:
    #special method/magic methd/dender method
    def __init__(self,id,name,department,salary):
        print("started executing attributes/data") 
        self.id=id
        self.name=name
        self.department=department
        self.salary=salary
        print("Atrributes or data initiated automantically")
    
    def travel(self,destination):
        
        print("travel method is called manually ")
        print(f"{self.name} is travelling to {destination}")
#creating an instance or Ojbject of class
chinmayV = employee(101,"Hari","II",125000)
#printing the attributes
print(chinmayV.salary)
print(chinmayV.name)
# #calling the functions/Method
chinmayV.travel("UK") 
print(type(chinmayV))  
print(type(chinmayV.name))     