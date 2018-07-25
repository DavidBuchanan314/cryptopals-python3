from sys import path; path += [".", ".."] # hacky...
from utils import *


if __name__ == "__main__":
	ciphertexts = map(dehex, load_data("8.txt").split("\n"))
	
	for ct in ciphertexts:
		chunks = chunkify(ct, 16)
		if len(set(chunks)) != len(chunks):
			print("AES ECB Ciphertext detected:")
			print(ct.hex())
