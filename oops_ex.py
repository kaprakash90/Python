class Account:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self,amt):
        self.balance += amt
        print(f'Deposited {amt} and the balance now is {self.balance}')
    def withdraw(self,amt):
        if amt<=self.balance:
            self.balance -= amt
            print(f'Withdrawn {amt} and the balance now is {self.balance}')
        else:
            print('you cant continue this transaction, Funds Unavailable!')

    def __str__(self):
        return(f'Account owner is {self.owner} \nAccount balance is ${self.balance}')
