#Polymorphism
class Jabar:
    def capitalCity(self):
        print("Capital City is Bandung")
        
    def language(self):
        print("Sunda is primary language")

class Jateng:
    def capitalCity(self):
        print("Capital City is Semarang")
        
    def language(self):
        print("Jawa is primary language")
        
def province(prov):
    prov.capitalCity()
        
sunda = Jabar()
jawa = Jateng()

province(sunda)
province(jawa)

'''
for province in (sunda, jawa):
    province.capitalCity()
    province.language()
'''