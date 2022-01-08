import random
import string

def senha(numero_caracteres, uppercase=True, lowercase=True, numbers=True):
    s = ''
    if uppercase:
        s += string.ascii_uppercase
    if lowercase:
        s += string.ascii_lowercase
    if numbers:
        s += string.digits
    return ''.join(random.choice(s) for i in range(numero_caracteres))

a = 0
while a == 0:
    i = int(input('\nQuantos caracteres sua senha precisa ter? '))
    c = input('\nSua senha precisa ter letras maiúsculas? (S) sim (N) não ')
    n = input('\nSua senha precisa ter números? (S) sim (N) não ')

    if(c.upper() == 'S'):
        s = senha(i, uppercase=True)
        
        if(n.upper() == 'S'):
            s = senha(i, uppercase=True, numbers=True)
        else:
            s = senha(i, uppercase=True, numbers=False)

    elif(c.upper() == 'N'):
        s = senha(i, uppercase=False)
        
        if(n.upper() == 'S'):
            s = senha(i, uppercase=False, numbers=True)
        else:
            s = senha(i, uppercase=False, numbers=False)

    print(f'\nSua nova senha gerada:\n "{s}"\n')

    continue
