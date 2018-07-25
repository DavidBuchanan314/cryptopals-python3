from sys import path; path += [".", ".."] # hacky...
from utils import *


def apply_pairwise(array, func):
	return [func(a, b) for a, b in zip(array[:-2], array[1:-1])]


def evaluate_keylen(ciphertext, keylen):
	return average(
		apply_pairwise(chunkify(ciphertext, keylen), hamming)
	)/keylen


if __name__ == "__main__":
	assert(hamming(b"this is a test", b"wokka wokka!!!") == 37)
	
	ciphertext = d64(load_data("6.txt"))
	
	keylen = min(range(2, 40), key=partial(evaluate_keylen, ciphertext))
	assert(keylen == 29)
	
	chunks = zip(*chunkify(ciphertext, keylen))
	key = [min(range(0x100), key=lambda k:englishness(xor(c, [k]))) for c in chunks]
	assert(bytes(key) == b"Terminator X: Bring the noise")
	
	plaintext = xor(ciphertext, key).decode()
	print(plaintext)
