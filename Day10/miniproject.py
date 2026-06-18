class App():
    
    def __init__(self , name , downloads , rating):
        self.name = name
        self.downloads = downloads
        self.rating = rating

    def viewdetails(self ):

        print(f"The {self.name} downloads is {self.downloads} and rating is {self.rating}")

obj1 = App("spotify" , 100000 , 4.5)  #App.__init__(obj1 , )
obj1.viewdetails()

