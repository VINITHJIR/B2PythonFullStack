class Payment:

    def pay(self,amount,tax=0):
        print(amount + tax)

payment = Payment()

payment.pay(1000)

payment.pay(1000,100)