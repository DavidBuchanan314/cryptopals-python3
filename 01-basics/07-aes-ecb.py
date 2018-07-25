from sys import path; path += [".", ".."] # hacky...
from utils import *


if __name__ == "__main__":
	ciphertext = d64(load_data("7.txt"))
	plaintext = aesunpad(aesdec(ciphertext, b"YELLOW SUBMARINE")).decode()
	print(plaintext)
