# Liskov Substitution Principle - Followed
from abc import ABC, abstractmethod


class NonWithdrawAccount(ABC):
    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    def deposit(self):
        pass


class WithdrawAccount(NonWithdrawAccount):
    def __init__(self, amount):
        self.amount = amount

    def deposit(self):
        deposited_amount = self.amount
        print(f"{deposited_amount} Amount saved")

    def withdraw(self):
        withdrawn_amount = self.amount
        print(f"{withdrawn_amount} amount is withdrawn")


# class SavingAccount(WithdrawAccount):
#     def __init__(self, amount):
#         super().__init__(amount)

#     def deposit(self):
#         super().deposit()

#     def withdraw(self):
#         super().withdraw()

# other wasy to write this if no overwrite needs to occurs

class SavingAccount(WithdrawAccount):
    pass

class CurrentAccount(WithdrawAccount):
    def __init__(self, amount):
        super().__init__(amount)

    def deposit(self):
        super().deposit()

    def withdraw(self):
        super().withdraw()


# class CurrentAccount(WithdrawAccount):
#     pass


class FixedDeposit(NonWithdrawAccount):
    def __init__(self, amount):
        super().__init__(amount)

    def deposit(self):
        super().deposit()


rupees = SavingAccount(500)
rupees.deposit() # 500 Amount saved

money = CurrentAccount(1000)
money.withdraw() #1000 amount is withdrawn

money2 = FixedDeposit(1000)
money2.withdraw()  # attribute error
