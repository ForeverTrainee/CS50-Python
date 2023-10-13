class Account:
    def __init__(self):
        self._balance = 0
    def balance(self):
        return self._balance

    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n



def main():
  account = Account()
  account.deposit(100)
  print("Balance: ", account.balance())
  account.withdraw(50)
  print("Balance: ", account.balance())



def deposit(n):
    global balance
    balance += n

def withdraw(n):
    global balance
    balance -= n

if __name__ == "__main__":
    main()