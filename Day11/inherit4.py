class father():
   def fproperties(self):
       
        print("500 acers of land , 2BHK home")

class child1(father):
   def c1properties(self):
       
        print("500 pown")

class child2(father):
   def c2properties(self):
       print("500 pown")

angavai = child1()
angavai.fproperties()
angavai.c1properties()
sangavai = child2()
sangavai.fproperties()
sangavai.c2properties()