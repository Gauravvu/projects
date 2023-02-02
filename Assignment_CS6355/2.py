letters = 'abcdefghijklmnopqrstuvwxyz'

# Frequencies of each letter given in question
letter_frequences = [0.08200, 0.01500, 0.02800, 0.04300, 0.12700, 0.02200, 0.02000,
					  0.06100, 0.0700, 0.00200, 0.00800, 0.04000, 0.02400, 0.06700,
					  0.07500, 0.01900, 0.00100, 0.06000, 0.06300, 0.09100, 0.02800,
					  0.01000, 0.02400, 0.00200, 0.02000, 0.00100]

#Using chi-squared test for frequency analysis
def freq_analysis(sequence):
	chisqr = [0] * 26

	for i in range(26):

		chisqr_sum = 0.0

		#offset = [(((seq_ascii[j]-97-i)%26)+97) for j in range(len(seq_ascii))]
		offset = [chr(((ord(sequence[j])-97-i)%26)+97) for j in range(len(sequence))]
		v = [0] * 26
		# count the numbers in ascii
		for l in offset:
			v[ord(l) - ord('a')] += 1
		# divide based on length of key
		for j in range(26):
			v[j] *= (1.0/float(len(sequence)))

		# Compare frequencies
		for j in range(26):
			chisqr_sum+=((v[j] - float(letter_frequences[j]))**2)/float(letter_frequences[j])

		chisqr[i] = chisqr_sum

	move = chisqr.index(min(chisqr))

	# return the letter
	return chr(move+97)

def get_key(ciphertext, key_length):
	key = ''
	# Calculte letter frequency
	for i in range(key_length):
		sequence=""
		# divide into sequences
		for j in range(0,len(ciphertext[i:]), key_length):
			sequence+=ciphertext[i+j]
		key+=freq_analysis(sequence)

	return key

# Returns the plaintext given the ciphertext and a key
def decryption(ciphertext, key):
	# Create array of ascii value of ciphertext and key
	cipher_ascii = [ord(letter) for letter in ciphertext]
	key_ascii = [ord(letter) for letter in key]
	plain_ascii = []

	# Turns each ascii value of the ciphertext into the ascii value of the plaintext
	for i in range(len(cipher_ascii)):
		plain_ascii.append(((cipher_ascii[i]-key_ascii[i % len(key)]) % 26) +97)

	# Turns the array of ascii values into characters
	plaintext = ''.join(chr(i) for i in plain_ascii)
	return plaintext

def main():
	
  ciphertext_raw = "OOFWGTXYE - FKVY MHIULX WTOGLE TH AMBELFS MV XAIAAPL, KQSDAAPL,ZQROLD AGK YUVO YOKL - FONJT NXHDLR LHEKF MSILOT HM PABSK LBMQ IG AADTF’E MHKQRG DAREK. FEVOZOEVSY BZ BOPLDEW UAT CBET UF EIEPOOG JTIIZ MNW LXEVADIVPFY, UBF BR ATE VYQAMPHIMF MNW PZGXUGIMF AF VVYPNAQR LJUEGAUSMZ IHH ADAGZXAML EOVPQTR’Z ZEXKE AGK IAGAE IGAA PKVPUVAE TAHF CTUUMIYAVX IATA ZACBLFY TUP TAL QCHUAMR"

  # Filters the text so it is only alphanumeric characters, and lowercase
  ciphertext = ''.join(x.lower() for x in ciphertext_raw if x.isalpha())	
  key_length = 4
  key = get_key(ciphertext, key_length)
  plaintext = decryption(ciphertext, key)

  print("Key is: ", key)
  print("Plaintext is: ",plaintext)

if __name__ == '__main__':
	main()