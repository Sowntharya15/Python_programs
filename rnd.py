class BankAccount:
    def deposit(self,dep):
        self.dep = dep
    def set_limit(self,limit):
        self.limit = limit
    def withdraw(self):
        pass
        
class SavingsAccount(BankAccount):
    def withdraw(self,amt):
        if amt > self.limit:
            print("Withdrawal Limit Exceeded. Balance {}".format(self.dep))
        else:
            print("{}".format(self.dep - amt))
        
class CheckingAccount(BankAccount):
    def withdraw(self,amt):
        if amt > self.limit:
            print("Withdrawal Limit Exceeded. Balance {}".format(self.dep))
        else:
            print("{}".format(self.dep - amt))
        
b1=SavingsAccount()
b1.deposit(int(input()))
b1.set_limit(int(input()))
b1.withdraw(int(input()))

    