class BankAccount:
    def deposit(self, dep):
        self.dep = dep

    def set_limit(self, limit):
        self.limit = limit

    def withdraw(self,amt):
        pass


class SavingsAccount(BankAccount):
    def withdraw(self, amt):
        if amt > self.limit:
            print("Withdrawal Limit Exceeded. Balance {}".format(float(self.dep)))
        else:
            print("{}".format(float(self.dep - amt)))


class CheckingAccount(BankAccount):
    def withdraw(self, amt):
        if amt > self.limit:
            print("Withdrawal Limit Exceeded. Balance {}".format(float(self.dep)))
        else:
            print("{}".format(float(self.dep - amt)))


b1 = SavingsAccount()
b2 = CheckingAccount()
b1.deposit(int(input()))
b1.set_limit(int(input()))
b1.withdraw(int(input()))
b2.deposit(int(input()))
b2.set_limit(int(input()))
b2.withdraw(int(input()))
