class Person:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
    
    def fullname(self):
        print(self.firstName + self.lastName)

personInfo = Person("Adam Lesmana ", "Ganda Saputra")

personInfo.fullname()

class Customer(Person):
    def __init__(self, firstName, lastName, address):
        self.address = address
        #init from class Person
        Person.__init__(self, firstName, lastName)
    
    def customerName(self):
        print(self.firstName + self.lastName + self.address)
    
customer = Customer("Gavin ", "Khawarizmi Abqary ", "Majalengka")
customer.customerName()