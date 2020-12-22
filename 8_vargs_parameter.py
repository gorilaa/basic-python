def totalNumber(a = 7, *numbers, **phonebooks):
    print('My favorite number', a)
    
    for num in numbers:
        print(num)
    
    for name, phoneNumber in phonebooks.items():
        print(name, phoneNumber)

totalNumber(7, 1, 2, 3, Adam = 1111, Lesmana = 2222, Ganda = 3333)        