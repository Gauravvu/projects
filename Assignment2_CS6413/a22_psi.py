import gmpy2
import random
from random import randrange
from gmpy2 import mpz,mpq,mpfr,mpc
import hashlib

#Intialization
p = mpz(5809605995369958062791915965639201402176612226902900533702900882779736177890990861472094774477339581147373410185646378328043729800750470098210924487866935059164371588168047540943981644516632755067501626434556398193186628990071248660819361205119793693985433297036118232914410171876807536457391277857011849897410207519105333355801121109356897459426271845471397952675959440793493071628394122780510124618488232602464649876850458861245784240929258426287699705312584509625419513463605155428017165714465363094021609290561084025893662561222573202082865797821865270991145082200656978177192827024538990239969175546190770645685893438011714430426409338676314743571154537142031573004276428701433036381801705308659830751190352946025482059931306571004727362479688415574702596946457770284148435989129632853918392117997472632693078113129886487399347796982772784615865232621289656944284216824611318709764535152507354116344703769998514148343807)
x = []
y = []
a = []
bf = []
m = 50
n = 50
#For X values of alice
for i in range(0,m):
    ele_x = random.randrange(5000,10000)
    x.append(ele_x)
#print(x)

#For Y values of Bob
for j in range(0,n):
    ele_y = random.randrange(5000,10000)
    y.append(ele_y)
#print(y)

#Obtaining values of alpha and beta
c = random.randrange(1,p-1)
alpha = p-c
#print(alpha)
d = random.randrange(1,p-1)
beta = p-d
print("public parametrs p: ",p)
print("Input X randomly generated for ALice: ",x)
print("Input Y randomly generated for Bob: ",y)
("--------------------------------------------")
print("Secret key alpha : ",alpha)
print("Secret key Beta: ",beta)
#print(beta)
#For Ai,Abeta
for k in x:
    a1 = gmpy2.powmod(k,alpha,p)
    a2 = gmpy2.powmod(a1,beta,p)
    a.append(a1)

#hash function1
for k1 in a:
    val = hashlib.sha256()
    t1 = gmpy2.to_binary(a[k1]+1)
    val.update(t1)
    h1 = gmpy2.mod(t1,600)
    h.append(h1)
print(h)        

#hash fucntion2
for k2 in a:
    val1 = hashlib.sha256()
    t2 = gmpy2.to_binary(a[k1]+2)
    val2.update(t2)
    h2 = gmpy2.mod(t2,600)
    ha.append(h2)
 

#hash function3
for k3 in a:
    val2 = hashlib.sha256()
    t1 = gmpy2.to_binary(a[k1]+2)
    val3.update(t1)
    h3 = gmpy2.mod(t1,600)
    hb.append(h3)


#Create BF of size 600 with 0
for z in range(0,10000):
    bf.append(0)
    
#Inserting (Ai^beta mod p) into BF
for r in h:
    if h in bf[r]:
        if bf[r] == 0:
            bf[r] == 1 #if value at that point is 0, make it one
        else:
            bf[r] = 0
for r in ha:
    if h in bf[r]:
        if bf[r] == 0:
            bf[r] == 1 #if value at that point is 0, make it one
        else:
            bf[r] = 0
for r in hb:
    if h in bf[r]:
        if bf[r] == 0:
            bf[r] == 1 #if value at that point is 0, make it one
        else:
            bf[r] = 0                        
#For Bi, ci
for k1 in y:
    b1 = gmpy2.powmod(k1,beta,p)
    b2 = gmpy2.powmod(b1,alpha,p)
    b.append(b2)    

#BF.check
#hash function1 for check
for l in a:
    value = hashlib.sha256()
    tf = gmpy2.to_binary(b[l]+1)
    value.update(f1)
    s1 = gmpy2.mod(f1,600)
    s.append(s1)        

#hash fucntion2 for check
for l1 in a:
    value1 = hashlib.sha256()
    f2 = gmpy2.to_binary(b[l1]+2)
    value2.update(f2)
    s2 = gmpy2.mod(f2,600)
    sa.append(s2)
 
#hash function3 for check
for l2 in a:
    value2 = hashlib.sha256()
    f3 = gmpy2.to_binary(b[l2]+2)
    value3.update(f3)
    s3 = gmpy2.mod(f3,600)
    sb.append(s3)

for i in range(bf):
    if (h[i] == s[i]) and (ha[i] == sa[i]) and (hb[i] == sb[i]):
        S.append(i) 
print("Size of s is", len(s))
print("Elements of s are", s)    
