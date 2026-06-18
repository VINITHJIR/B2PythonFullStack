class App:

    def __init__(self, usage, downlaods, rating ):
        self.usage = usage
        self.downloads = downlaods
        self.feedback = rating
        print("App created ") 

threads = App(10000, 5000, 4.5) # App.__init__(threads , 10000 , 5000 , 4.5 ) == __init__(self , usage , downlaods , rating )
print(threads.usage)
print(threads.downloads)
print(threads.feedback)