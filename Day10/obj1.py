class app:
    views = 10000000
    downloads = 50000

    def intro(self , value):
        self.value = value  #whatsapp.value = value , facebook.value = 20000
        print("The total downloads is : " , value)

whatsapp = app()
whatsapp.intro(10000)   #app.intro(whatsapp , 10000)

telegram = app()
telegram.intro(20000) 

facebook = app()
facebook.intro(30000) #app.intro(facebook , 20000)

print("whatsapp " ,  whatsapp.value)
print("telegram " ,facebook.value)
print("facebook " ,telegram.value)





