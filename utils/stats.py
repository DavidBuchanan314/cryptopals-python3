# relative sum of absolute differences
def absdiff(a, b):
	assert(len(a) == len(b))
	return sum([abs(x-y)**0.1 for x, y in zip(a, b)])/len(a)


def average(data):
	return sum(data)/len(data)
