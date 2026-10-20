# Open/Closed Principle

from abc import ABC, abstractmethod

""" bad violating OCP
in this assume if in future u need to add more payment_type like paypal then u would have to write a lot of these if elif, which means u are modifying the class which is bad
"""


class PaymentService1:
    def __init__(self, payment_type, amount):
        self.payment_type = payment_type
        self.amount = amount

    def pay(self):
        if payment_type == "razorpay":
            pass
        elif payment_type == "stripe":
            pass
        else:
            pass


"""

below is the correct implementation of OCP an abstract class which is then inherited by child class, so there can be n no. of classes 
"""

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class Razorpay(Payment):
    def pay(self, amount:int):
        print(f"Razorpay functional, with {amount}")


class Stripe(Payment):
    def pay(self, amount):
        print(f"Strip activated with {amount}")


class PaymentService:
    def __init__(self, provider):
        self.provider = provider
    
    def checkout(self, amount):
        self.provider.pay(amount) #over here we are saying self.provider.pay because we need to use the pay method of the provider, and as the provider is now stored in the self.provider so we self.provider.pay, don't get confused, we are using provider attribute within class which is now stored in self.provider, and when roaming the class u need to user attributes with self. , Simply the provider is now stored in self.provider so we further use this self.provider



payment  = PaymentService(Stripe())

payment.checkout(1000)
