from Crypto.Cipher import AES


def xor(a, b): # a and b are bytes like
	n = len(b) # maaaybe improve performance?
	return bytes([ai ^ b[i%n] for i, ai in enumerate(a)])


def aesdec(data, key):
	cipher = AES.new(key, AES.MODE_ECB)
	return cipher.decrypt(data)


def aesenc(data, key):
	cipher = AES.new(key, AES.MODE_ECB)
	return cipher.encrypt(data)


def aespad(data):
	padlen = 16-(len(data)%16)
	return data + bytes([padlen]*padlen)


def aespadvalid(data):
	assert(len(data) % 16 == 0)
	padlen = data[-1]
	return data[-padlen:] == bytes([padlen]*padlen)


def aesunpad(data):
	assert(aespadvalid(data))
	return data[:-data[-1]]
