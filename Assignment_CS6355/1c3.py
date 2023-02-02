from tkinter import *
import random
from typing import List
import gmpy2
from Crypto.Util import number
from math import gcd as bltin_gcd

#Execute Diffie-hellman  
def DH():
    p = 65537
    g = 3
    x = random.randrange(1,100)
    listbox1.insert(0,x)
    X = gmpy2.powmod(g,x,p)
    listbox2.insert(0,X)
    #input message
    y = random.randrange(1,10000)
    listbox3.insert(0,y)
    #Find c1 = g^r mod p
    Y = gmpy2.powmod(g,y,p)
    listbox4.insert(0,Y)
    #Encryption
    K1 = gmpy2.powmod(Y,x,p)
    listbox5.insert(0,K1)
    #Decryption
    K2 = gmpy2.powmod(X,y,p)
    listbox6.insert(0,K2)

root = Tk()
root.title('Diffie-Hellman Key Exchange')

#p and g given
show = Label(root, text = '0. Given large prime p=65537, a primary root g=3')
show.pack()
#
button_p = Button(root, text = "Execute", command = DH)
button_p.pack()
show_p = Label(root, text = '1. Chosen random number x is')
show_p.pack()
listbox1 = Listbox(root, height = 1, width = 40)
listbox1.pack()
#For q
show_q = Label(root, text = '2. Compute X = g^x mod p')
show_q.pack()
listbox2 = Listbox(root, height = 1, width = 40)
listbox2.pack()
#For p*q
show_pq = Label(root, text = '3. Chosen random number y is')
show_pq.pack()
listbox3 = Listbox(root, height = 1, width = 40)
listbox3.pack()
#For d
show_d = Label(root, text = '4 Compute Y = g^y mod p')
show_d.pack()
listbox4 = Listbox(root, height = 1, width = 40)
listbox4.pack()
#Message m randomly generated
show_de = Label(root, text = '5. Calculate the session key K=g^(xy) mod p')
show_de.pack()
show_m = Label(root, text = 'K = Y^(x) mod p')
show_m.pack()
listbox5 = Listbox(root, height = 1, width = 40)
listbox5.pack()
#For decryption
show_dec = Label(root, text = 'K = X^(y) mod p')
show_dec.pack()
listbox6 = Listbox(root, height = 1, width = 40)
listbox6.pack()

root.mainloop()
