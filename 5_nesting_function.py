def myNumber(x):
    def num(x):
        return x + 1
    result = num(x)
    return result

print(myNumber(9))