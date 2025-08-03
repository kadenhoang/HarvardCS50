class Account():
    def __init__(self):
        self._balance = 0

    @property #to call this function in main without the ()
    #read-only and cannot change the value in the main function.
    def balance(self):
       return self._balance

    def deposit(self, n):
        self._balance += n

    def widthraw(self, n):
        self._balance -= n

# class make a variable global(accessible for other method in a class)
def main():
    account = Account()
    account.deposit(100)
    account.widthraw(50)
    print("Balance:" , account.balance)

if __name__ =="__main__":
    main()


