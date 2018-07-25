from .stats import *
from .functional import *

# https://github.com/DavidBuchanan314/english-letter-freqs
byte_freqs = [
	0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
	0.000000, 0.000000, 0.022298, 0.000000, 0.000000, 0.022298, 0.000000, 0.000000,
	0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
	0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
	0.166921, 0.002692, 0.000806, 0.000006, 0.000012, 0.000006, 0.000000, 0.017219,
	0.000454, 0.000454, 0.000525, 0.000000, 0.015315, 0.004441, 0.007198, 0.000143,
	0.000131, 0.000406, 0.000072, 0.000078, 0.000060, 0.000078, 0.000042, 0.000036,
	0.000060, 0.000066, 0.001528, 0.001158, 0.000000, 0.000000, 0.000000, 0.001206,
	0.000012, 0.004309, 0.000746, 0.001116, 0.001444, 0.001868, 0.000800, 0.001152,
	0.001844, 0.004972, 0.000078, 0.000525, 0.000943, 0.001325, 0.001086, 0.001397,
	0.001027, 0.000507, 0.001265, 0.001725, 0.003408, 0.000663, 0.000310, 0.001528,
	0.000036, 0.000848, 0.000006, 0.000024, 0.000000, 0.000024, 0.000000, 0.000024,
	0.000000, 0.054212, 0.009675, 0.016813, 0.031203, 0.090035, 0.013417, 0.016419,
	0.045247, 0.046572, 0.001325, 0.007174, 0.030159, 0.013399, 0.046978, 0.055173,
	0.010719, 0.000806, 0.038198, 0.041666, 0.069420, 0.023080, 0.005437, 0.016091,
	0.001015, 0.014575, 0.000472, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
	0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
	0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
	0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
	0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
	0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
	0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
	0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
	0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
	0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
	0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
	0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
	0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
	0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
	0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
	0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
	0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000
]


# oh god, why did I do this...
likely_bytes = bytes([
	x[1] for x in
	reversed(sorted(map(
		compose(tuple,reversed),
		enumerate(byte_freqs)
	)))
])[:-byte_freqs.count(0)]


freqscore = partial(absdiff, byte_freqs)


def freqs(data):
	f = [0]*0x100
	for x in data:
		f[x] += 1
	return f


englishness = compose(freqscore, freqs)