from threading import Thread
import time
start = time.time() #9.15
def dwonload_file():
    print("download started")
    time.sleep(5)
    print("download completed")#9.20


def email_sent(): #9.15
    print("sent mail started")
    time.sleep(2)
    print("sent mail completed")#9.17

t1 = Thread(target=dwonload_file )
t2 = Thread(target=email_sent )

t1.start()
t2.start()
t1.join()
t2.join()

print("hi jayanthi")

end = time.time() #9.20
print("total time : " ,end - start)

