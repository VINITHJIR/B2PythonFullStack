class CloudResource:    
     def __init__(self):        
         self.mymoney = 50000

     def getmymoney(self):
          
          print(self.mymoney)

resource = CloudResource()
resource.mymoney = 1
resource.getmymoney()
print(resource.mymoney)