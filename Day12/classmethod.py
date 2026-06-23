class Payment():
    gst  = 18

    @classmethod
    def changegstvalue(cls , changedgstvalue):
        if changedgstvalue > cls.gst:
          cls.gst = changedgstvalue
          print("The GST Updated ")
        else:
           print("gst not updated ")


p1 = Payment()
p1.changegstvalue(100)
print(p1.gst)