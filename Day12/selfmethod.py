class mathclass():


    def addfunc(self,*value):
         sumofvalue = sum(value)
         self.sumofvalue = sumofvalue #sum1.sumofvalue = 100
         print(sumofvalue)
    
sum1 = mathclass()
sum1.addfunc(10,20,30,40)
sum2 = mathclass()
sum2.addfunc(10,20,30,50)
sum3 = mathclass()
sum3.addfunc(10,20,30,60)
print(sum1.sumofvalue)