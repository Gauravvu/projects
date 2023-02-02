from Crypto.Util import number
import random
import gmpy2
num = random.randrange(1,3)
if num == 1:
    a = number.getPrime(1024)
else:
    a = random.getrandbits(1024)
print("Random a generated is: ",a)
result = gmpy2.is_prime(a) #Rabin primality test
if(result == True):
    print("1")
else:
    print("0")