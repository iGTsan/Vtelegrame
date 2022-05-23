import random
import prime
blocksize = 64
def binp(a,n,mod):
    if n==1:
        return a%mod
    b = binp(a,n//2,mod)
    if n%2:
        return b*b*a%mod
    return b*b%mod

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

x,y = 0,0

def gcd1 (a,b):
    global x,y
    if  a == 0:
        x = 0
        y = 1
        return b
    d = gcd1(b%a, a)
    x1 = x
    x = y - (b // a) * x
    y = x1
    return d

def make_key(p,q):
    global x,y
    fi = (p-1)*(q-1)
    e = random.randint(23,fi)
    while gcd1(e,fi)!=1:
        e = random.randint(23, fi)
    d = x%fi
    return (p*q,e,d)

def encode_rsa(m,e,n):
    return binp(m,e,n)

def decode_rsa(m,d,n):
    return binp(m,d,n)

def encode_rsa_s(s,e,n):
    a1,a2,a3 = random.randint(23, n),random.randint(23, n),random.randint(23, n)
    c1 = encode_rsa(a1,e,n)
    c2 = encode_rsa(c1+a2,e,n)
    c3 = encode_rsa(c2+a3,e,n)
    st = [c1,c2,c3]
    for i in range(len(s)):
        st.append(encode_rsa(st[-1]+ord(s[i]),e,n))
    st.append(n+1)
    #print(st)
    return list(map(lambda x: x.to_bytes(blocksize, 'little', signed=False),st))

def decode_rsa_s(s,d,n):
    st = [0]+list(map(lambda x: int.from_bytes(x, 'little', signed=False),s))
    st1 = st[:]
    for i in range(1,len(st)-1):
        st[i] = (decode_rsa(st[i],d,n)-st1[i-1])%n
    return ''.join(list(map(chr,st[4:-1])))

def gen_keys():
	m = int(1e9)
	a = prime.get_prime(random.randint(m, 2 * m))
	b = prime.get_prime(random.randint(m, 2 * m))
	n,e,d = make_key(a ,b)
	f = open("keys", "w")
	f.write(str(e) + '\n')
	f.write(str(n) + '\n')
	f.write(str(d))
	f.close()

if __name__ == "__main__":
	print(n,e,d)
	print(binp(10,e*d,n))
	a = encode_rsa_s('aba',e,n)
	print(a)
	print(decode_rsa_s(a,d,n))
	