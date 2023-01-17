class Account:
    def __init__(self,title = None,Balance = None):
        self.title = title
        self.Balance = Balance

class SavingsAccount(Account):
    def __init__(self,title = None,Balance = None,interestRate = None):
        super().__init__(title,Balance)
        self.interestRate = interestRate
c = SavingsAccount("lipsa",2000,5)