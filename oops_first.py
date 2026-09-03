class employee:
    #special method/magic methd/dender method
    def __init__(self,id1,name,department,salary):
        print("started executing attributes/data")
        self.__city ='Pune'
        self.id=id1
        self.name=name
        self.department=department
        self.salary=salary
        print("Atrributes or data initiated automantically")
    def get_name(self):
        return self.__city
    def set_name(self,value):
        self.__city=value
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
print(chinmayV._employee__city)  
print(chinmayV.get_name())
chinmayV.set_name('Hyd')
print(chinmayV.get_name())