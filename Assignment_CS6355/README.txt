All the codes have made use crypto libraries available in python and permission was given by Professor. Lu to use. Each library used has underlying algorithms implemented hence for ease the codes are built as so.
For GUI codes, the GUI has been edited to perform all operations on single button click for ease of execution (Click button multiple times for different outputs)
All codes are run using Python 3
Screenshots have also been attached in case there are any issues with running the code


Libraries needed to download before execution:
    (Pycryptodomex library):                       pip3 install pycryptodomex 
    (gmpy2 library)                                sudo apt-get install -y python3-gmpy2
    (tkinter library for gui)                      sudo apt install python3-tk


To run the files, type the following commands seperately
    1(a)  Extended Euclidean algorithm type:       python3 1a.py
    1(b)  Miller-Rabin primality testing type:     python3 1b.py (Run multiple times for different outputs as shown in screenshots)
    1(c1) RSA GUI type:                            python3 1c1.py
    1(c2) Elgamal GUI type:                        python3 1c2.py
    1(c3) Diffie Hellman GUI type:                 python3 1c3.py
    2.    Vigenere Cipher type:                    python3 2.py 

For Vigenere Cipher, Chi-squared method is sued for frequency analysis of key using key length. Then after obtaining key, divivde the ciphertext into size of keys and analyse using key match with letter technique and decrypt the ciphertext to obtain plaintext 
