# Priciple 
# Single Responsibility SRP


# class Person:
#     isInstance = True
#     def __new__(cls):
#         print("Creating instance of Person")
#         if cls.isInstance == True:
#             isinstance = super().__new__(cls)
#             return isinstance
#  # ab ek hi baar chalega single turn ban gya ab ye jab hame koi asii cheez banani ho jo ek hi bane to ham sigle turn used karte h 
#  # jese hame kisi company k CEO k liye instance banana ho wo to ek hi banega naa boht saare ceo nhi ayege

#     #     return super().__new__(cls)
#     # what should i do k ek hi init method chale










# Interface segragation Principle ISP 2

# liskov Substitution Principle LSP 03 
# when we know that a method like def pay jo har class me hain or hamne jb paypal ka method banaya to use wo khud
# automatic samjh gya python wo shocked nhi hua kiuke uske andr wahi cheeze thi jo har class me hai

# Open Closed Principle OCP 04 
# paramter ki koi value change karna

# Dependency Inversion Principle DIP 05
# if i pass Ipayment as a parameter n class IRefundProcess directly  this is called dependency inversion principle
from abc import ABC, abstractmethod      #abstract base class
class Ipayment(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass
class IRefundProcess(ABC):
    @abstractmethod    
    def pay(self, transaction_id: str):
        pass
class Paypal(ABC):
     @abstractmethod
     def pay(self, amount: float, transaction_id: str)-> None:
        print(f"Payment of {amount:67.5} made using Stripe.")
     def refund(self, transaction_id: str) -> None:
        print(f"Refund transaction id is {transaction_id} ")

class Stripe_Process(IRefundProcess, Ipayment):
    def pay(self, amount: float, transaction_id: str)-> None:
        print(f"Payment of {amount:67.5} made using Stripe.")
    def refund(self, transaction_id: str) -> None:
        print(f"Refund transaction id is {transaction_id} ")
class Bank_payment(Ipayment):
    def pay(self, amount: float) -> None: 
        print(f"Payment of {amount:60.0} made using Bank.")       
class OrderProcessor:
    def __init__(self, payment: Ipayment, repo) -> None:
        self.payment = payment
        self.repo = repo
    def process_order(self, amount: float) -> None:
        self.payment.pay(amount)

# def pay (self, amount: float) -> None: this is the method that will be used to process the payment 
# only this method are common






# Dependency Inversion Principle DIP 05
# if i pass Ipayment as a parameter n class IRefundProcess directly  this is called dependency inversion principle
class Ipayment(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass
class IRefundProcess(Ipayment): #this is DIP
    @abstractmethod    
    def pay(self, transaction_id: str):
        pass