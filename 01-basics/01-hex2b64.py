from sys import path; path += [".", ".."] # hacky...
from utils import *

hex2b64 = compose(b64, dehex) # functional programming FTW

if __name__ == "__main__":
	data = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
	result = hex2b64(data)
	
	assert(result == "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t")
	print(result)
