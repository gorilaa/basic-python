def greeting():
    def hello():
        return 'Hallo Adam'
    return hello()

print(greeting())