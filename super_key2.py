class Phone:

    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.__price=price
        self.brand=brand
        self.camera=camera

    def buy(self):
        print("Buying a Phone")


class SmartPhone(Phone):

    def __init__(self,price,brand,camera,os,ram):
        super().__init__(price,brand,camera)
        self.os=os
        self.ram=ram
        print("Inside smartphone constructor")

    def buy(self):
        print("Buying a smartphone")
        super().buy()

s=SmartPhone(20000,"Realme",20,"Android",8)
print(s.os)
print(s.brand)


####################################################################################

