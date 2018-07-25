from sys import path; path += [".", ".."] # hacky...
from utils import *

if __name__ == "__main__":
	data = dehex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
	keyspace = list()
	
	best_key  = min(range(0x100), key=lambda k:englishness(xor(data, [k])))
	
	message = xor(data, [best_key]).decode()
	assert(message == "Cooking MC's like a pound of bacon")
	print(message)
