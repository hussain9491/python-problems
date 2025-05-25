
class Account:
    def __init__(self, balance, account_number):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, credit):
      self.balance += credit
      print( f" your credit amount was: {credit}")
      return f"Your account number is: {self.account_number}, your total balance is: {self.show_balance()}"

      
    
    def debit(self, debit):
        
        if debit < 0:
            return f"Invalid amount"
        elif debit == 0:
            return "Zero amount cannot be debited"
        if debit > self.balance:
            return f"Insufficient balance"
        else:
            self.balance -= debit
            print(f" your debit amount was: {debit}")
            return f"Your account number is: {self.account_number}, your balance is: {self.show_balance()}" 
    def show_balance(self):
        return f"Account Number: {self.account_number}, Balance: {self.balance}"     
display = Account(1000, 123456789)

print(display.deposit(7000))  
print(display.debit(120))
print(display.show_balance())
