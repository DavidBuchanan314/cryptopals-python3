from sys import path; path += [".", ".."] # hacky...
from utils import *

if __name__ == "__main__":
	ciphertexts = map(dehex, load_data("4.txt").split("\n"))
	keyspace = list(range(0x100))
	
	plaintexts = reduce(op.add, [
		[xor(ct, [key]) for key in keyspace]
		for ct in ciphertexts
	])
	
	best_plaintext = min(plaintexts, key=englishness) # I like this code
	
	message = best_plaintext.decode()
	assert(message == "Now that the party is jumping\n")
	print(message.strip())
