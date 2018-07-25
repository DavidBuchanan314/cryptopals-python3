from glob import glob
from os import system
import sys

PYTHON = sys.executable

total = 64
passed = 0
failed = 0

for chal in range(1, total+1):
	print("[*] Testing challenge {}".format(chal))
	path = glob("*/{:02x}-*.py".format(chal))
	if not path:
		print("[-] INCOMPLETE")
		continue
	else:
		assert(len(path) == 1)
		path = path[0]
	
	retcode = system(PYTHON + " " + path)
	
	if retcode:
		print("[!] FAILED")
		failed += 1
	else:
		print("[+] PASSED!")
		passed += 1

print("\n[*] SUMMARY:")
print("{} tests passed.".format(passed))
print("{} tests failed.".format(failed))
print("{} solutions did not exist.".format(total-(passed+failed)))
