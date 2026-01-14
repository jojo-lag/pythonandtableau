class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, acctName, initialAmount):
        self.balance = initialAmount
        self.name = acctName
        print(f"\nAccount '{self.name}' created.\nBalance - #{self.balance:.2f}")
    
    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = #{self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"\nDeposit complete.")
        self.getBalance()

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry, account {self.name} only has a balance of #{self.balance:.2f}"
            )

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw complete.")
            self.getBalance()
        except BalanceException as error:
            print(f"Withdraw interrupted: {error}")

    def transfer(self, amount, account):
        try:
            print("\n *******\n\n Initializing Transfer..")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTransfer complete!\n\n*******")
        except BalanceException as error:
            print(f"\nTransfer interrupted.{error}")


class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit complete")
        self.getBalance()


class SavingsAcct(InterestRewardsAcct):
    def __init__(self, acctName, initialAmount):
        super().__init__(acctName, initialAmount)
        self.fee = 0.5
    
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            print("\nWithdraw completed.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")

    