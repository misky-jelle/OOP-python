class Bank:
    name:"Customers"
    def __init__(self,name,money,location,balance,):
        self.money=money
        self.name=name
        self.location=location
        self.balance=balance

    def deposite(self):
        self.balance+=self.money
        return f"Hello your deposited{self.balance}" 

    def withdrawal(self):
        self.balance-=self.money
        return f"Hello your withdrawal is {self.balance}"       
