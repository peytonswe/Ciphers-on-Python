# encryption function
def enc(k, text):
    Alf = 'abcdefghijklmnopqrstuvwxyz'
    l = len(Alf)
    cip = ''
    for x in text:
    	y = Alf[(Alf.index(x)+k) % l]
    	cip = cip + y
    return cip

# decryption function
def dec(k, cip):
    Alf = 'abcdefghijklmnopqrstuvwxyz'
    l = len(Alf)
    text = ''
    for x in cip:
        y = Alf[(Alf.index(x) - k) % l]
        text = text + y
    return text

print(enc(4,'ab'));
print(dec(4,'ef'));
