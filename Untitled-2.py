class employee:
    num_employee=0
    raise_amount=1.04
    def __init__(self,first_name,last_name,pay):
        self.first_name=first_name
        self.last_name=last_name
        self.pay=pay
        employee.num_employee+=1
    def fullname(self) :
        print(self.first_name,self.last_name)
    def apply_raise(self):
        self.pay=int(self.pay)*self.raise_amount
    def __repr__(self):
        pass
        return f"Employeed'{self.first_name}','{self.last_name}','{self.pay}'."
    def __str__(self) :
        return f"{self.first_name}-{self.last_name}"
    
    def __add__(self,other):
        return self.pay*


#emp_1=employee("corey","scharler",5000,)
#emp_2=employee("test","user",3000,)
#print(repr(emp_1))
#print(str(emp_1))
print(str.__add__('1','2'))
