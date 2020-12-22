def myDecorator(function):
    def wrapper():
        func = function()
        convertUppercase = func.upper()
        return convertUppercase
    return wrapper

@myDecorator
def greeting():
    return "Hallo adam lesmana"
print(greeting())