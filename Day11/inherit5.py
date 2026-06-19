class CloudResource:
    def start(self):
        print("Cloud Started")

class Server(CloudResource):
   pass

class Storage:
    def storage_info(self):
        print("Storage Ready")

class Security:
    def security_info(self):
        print("Security Ready")

class CloudAdmin(Storage,Security,Server):
    pass

admin = CloudAdmin()
admin.start()
admin.storage_info()
admin.security_info()