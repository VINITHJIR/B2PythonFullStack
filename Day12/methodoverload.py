class Payment():
  
    def pay(self ,amount , tax = 0 , gst =10):
        print("func 1" , amount + tax + gst)


p1 = Payment()

p1.pay(1000)
p1.pay(1000 ,100)
p1.pay(1000 , 1200 ,50000)
