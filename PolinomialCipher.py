alf = 'abcdefghijklmnopqrstuvwxyz'
m = 'polynomialcipher'.lower() 
a = 5

# encryption
def f(x):
	return x**2+2*x+22
c = ''.join([ alf[(alf.index(m[i])+a)%len(alf)]+
              alf[(alf.index(m[i+1])+f(alf.index(m[i])))%len(alf)]
              for i in range(0,len(m),2) ])

# it's how encryption function representation
print('u = [x+a,y+f(x)]')
print('c =', c, '\n')

# decryption
m = ''.join([ alf[(alf.index(c[i])-a)%len(alf)]+
              alf[(alf.index(c[i+1])-f(alf.index(c[i])-a))%len(alf)]
              for i in range(0,len(c),2) ])

# it's how decryption function representation
print('u = [x-a,y-f(x-a)]')
print('m =', m)
