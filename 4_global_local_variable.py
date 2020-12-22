number = 10

def myNumber():
    global number
    print(number)
    number = 100
    print('My fav number', number)

myNumber()

print(number)