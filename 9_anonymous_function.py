def anonymousFunction(number):
    return lambda f : f * number
double_num = anonymousFunction(2)

print(double_num(2.4))