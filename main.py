from password.pswrd import *

a = 0
while a == 0:
    i = int(input('\nHow many characters does your password need to have?'))
    c = input('\nDoes your password need to have capital letters? (Y) yes (N) no ')
    n = input('\nDoes your password need numbers? (Y) sim (N) no ')

    if(c.upper() == 'Y'):
        p = pswrd(i, uppercase=True)
        
        if(n.upper() == 'S'):
            p = pswrd(i, uppercase=True, numbers=True)
        else:
            p = pswrd(i, uppercase=True, numbers=False)

    elif(c.upper() == 'N'):
        p = pswrd(i, uppercase=False)
        
        if(n.upper() == 'S'):
            p = pswrd(i, uppercase=False, numbers=True)
        else:
            p = pswrd(i, uppercase=False, numbers=False)

    print(f'\nYour brand new password:\n "{p}"\n')

    continue
