class employee:
    num_employee=0
    raise_amount=1.04
    def __init__(self,first_name,last_name,pay) -> None:
        self.first_name=first_name
        self.last_name=last_name
        self.pay=pay
        employee.num_employee+=1
    def fullname(self) :
        print(self.first_name,self.last_name)
    def apply_raise(self):
        self.pay=int(self.pay)*self.raise_amount
    def __repr__(self):
        return f"Employeed '{self.first_name}','{self.last_name}','{self.pay}'."
    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount=amount
    @classmethod
    def from_String(cls,emp_str):
        first,last,pay=emp_str.split("-")
        return cls(first,last,pay)
    @staticmethod
    def fs_workday(day):
        if day.weekday() ==5 or day.weekday() == 6:
            return False
        else:
            return True

class Developer(employee):
    raise_amount=1.10
    def __init__(self,first_name,last_name,pay,prog_language) -> None:
        super().__init__(first_name,last_name,pay)
        self.prog_language=prog_language
class Mananger(employee):
        def __init__(self,first_name,last_name,pay,employees=None) -> None:
            super().__init__(first_name,last_name,pay)
            if employee is None:
                self.emloyees=[]
            else:
                self.employees= employees
                
        def add_emp(self,emp):
            if emp not in self.employees:
                self.employees.append(emp)

        def remove_emp(self,emp):
            if emp in self.employees:
                self.employees.remove(emp)

        def print_emps(self):
            for emp in self.employees:
                print("-->",emp.fullname())

           
dev_1=Developer("corey","scharler",5000,"python")
dec_2=Developer("test","user",3000,"java")

mgr_1=Mananger("sue","smith",90000,[dev_1])
mgr_1.print_emps()
mgr_1.add_emp(dec_2)
mgr_1.print_emps()