from sys import path; path += [".", ".."] # hacky...
from utils import *

if __name__ == "__main__":
	data = "1c0111001f010100061a024b53535009181c"
	key = "686974207468652062756c6c277320657965"
	result = xor(dehex(data), dehex(key)).hex()
	
	assert(result == "746865206b696420646f6e277420706c6179")
	print(result)
