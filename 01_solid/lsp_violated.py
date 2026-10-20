# Liskov Substitution Principle - Violated

class Account:
    def __init__(self, amount):
        self.amount = amount

    def deposit(self):
        deposited_amount = self.amount
        print(f"{deposited_amount} Amount saved")

    def withdraw(self):
        withdrawn_amount = self.amount 
        print(f"{withdrawn_amount} amount is withdrawn")


class SavingAccount(Account):
    def __init__(self,amount):
        super().__init__(amount)
    
    def deposit(self):
        super().deposit()
    
    def withdraw(self):
        super().withdraw()


class CurrentAccount(Account):
    def __init__(self,amount):
        super().__init__(amount)
    
    def deposit(self):
        super().deposit()
    
    def withdraw(self):
        super().withdraw()


class FixedDeposit(Account):
    def __init__(self,amount):
        super().__init__(amount)
    
    def deposit(self):
        super().deposit()
    
    def withdraw(self):
        raise Exception("Cannot Withdraw from FD")




# money = CurrentAccount(1000)
# money.withdraw()   

money2 = FixedDeposit(1000)
money2.withdraw()