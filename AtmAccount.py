class AtmAccount(object):
    def __init__(self, name, password):
        self.name = name
        self.balance = 0
        self.password = password

    def deposit(self, amount):
        amount = float(amount)
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        amount = int(amount)
        if self.balance - amount >= 0:
           self.balance -= amount
        else:
            print "Insufficient funds"
        return self.balance

    def get_current_balance(self):
        return self.balance

    def check_login(self, check_name, check_password):
        if self.password == check_password and self.name == check_name:
            return True
        else:
            return False




