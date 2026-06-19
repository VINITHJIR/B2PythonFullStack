class CloudResource:    
     def __init__(self):        
         self.__apikey = "AWS123"

     def getprivatekey(self):
          
          print(self.__apikey)

resource = CloudResource()
resource.getprivatekey()
print(resource.__apikey)

