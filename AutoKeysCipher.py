from functools import reduce

Alf = 'abcdefghijklmnopqrstuvwxyz'

# ecryption function
def enc(k, text):
    pairs = zip(text, k + text)
    cip = ''
    for pair in pairs:
        total = reduce(lambda x, y: Alf.index(x) + Alf.index(y), pair)
        cip += Alf[total % 26]
    return cip

# decryption function
def dec(k, cip, text):
    pairs = zip(cip, k + text)
    text = ''
    for pair in pairs:
        total = reduce(lambda x, y: Alf.index(x) - Alf.index(y), pair)
        text += Alf[total % 26]
    return text

print(enc('key', 'mathematics'));
print(dec('key', 'wertefhxucl', 'mathematics'))

