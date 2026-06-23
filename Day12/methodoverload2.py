class Bill():
    
    def calculate(self , *amounts):
        self.value = sum(amounts)
        print(self.value)
    
b1 = Bill()
b1.calculate(10 )
b1.calculate(10,20 ,30)
b1.calculate(10 ,20 ,30 ,40 ,50)