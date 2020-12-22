class Companies:
    companyName = "Berlin Corp"
    
    def __init__(self, tagline, address):
        self.tagline = tagline
        self.address = address
    
    def information(self):
        print("My Company name is", Companies.companyName)

companyInfo = Companies("Python for beginners", "Majalengka")

#modify tagline
companyInfo.tagline = "Python is simple"
companyInfo.information()

print(companyInfo.tagline)

#remove address
del companyInfo.address