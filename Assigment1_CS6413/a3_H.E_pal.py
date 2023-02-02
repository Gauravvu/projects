import gmpy2
from gmpy2 import mpz
import random
from random import randint

#Initialize
p = mpz(91384202109071442293463836021112242872202112556997233738650771115304627068435244189452217404518350934650625169787645878831492249234702966702870665364147218752886578786376766042770107058123323172961898496290467790495229761191517699758387645314555098976305458147233083947409856486295027584628343852346198294834673398056518565970306137057662042381108071850367597403128086501769091999204250111973206216989075174484334959172281822465253170809350903328437985069427319)
q = mpz(81461618609951926714232486073323681843605711813586129469089521881286578240351609211470308250561781558375310490543983933780038328473513066035201591085583608631590043360965785867067725207262314428957973642440166838678305658012018727393737744349209249924848069061992265051686526452564260097993214532057415090837113730859560081637862504223208931316591467688041729971515846931082731879867661935144206080893902297595573259652166808407688180529379028374251689469303983)
n = gmpy2.mul(p,q) # n = p*q 
lamda = gmpy2.mul(p-1,q-1) #lambda = (p-1)*(q-1)
g = n+1 #generator
n2 = pow(mpz(n),2) #n^2
alice = [] #List for x values
enalice = [] #List for encoded x values
e1_alice = [] #List for encrypted and encoded x values
bob = [] #List for theta values
enbob = [] #List for encoded theta values
e1_bob = [] #List for encrypted and encoded theta values
r = mpz(randint(1,4000)) #random number generated


#printing I/O
print("The public-key (g,n): (",g,",",n,")" )
print("-------------------------------------")
print("The private-key (lambda, p, q): (",lamda,",",p,",",q,")")
print("-------------------------------------")
l = int(input("Please enter l(>=3): "))
print("-------------------------------------")

#Obtaining values of alice both x and encoded x
for i in range(0,l):
    ele_x = random.uniform(1.0, 10.0) #Random
    alice.append(ele_x)
    encode_x = int((ele_x * (2**30)) // 1) #Encoded with floor division
    enalice.append(encode_x)
print("Input values of x(1-n) for Alice (floating point numbers) = ",alice)    
print("Encoded x = ",enalice)

#Obtaining values of bob for both theta0 and encoded theta0
theta_o = random.uniform(1.0,10.0)
encode_tho = int((theta_o * (2**30))//1)

for j in range(0,l):
    ele_o = random.uniform(1.0,10.0)
    bob.append(ele_o)
    encode_o = int((ele_o * (2**30))//1) #Encoded with floor division
    enbob.append(encode_o)
print("theta_0: ",theta_o)    
print("Theta_0 is: ", encode_tho)    
print("Input values of theta(1-n) for bob (floating point numbers) = ", bob)    
print("Encoded theta = ",enbob)
print("-------------------------------------")

#Encryption1, used for theta_0 which gives us E(theta_0)
def encrypt(m):
    #c = gmpy2.mod(gmpy2.mul(gmpy2.powmod(g,m,n2),gmpy2.powmod(r,n,n2)),n2)# c = [(g^m mod n).(r^n mod n)])mod n^2
    g_m1 = gmpy2.powmod(g, m, n2)
    r_n1 = gmpy2.powmod(r, n, n2)
    gr1 = gmpy2.mul(g_m1, r_n1)
    c_e1 = gmpy2.powmod(gr1, 1, n2)
    ca = gmpy2.powmod(c_e1, 2**30, n2)
    return ca

#Encrypting theta 0
etheta_o = encrypt(encode_tho) 

#Encryption2, used for E(x) which gives us E(x(i))
def encrypt2(al): #al is alice input as argument
    g_m2 = gmpy2.powmod(g, al, n2)
    r_n2 = gmpy2.powmod(r, n, n2)
    gr2 = gmpy2.mul(g_m2, r_n2)
    c_e2 = gmpy2.powmod(gr2,1, n2)
    return c_e2

#Encrypts vector and stores it in a list
for element in enalice:
    e_a = encrypt2(element) #Encryption of alice
    e1_alice.append(e_a)
print("Encrypted vector E(x) = ",e1_alice)

#Encrypts E(x[k]^theta[k]) i.e. Multiplicative homomorphic property
for k in range(0,l):
    cb = gmpy2.powmod(e1_alice[k], enbob[k], n2)
    e1_bob.append(cb)

#Used for addition homomorphic property E(theta[0)*E(x[k]^theta[k])*E(x[k]^theta[k])...    
def multiply(mylist) :
    ans = 1
    for ele1 in mylist:
         ans = gmpy2.mod(gmpy2.mul(ans,ele1),n2) 
    return ans 

f_x_o1 = multiply(e1_bob) # E(x1)^theta1*E(x2)^theta2*...
f_x_o2 = gmpy2.mod(gmpy2.mul(etheta_o,f_x_o1),n2)
print("Encrypted result E(f_x_o) is = ",f_x_o2)
print("-------------------------------------")

#Decryption
def decrypt(a1):
    x = (gmpy2.powmod(a1,lamda,n2)) # x = (c^lamda mod n^2)
    s = gmpy2.mod(mpz((x-1)//n),n) # S = L[(c^lamda mod n^2)-1/n] mod n
    m_obtained = gmpy2.mod(gmpy2.mul(gmpy2.powmod(s,1,n),gmpy2.invert(lamda,n)),n) # m_obtained = (S modn * lamda^-1 modn) mod n
    return m_obtained

#Decryption of E(f(x,theta))
d = decrypt(f_x_o2) 
print("Decrypted encoded result is = ",d)
#Decoding of f(x,theta)
d1 = d/(2**60)
print("Decrypted result is = ",d1)
