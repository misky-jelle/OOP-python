class Student:
    school="Akirachix"
    def __init__(self,first_name,second_name,year_of_birth,age,country):
        self.first_name=first_name
        self.second_name=second_name
        self.year_of_birth=year_of_birth
        self.age=age
        self.country=country


    def greet(self):
        return f"Hello{self.name} from {self.country} welcome to {self.school}" 
    def year(self):
        year_of_birth=2022-self.age
        return f"Hello your year of birth is {year_of_birth}"    
    def names(self):
        return f"Hello your name is {self.first_name} {self.second_name}"    

    def initials(self):
        return f"Hello your initials are{self.first_name[0]} {self.second_name[0]}"    
