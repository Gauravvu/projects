from tkinter import *
import random
from typing import List
import gmpy2
from Crypto.Util import number
from math import gcd as bltin_gcd

 

#Execute Elgamal    
def Elg():
    p = 65537
    g = 3
    x = random.randrange(1,100)
    listbox1.insert(0,x)
    y = gmpy2.powmod(g,x,p)
    listbox2.insert(0,y)
    #input message
    m = random.randrange(1,10000)
    listbox3.insert(0,m)
    #Find random number r
    r = random.randrange(1,10000)
    listbox4.insert(0,r)
    #Find c1 = g^r mod p
    c1 = gmpy2.powmod(g,r,p)
    listbox5.insert(0,c1)
    #Encryption
    c2 = gmpy2.mod(gmpy2.mul(gmpy2.powmod(m,1,p),gmpy2.powmod(y,r,p)),p)
    listbox6.insert(0,c2)
    #Decryption
    term = (p-x-1)
    dec = gmpy2.mod(gmpy2.mul(gmpy2.powmod(c1,term,p),gmpy2.powmod(c2,1,p)),p)
    listbox7.insert(0,dec)

  

root = Tk()
root.title('ElGamal Encryption/Decryption')

#To generate p and q
show = Label(root, text = '0. Given large prime p=65537, a primary root g=3')
show.pack()
#For q
button_p = Button(root, text = "Execute", command = Elg)
button_p.pack()
show_p = Label(root, text = '1. Chosen private key x is')
show_p.pack()
listbox1 = Listbox(root, height = 1, width = 40)
listbox1.pack()
#For q
show_q = Label(root, text = '2. Compute the corresponding public key, y = g^x mod p')
show_q.pack()
listbox2 = Listbox(root, height = 1, width = 40)
listbox2.pack()
#For p*q
show_pq = Label(root, text = '3. Input message m is')
show_pq.pack()
listbox3 = Listbox(root, height = 1, width = 40)
listbox3.pack()
#For e
show_el = Label(root, text = '4. Encrypt')
show_el.pack()
show_e = Label(root, text = '4.1 Chosen random number r')
show_e.pack()
listbox4 = Listbox(root, height = 1, width = 40)
listbox4.pack()
#For d
show_d = Label(root, text = '4.2 Compute c1 = g^r mod p')
show_d.pack()
listbox5 = Listbox(root, height = 1, width = 40)
listbox5.pack()
#Message m randomly generated
show_m = Label(root, text = '4.3 Compute c2 = m*y^r mod p')
show_m.pack()
listbox6 = Listbox(root, height = 1, width = 40)
listbox6.pack()
#For decryption
show_de = Label(root, text = '5. Derypt C = (c1,c2)')
show_de.pack()
show_dec = Label(root, text = 'm = c2/(c1)^x mod p')
show_dec.pack()
listbox7 = Listbox(root, height = 1, width = 40)
listbox7.pack()

root.mainloop()
