#Encapsulation

class Cars:
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color
    
    def setSpeed(self, value):
        self.speed = value
    
    def getSpeed(self):
        return self.speed
    
    def getColor(self):
        return self.color

ford = Cars(1000, "Red Candy")
nissan = Cars(2000, "Blue Sky")
bmw = Cars(3000, "Blue Sky")

#set new speed
ford.setSpeed(4500)
nissan.setSpeed(2500)
bmw.setSpeed(1500)

#change speed
ford.speed = 3000

print(ford.getSpeed())
print(ford.getColor())