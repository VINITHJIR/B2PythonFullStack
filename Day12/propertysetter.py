class Payment:
    def __init__(self,town):
        self._address = town

    @property
    def address(self):
        return self._address
    
    @address.setter
    def address(self , value):
        if self._address != value :
            self._address = value
            return self._address 
    

p1 = Payment("coimbatore")
print(p1._address)
print(p1.address)
p1.address = "sathyamangalam"
print(p1.address)