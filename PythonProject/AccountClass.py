class Account:
    def __init__(self):
        self.__number = None
        self.__balance = None
        self.__accountType = None

    def set_number(self, number):
        self.__number = number

    def get_number(self):
        return self.__number

    def set_balance(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_accountType(self, accountType):
        self.__accountType = accountType

    def get_accountType(self):
        return self.__accountType

    def deposit(self, amt):
        if amt > 0 and amt <= 50000:
            self.__balance = self.__balance + amt
            print("Your balance is", self.__balance)
        else :
            print("Error")

    def withdrawal(self, amt):
        if amt > 0 and amt < self.__balance and amt <= 50000:
            self.__balance = self.__balance - amt
            print("Your balance is", self.__balance)
        elif amt > 50000:
            print("You cannot withdraw more than 50000")
        else:
            print("Error")

acc = Account()
acc. set_number(987654)
acc.set_balance(10000)
acc.set_accountType("Savings")
print("Account number:", acc.get_number())
print("Account balance:", acc.get_balance())
print("Account Type:", acc.get_accountType())

acc.deposit(50000)
acc.withdrawal(50001)