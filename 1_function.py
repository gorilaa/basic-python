def halloFriend(name, address):
    print('Halo '+ name)
    print('Your Address '+ address)

#return value
def sum(x, y):
    return x + y

#default parameter
def personInfo(name = 'Adam Lesmana Ganda Saputra'):
    return name
    
halloFriend('Adam Lesmana', 'Majalengka')
print('return', sum(4, 5))
print('Hallo', personInfo('Gavin Khawarizmi'))
print('Hallo', personInfo('Maezura'))
print('Hallo', personInfo())