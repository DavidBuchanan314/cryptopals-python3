def xor(a, b): # a and b are bytes like
	n = len(b) # maaaybe improve performance?
	return bytes([ai ^ b[i%n] for i, ai in enumerate(a)])
