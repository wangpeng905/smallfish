#/usr/bin/env python3

import sys
import hashlib
import binascii
import base64

# Usage: python3 md5sum_sha1sum.py <inputfile> 

def SHA1FileWithName(fineName, block_size=64 * 1024):
	with open(fineName, 'rb') as f:
		sha1 = hashlib.sha1()
		while True:
			data = f.read(block_size)
			if not data:
				break
			sha1.update(data)
		retsha1 = binascii.b2a_hex(sha1.digest())
	return retsha1

def MD5FileWithName(fineName, block_size=64 * 1024):
	with open(fineName, 'rb') as f:
		md5 = hashlib.md5()
		while True:
			data = f.read(block_size)
			if not data:
				break
			md5.update(data)
		retmd5 = binascii.b2a_hex(md5.digest())
	return retmd5

print("MD5:",MD5FileWithName(sys.argv[1]))
print("SHA1:",SHA1FileWithName(sys.argv[1]))
