class CashPayment():

    def pay(self):
        print("Normal Payment")

class UPIPayment(CashPayment):
    
    def pay(self):
        print("UPI Payment")


upipay = UPIPayment()
upipay.pay()