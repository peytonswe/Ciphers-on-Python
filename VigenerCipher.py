from itertools import cycle

from functools import reduce

Alf = 'abcdefghijklmnopqrstuvwxyz'

# encryption function
def enc(k, text):
    # generate pairs the letter of the text is assigned a key letter
    pairs = zip(text, cycle(k))
    cip = ''
    for pair in pairs:
        total = reduce(lambda x, y: Alf.index(x) + Alf.index(y), pair)
        cip += Alf[total % 26]
    return cip

# decryption function
def dec(k, cip):
    pairs = zip(cip, cycle(k))
    text = ''
    for pair in pairs:
        total = reduce(lambda x, y: Alf.index(x) - Alf.index(y), pair)
        text += Alf[total % 26]
    return text


def show_result(text, k):
    """Generate a resulting cipher with elements shown"""
    encrypted = enc(k, text)
    decrypted = dec(k, encrypted)

    print ('k: %s' % k)
    print ('text: %s' % text)
    print ('encrytped: %s' % encrypted)
    print ('decrytped: %s' % decrypted)

show_result('mathematics', 'key')