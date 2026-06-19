class father():
   def fproperties(self):
       
        print("500 acers of land , 2BHK home")

class mother():
   def mproperties(self):
       
        print("500 pown")

class child(father, mother):
   def cproperties(self):
       
        print("100 acers of land , 3BHK home")

jayanthi = child()

jayanthi.fproperties()
jayanthi.mproperties()
jayanthi.cproperties()