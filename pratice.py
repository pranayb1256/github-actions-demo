class Dog:
    def __init__(self,name,breed,cost):
        self.name=name 
        self.breed=breed
        self.cost=cost
    def __repr__(self) -> str:
        return f"THE name is {self.name},the breed is {self.breed} ,the cost is {self.cost}"
    def __str__(self) -> str:
        return f"THE name is {self.name},the breed is {self.breed} ,the cost is {self.cost}"    
class Cat(Dog):
    def __init__(self, name, breed, cost):
        super().__init__(name, breed, cost)
    @classmethod
dog_1=Dog("Jimmy","Husky",5000)
dog_2=Dog("Baston","labrador",2000)
cat_1=Cat)