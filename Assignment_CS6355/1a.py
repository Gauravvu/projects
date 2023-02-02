from Crypto.Util import number
import random
import gmpy2


a = random.getrandbits(1024)
print("Random a generated is: ",a)
b = random.getrandbits(1024)
print("\nRandom b generated is: ",b)

print("Computation using Extended euclidean algorithm")
c = gmpy2.invert(a,b)
print("\nComputed c = (a^(-1) mod b) is: ", c)
d = gmpy2.invert(b,a)
print("\nComputer d = (b^(-1) mod a) is: ", d)
