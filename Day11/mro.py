class Storage:

    def deploy(self):
        print("Storage Deploy")

class Security:

    def deploy(self):
        print("Security Deploy")
        
class CloudAdmin(Security , Storage):
    pass

admin = CloudAdmin()
admin.deploy()
print("MRO Orders are : ")
print(CloudAdmin.mro())