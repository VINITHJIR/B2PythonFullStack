class CloudResoure():

    def __init__(self):
        print("Cloud initiated ")


class Server(CloudResoure):
    
    
    def __init__(self):
        super().__init__()
        print("Server Started")


s1 = Server()