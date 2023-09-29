class Atm:

    def __init__(self):

        self.__pin=""
        self.__balance=0

        self.menu()
        print("Hello")

    def get_pin(self):
        return self.__pin

    def set_pin(self,new_pin):
        self.__pin=new_pin
        
    def menu(self):
        user_input=input("""
                            Hellom how would you like to proceed?
                            1.Enter 1 to create pin
                            2.Enter 2 to deposit
                            3.Enter 3 to withdraw
                            4.Enter 4 to check balance
                            5.Enter 5 to exit
        """ )
        if user_input=="1":
            self.create_pin()
        elif user_input=="2":
            self.depost()
        elif user_input=="3":
            self.withdraw()
        elif user_input=="4":
            check_balance()
        elif user_input=="5":
            print("Exit")
                    
    def create_pin(self):
        self.__pin=input("Enter your Pin")
        print("Pin set Successfully")

    def deposit(self):
        temp=input("Enter your pin")
        if temp==self.__pin:
            amount=int(input("Ënter the amount"))
            self.__balance=self.__balance+amount
            print("Deposited successfully")
        else:
            print("Invalid Pin")

    def withdraw(self):
        temp=input("Enter your pin")
        if temp==self.__pin:
            amount=int(input("Ënter the amount"))
            if amount<self.__balance:
                self.__balance=self.__balance-amount
                print("Withdrawn successfully")
            else:
                print("ïnsufficient Balance")
        else:
            print("Invalid Pin")

    def check_balance(self):
        temp=input("Enter your pin")
        if temp==self.__pin:
            print(self.__balance)
        else:
            print("Invalid Pin")
            
