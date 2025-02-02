class Account:
    def __init__(self, owner ,balance):
        self.owner = owner
        self.balance = balance
    def deposit(self,dep):
        self.balance += dep
        print(f"Deposit: {dep}$ ✅\nAvailable: {self.balance}$\n")
    def withdraw(self,wtd):
        if wtd <= self.balance :
            self.balance -= wtd
            print(f"Withdrawal: {wtd}$ ✅\nAvailable: {self.balance}$\n")
        else:
            print("Operation declined ❌ \n\"Not enough money for withdrawal\"")


myacc = Account("Radmir", 1000)
print("Your balance",myacc.balance,"$\n")

myacc.deposit(1500)
myacc.deposit(500)

myacc.withdraw(2000)

myacc.withdraw(2000)
