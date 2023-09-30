class Customer:

    def __init__(self,name,gender,address):
        self.name=name
        self.gender=gender
        self.address=address

    def edit_profile(self,new_name,new_city,new_pin,new_state):
        self.name=new_name
        self.address.change_address(new_city,new_pin,new_state)

class Address:

    def __init__(self,city,pin,state):
        self.city=city
        self.pin=pin
        self.state=state

    def change_address(self,new_city,new_pin,new_state):
        self.city=new_city
        self.pincode=new_pin
        self.state=new_state


add=Address("kolkata",787898,"WB")
cust=Customer("Akhand","M",add)

print("Name",cust.name)
print("Gender",cust.gender)
print("State",cust.address.state)
print("Pin",cust.address.pin)
print("City",cust.address.city)


cust.edit_profile("Anmol","Kanpur",203509,"UP")


print("Name",cust.name)
print("Gender",cust.gender)
print("State",cust.address.state)
print("Pin",cust.address.pin)
print("City",cust.address.city)
