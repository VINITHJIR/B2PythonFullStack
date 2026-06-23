class CashPayment():

    def pay(self):
        print("Normal Payment")

class UPIPayment(CashPayment):
    
    #def pay(self):
        #print("UPI Payment")
    pass

print("parent object")
cash = CashPayment()
cash.pay()

print("child object")
upipay = UPIPayment()
upipay.pay()