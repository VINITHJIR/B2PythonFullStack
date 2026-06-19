class CloudResource:    
     def __init__(self):        
         self.__mymoney = 50000

     def assignmoney(self , changemoneyvalue ):
          self.__mymoney = changemoneyvalue

     def getmymoney(self):
          
          print(self.__mymoney)

     

resource = CloudResource()
resource.__mymoney = 1 #copy __my2money 
print(resource.__mymoney)
resource.assignmoney(8000)
resource.getmymoney()



