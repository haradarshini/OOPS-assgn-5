class Account:
    def __init__(self,title = None,Balance = None):
        self.title = title
        self.Balance = Balance
    def deposit(self):
        self.amount = 500
        self.Balance = self.amount + self.Balance
    def withdrawal(self):
        self.amount = 500
        self.Balance = self.Balance - self.amount
    def getBalance(self):
        return self.Balance

class SavingsAccount(Account):
    def __init__(self,title = None,Balance = None,interestRate = None):
        super().__init__(title,Balance)
        self.interestRate = interestRate
    def interestAmount(self):
        self.interestAmount = (self.interestRate*self.Balance)/100
        return self.interestAmount

c = SavingsAccount("Sham",2000,5)

print("Balance is", c.getBalance())
c.deposit()
print("New Balance after deposit is", c.getBalance())
c.withdrawal()
print("New Balance after withdrawal is", c.getBalance())
print("Interest amount is", c.interestAmount())