import base64

"""
encoders take a bytes like object, and return a string
decoders take a string like object, and return bytes
"""

# base64
def b64(data):
	return base64.b64encode(bytes(data)).decode()


d64 = base64.b64decode


# hexadecimal
def enhex(data):
	return bytes(data).hex()


dehex = bytes.fromhex
