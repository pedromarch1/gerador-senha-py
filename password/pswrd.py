import string
import random

def pswrd(ch_number, uppercase=True, lowercase=True, numbers=True):
    p = ''
    if uppercase:
        p += string.ascii_uppercase
    if lowercase:
        p += string.ascii_lowercase
    if numbers:
        p += string.digits
    return ''.join(random.choice(p) for i in range(ch_number))
