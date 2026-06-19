class gfather():
   def gproperties(self):
       
        print("1500 acers of land , 2BHK home")

class father(gfather):
   def fproperties(self):
       
        print("500 acers of land , 2BHK home")

class child(father):
   def cproperties(self):
       
        print("100 acers of land , 3BHK home")

print("the gfather asset : ")
kuppusamy = gfather()
kuppusamy.gproperties()
print("the father asset : ")
ramasamy = father()
ramasamy.fproperties()
ramasamy.gproperties()
print("the child asset : ")
vinoth = child()
vinoth.gproperties()
vinoth.fproperties()
vinoth.cproperties()