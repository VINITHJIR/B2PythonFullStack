class Bank:

    def deposit(self, amount):
      self.balance = amount
      print("current salary" , amount)

acc1 = Bank()
acc1.deposit(10000)
acc2 = Bank()
acc2.deposit(50000)
acc = Bank()
acc.deposit(170000)
acc4 = Bank()
acc4.deposit(1560000)
acc5 = Bank()
acc5.deposit(1200000)
print(acc1.balance)
