class CloudResource:    
     def __init__(self):        
         self.__apikey = "AWS123"

     def jayanthi(self):
          return self.__apikey
     
     


resource = CloudResource()
resource.__apikey = "vini" #__api_1key = 
print(resource.__apikey) #vini
print(resource.jayanthi()) #aws123

