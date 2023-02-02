from tkinter import *
import random
from typing import List
import gmpy2
from Crypto.Util import number
from math import gcd as bltin_gcd

#Find e
def set_e(a,b):
    phi_n = (a-1)*(b-1)
    rand_state = gmpy2.random_state(random.randint(1,10))
    e = gmpy2.mpz_random(rand_state,phi_n) 
    while(gmpy2.gcd(e,phi_n) != 1):
        e = gmpy2.mpz_random(rand_state,phi_n)
    return e  

#Execute RSA    
def RSA():
    r = 1
    while(r == 1):
        num1 = random.randrange(1000,5000)
        num2 = random.randrange(1000,5000)
        if(gmpy2.is_prime(num1) and gmpy2.is_prime(num2)  == True):
            r = 0
        else:
            continue
    listbox1.insert(0,num1)
    listbox2.insert(0,num2)
    #p*q
    mul = num1*num2
    #(p-1)*(q-1)
    phi_n = (num1-1)*(num2-1)
    listbox3.insert(0,mul)
    #Find e using function
    e = set_e(num1,num2)
    listbox4.insert(0,e)
    #Find d using function
    d = gmpy2.invert(e,phi_n)
    listbox5.insert(0,d)
    #Generate random message
    m = random.randrange(1,10000)
    listbox6.insert(0,m)
    #Encryption
    c = gmpy2.powmod(m,e,mul) 
    listbox7.insert(0,c)
    #Decryption
    m_obt = gmpy2.powmod(c,d,mul)
    listbox8.insert(0,m_obt)

  

root = Tk()
root.title('RSA Encryption/Decryption')

#To generate p and q
show = Label(root, text = '1. Generate primes p and q (in range 1000 and 5000)')
show.pack()
#For q
button_p = Button(root, text = "Execute", command = RSA)
button_p.pack()
show_p = Label(root, text = 'Value of p')
show_p.pack()
listbox1 = Listbox(root, height = 1, width = 40)
listbox1.pack()
#For q
show_q = Label(root, text = 'Value of q')
show_q.pack()
listbox2 = Listbox(root, height = 1, width = 40)
listbox2.pack()
#For p*q
show_pq = Label(root, text = '2. n (p*q) is')
show_pq.pack()
listbox3 = Listbox(root, height = 1, width = 40)
listbox3.pack()
#For e
show_e = Label(root, text = '3. Set public key e is')
show_e.pack()
listbox4 = Listbox(root, height = 1, width = 40)
listbox4.pack()
#For d
show_d = Label(root, text = '4. d is')
show_d.pack()
listbox5 = Listbox(root, height = 1, width = 40)
listbox5.pack()
#Message m randomly generated
show_m = Label(root, text = '5. Input message m')
show_m.pack()
listbox6 = Listbox(root, height = 1, width = 40)
listbox6.pack()
#For encryption 
show_enc = Label(root, text = '6. Encrypt c = m^e mod n')
show_enc.pack()
listbox7 = Listbox(root, height = 1, width = 40)
listbox7.pack()
#For decryption
show_dec = Label(root, text = '7. Decrypt m = c^d mod n')
show_dec.pack()
listbox8 = Listbox(root, height = 1, width = 40)
listbox8.pack()

root.mainloop()
