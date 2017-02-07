# function that converts binary representation to a string
def bin_to_string(bs):
    assert len(bs)%8 == 0
    s = ''
    for i in range(0,len(bs),8):
        s += chr(int(bs[i:i+8],2))
    return s

# function that converts a string to a binary representation
def string_to_bit(s):
    def char_to_8bit(c):
        return bin(ord(c))[2:].zfill(8)
    bs = ''
    for i in range(len(s)):
        bs += char_to_8bit(s[i])
    return bs

# adds two binary strings
def xor_bits(bs1,bs2):
    bs = ''
    for i in range(len(bs1)):
        if bs1[i] == bs2[i]:
            bs += '0'
        else:
            bs += '1'
    return bs

def fix_string(s):
    Alf = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    new_s = ''
    for i in s:
        if i in Alf:
            new_s += i;
        else:
            new_s += '_'
    return new_s

# example, when we have 7 ciphertext that was encrypted one time pad cipher with a single key

c0='101100111110100010000000110010110010001011010011100000111100001110111110111010011111101010011110011001101110101011011110101001011010001001001010010110011011010111001000011000011011101011111000111000000010100100000011101000011111100011100101101110111101110011101101111111110011011010110110'
c1='101100011010011110001000110000100010010011011011110001101100110010110011111010001111101010011111011111001011100110011111111010001011110101001000010111011010001010011100001000001010011111111011111000000010100100000000101000011110000111100101101011001100111111110000111111000010011110111010'
c2='101110001110001011001110110110010010001111010110100100101000110110111111111111101011001110011001011100101011100110011111111000101011110101001001010111001111101111010010001001001010001011101101111000000011000100000001101000011110110010101110101011111000111011101010111010010011000010111010'
c3='101100011110101110000010100011010010110011011000100010011100100111111101111110001011001010011110011110111010110111001100101001011011000101001001010101011011111010011100001101011011101010111110101010000011111101001111101110011110011110101010111111001101100111100011111000010011011010101101'
c4='101100011010011110011110110111110010010011010101100010101100100010110000101011001010100110011111011101001011100011011010111000011111001001001111010010111111101111011101011000011010010111101100101011110011100000000011101010111110001011100101101101001100111111101110111111100010011110111010'
c5='101001001110111110001011100011010010011111010110100101011101100111111101111010001010100010011000011001011110101011010010111001001011100101000011010010111111101111001000001010011011000010111110101000110010111100011111111011101111110110110000101100101000111011101101111111100010011110101100'
c6='101100011010011110000110110010000010101011000001100111111000110110101101111110011010100010000100011100001110101011011000111011001010010001000011010010111111101111001000001011101111010111111111111000000011011000000110101010011110011110110001111111001100011011100111111010010011000010101010'

x = 'Confidence is a plant of slow growth'

x0 = (string_to_bit(x))
print(x0)

# key
k = xor_bits(x0,c0)

print(bin_to_string(xor_bits(k,c0)))
print(bin_to_string(xor_bits(k,c1)))
print(bin_to_string(xor_bits(k,c2)))
print(bin_to_string(xor_bits(k,c3)))
print(bin_to_string(xor_bits(k,c4)))
print(bin_to_string(xor_bits(k,c5)))
print(bin_to_string(xor_bits(k,c6)))

a = (bin_to_string(xor_bits(c0,c1)))
b = (bin_to_string(xor_bits(c0,c2)))
c = (bin_to_string(xor_bits(c0,c3)))
d = (bin_to_string(xor_bits(c0,c4)))
e = (bin_to_string(xor_bits(c0,c5)))
f = (bin_to_string(xor_bits(c0,c6)))

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

print(fix_string(a))
print(fix_string(b))
print(fix_string(c))
print(fix_string(d))
print(fix_string(e))
print(fix_string(f))

