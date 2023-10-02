class Phone:

    def __init__(self,price,brand,camera):
        self.__price=price
        self.brand=brand
        self.camera=camera

    def buy(self):
        print("Buying a Phone")


class SmartPhone(Phone):

    def buy(self):
        print("Buying a smartphone")
        super().buy()

s=SmartPhone(20000,"Realme",20)
s.buy()
