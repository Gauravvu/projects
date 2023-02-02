import gmpy2
from gmpy2 import mpz
from random import randint

#Initialize
p = mpz(91384202109071442293463836021112242872202112556997233738650771115304627068435244189452217404518350934650625169787645878831492249234702966702870665364147218752886578786376766042770107058123323172961898496290467790495229761191517699758387645314555098976305458147233083947409856486295027584628343852346198294834673398056518565970306137057662042381108071850367597403128086501769091999204250111973206216989075174484334959172281822465253170809350903328437985069427319)
q = mpz(81461618609951926714232486073323681843605711813586129469089521881286578240351609211470308250561781558375310490543983933780038328473513066035201591085583608631590043360965785867067725207262314428957973642440166838678305658012018727393737744349209249924848069061992265051686526452564260097993214532057415090837113730859560081637862504223208931316591467688041729971515846931082731879867661935144206080893902297595573259652166808407688180529379028374251689469303983)
m = mpz(randint(1,5000)) #randomly generated message
r = mpz(randint(1,4000)) #random number generated
n = gmpy2.mul(p,q) # n = p*q 
lamda = gmpy2.mul(p-1,q-1) #lambda = (p-1)*(q-1)
g = n+1
n2 = pow(mpz(n),2) #n^2
flag = 0

#Encryption
c = gmpy2.mod(gmpy2.mul(gmpy2.powmod(g,m,n2),gmpy2.powmod(r,n,n2)),n2)# c = [(g^m mod n).(r^n mod n)])mod n^2

#Decryption
x = (gmpy2.powmod(c,lamda,n2)) # x = (c^lamda mod n^2)
s = gmpy2.mod(mpz((x-1)//n),n) # S = L[(c^lamda mod n^2)-1/n] mod n
m_obtained = gmpy2.mod(gmpy2.mul(gmpy2.powmod(s,1,n),gmpy2.invert(lamda,n)),n) # m_obtained = (S modn * lamda^-1 modn) mod n


#printing I/O
print("\nPallier encryption")
print("\np = "+str(p)+"\n\nq = "+str(q)+"\n\nn = "+str(n)+"\n\nlambda = "+str(lamda)+"\n\ng = "+str(g)+"\n\nr = "+str(r)+"\n")
while(flag == 0):
    print("1.Encrypt  2.Decrypt")
    inp = int(input("\nEnter an option: "))
    if inp == 1:
        print("\nYou chose encryption")
        print("\nThe message m is = ",m)
        print("\nThe cipertext c is = ",c)
        print("\n")
    if inp == 2:
        flag = 1
        print("\nYou chose decryption")
        print("\nThe message m is = ",m)
        print("\nThe cipertext c is = ",c)
        print("\nThe obtained m is = ",m_obtained)
 
