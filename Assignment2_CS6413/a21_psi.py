import gmpy2
import random
from random import randrange
from gmpy2 import mpz

#Initialization
p = mpz(1941565844856531646114171208332308288737202855842892293872689903132005769897666395849234923976472072453661490113502664142778225637324691062275469734793251137939894389914123913124826353289301509129903379949104190609977093042559771891688839438919921448757235390765776478842732904868369951474975332819283595087576996031560840436159870411902918822624164712794990616043477766088755013907009086590054780401410468213986529220261325027267627116121738417383215790494187)
q = mpz(285376461243978140975765932732581103149537712152069644420135993928427819592986035222104139501336183003144267471237429844034590188308649074207369316104546207408682190938743300654289184009188460718232086639126795896283000490540402012738875973561593757825265544151667993394570912690313220018439984422341617132381470797199064863744364968461744131433351481806407427904615013424808167519722783328144804748114836053188981462035473996673507189016701858588656783971763)
g = 3
n = gmpy2.mul(p,q) #generate N
n2 = gmpy2.mul(n,2)
phi_n = gmpy2.mul(p-1,q-1)

alice = [] #To generate random
for i in range(1,10):
    a = random.randrange(5000,10000)
    if (gmpy2.gcd(a,phi_n) == 1):
        alice.append(a)
    print(i)    
print(alice)

#accumalated x
ax = 1
for j in alice:
    ax = gmpy2.mul(ax,j) #ax =  x1*x2*x3....*xn    
x_prod = gmpy2.mod(ax,phi_n) #x_prod = (x1*x2*x3....*xn) mod(phin)         
accx = gmpy2.powmod(g,x_prod,n) #accx = (g^x_prod) mod(n)

print("The public parameters (g,N): ",g,"\n",n)
print("The secret parameters (p,q): ",p,"\n",q)
print("--------------------------")
print("Input X for ALice: ")
print(alice)
print("--------------------------")
print("Option 1 to y belong to X")
print("Option 0 to y not belong to X")
op = int(input("Please enter an option: "))
print("Your option: ",op)
print("--------------------------")
print("The accumalated value of X(accx): ",accx)

#Choosing option 1 for y in x (Take mod on both sides)
if op == 1:
    #Get y from list of x
    k = random.randrange(1,len(alice))
    y = alice[k]
    print("y: ",y)
#Verification y in X
    y_inv = gmpy2.invert(y,phi_n)
    #print("y_inv : ",y_inv)
    z = gmpy2.powmod(accx,y_inv,n)
    z_ver = gmpy2.powmod(z,y,n)
    if z_ver == accx:
        print("Verified result for y IN X: ", z_ver)

#Choosing option 0 for y not in x
elif op == 0:
    flag = 0
    while flag == 0:
        yn = random.randrange(5000,10000)
        if yn not in alice and gmpy2.gcd(yn,x_prod) == 1:
            flag = 1 #condition to check y
            print("y: ",yn)
    gg, a, b = gmpy2.gcdext(yn,x_prod)
    print("Value of a: ",a)
    print("Value of b: ",b)
    print("gcd: ",gg)
#Verification y not in X (Take mod on both sides)
    prod_a_y = gmpy2.mul(-a,yn)
    a_y_phin = gmpy2.mod(prod_a_y,phi_n)
    g_pow_ay = gmpy2.powmod(g,a_y_phin,n)
    g_last = gmpy2.mul(g,g_pow_ay)
    g_verf = gmpy2.mod(g_last,n)
    print("g.[g^(-a)]^y: ",g_verf)
    accb = gmpy2.powmod(accx,b,n)
    if (accb == g_verf):
        print("Result for y NOT in X is 'Verified' (accx)^b: ",accb)