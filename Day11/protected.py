class CloudResource:

    def __init__(self):
        self._cpu = 70  #_ ->single underscore


class Server(CloudResource):

    def monitor(self):
        print(self._cpu)

server = Server()
server.monitor()



