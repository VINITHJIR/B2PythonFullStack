#single inheritance - > child class get parent access
class father():

    def __init__(self , goldvalue):
        self.goldvalue = goldvalue

    def fproperties(self):
        print("the gold value : " , self.goldvalue)
        print("500 acers of land , 2BHK home")

class child(father):
    
    def cproperties(self):
        print("1 bike")

print("The father properties : ")
ramasamy = father("100 pown")
ramasamy.fproperties()

print("The child properties : ")
dinesh = child()
dinesh.fproperties()





