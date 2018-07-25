# Global namespace pollution party!
from .codecs import *
from .functional import *
from .crypto import *
from .english import *
from .stats import *
import os


def load_data(name, mode="r"):
	path = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "data", name)
	return open(path, mode).read()


def chunkify(data, n):
	return [data[i:i+n] for i in range(0, len(data)-n, n)]
