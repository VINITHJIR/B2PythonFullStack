import time
start = time.time()
def dwonload_file():#9.10
    print("download started") #
    time.sleep(5)
    print("download completed") #9.15


def email_sent():#9.15
    print("sent mail started")
    time.sleep(2)
    print("sent mail completed")#9.17



dwonload_file()
email_sent()

end = time.time()
print("total time : " ,end - start) #7

