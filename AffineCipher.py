# encryption function
def enc(k,s,text):
    Alf = 'abcdefghijklmnopqrstuvwxyz'
    l = len(Alf)
    cip = ''
    for x in text:
    	y = Alf[(Alf.index(x)*k+s) % l]
    	cip = cip + y
    return cip

# decryption function
def dec(k,s,cip):
	Alf = 'abcdefghijklmnopqrstuvwxyz'
	l = len(Alf)

	# Euclid's algorithm
	if l <= 0:
		raise ValueError("modulus must be positive")
    	
	a = abs(k)
	b = l
	sign = -1 if k < 0 else 1
	c1 = 1
	d1 = 0
	c2 = 0
	d2 = 1
    
	while b > 0:
		q = a // b
		r = a % b

		c3 = c1 - q*c2
		d3 = d1 - q*d2
        
		c1 = c2
		d1 = d2
		c2 = c3
		d2 = d3
		a = b
		b = r
        
	if a != 1:
		raise ValueError("gdc of %d and %d is %d has no "
    	                 "multiplicative inverse modulo %d"
    	                 % (k, l, a, k, l))
    	                 
	k = c1 * sign;
	text = ''
	for x in cip: 
		y = Alf[(Alf.index(x)*k-s*k) % l]
		text = text + y
	return text
    
print(enc(3,4,'people'));
print(dec(3,4,'xquxlq'));
