import gmpy2
from random import randint
from gmpy2 import mpz,mpq,mpfr,mpc

#Initialization
p = mpz(19211916981990472618936322908621863986876987146317321175477459636156953561475008733870517275438245830106443145241548501528064000686696553079813968930084003413592173929258239545538559059522893001415540383237712787805857248668921475503029012210091798624401493551321836739170290569343885146402734119714622761918874473987849224658821203492683692059569546468953937059529709368583742816455260753650612502430591087268113652659115398868234585603351162620007030560547611)
q = mpz(49400957163547757452528775346560420645353827504469813702447095057241998403355821905395551250978714023163401985077729384422721713135644084394023796644398582673187943364713315617271802772949577464712104737208148338528834981720321532125957782517699692081175107563795482281654333294693930543491780359799856300841301804870312412567636723373557700882499622073341225199446003974972311496703259471182056856143760293363135470539860065760306974196552067736902898897585691)
rand_state = gmpy2.random_state(randint(1,10))
flag = 0


n = gmpy2.mul(p,q) #n = p*q
phi_n = gmpy2.mul(p-1,q-1) #phi(n) = (p-1) * (q-1) 

#Check if gcd(e,phi(n)==1), Return e.
e = gmpy2.mpz_random(rand_state,phi_n) 
while(gmpy2.gcd(e,phi_n) != 1):
    e = gmpy2.mpz_random(rand_state,phi_n)


d = gmpy2.invert(e,phi_n)#Value of d 
m = gmpy2.mpz(randint(1,5000))#randomly generated message
c = gmpy2.powmod(m,e,n) # c = m^e mod n 
m_obtained = gmpy2.powmod(c,d,n)# m = c^d mod n 

print("The first prime is p =\n",p)
print("The second prime is q =\n",q)
print("The composite modulus n =\n",gmpy2.mul(p,q))
print("The encryption exponent e =\n",e)
print("The decryption exponent d =\n",d)
print("----------------------------------")
while(flag == 0):
    print("Please enter an option")
    o = int(input("1 to Encrpyt\n2 to Decrypt\n = "))
    print("Your option: ",o)
    if o == 1:
        print("Encryption:")
        print("Plaintext (randomly generate) to be encrypted is m = ",m)
        print("ciphertext is c =\n",c)
    if o == 2:
        flag = 1
        print("Decryption:")
        print("message is m = ",m)
        print("Ciphertext to be decrypted is c =\n",c)
        print("Decrypted plaintext is m = ",m_obtained)