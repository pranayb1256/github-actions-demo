class employee:
    def __init__(self,first_name,last_name,pay):
        self.first_name=first_name
        self.last_name=last_name
        self.pay=pay
    def fullname(self) :
        print(self.first_name,self.last_name)
    
    @property
    def email(self):
        return f'{self.first_name}.{self.last_name}email.com'    
    
    @fullname.setter
     def 

emp_1=employee("john",'smith')
