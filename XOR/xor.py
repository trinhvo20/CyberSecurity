
# Get the key from file 'key':
f = open("key", "rb")
#f = open("key2", "rb")
k = bytearray(f.read())

# Get the message (plaintext or ciphertext) from redirection:
import sys
m = bytearray(sys.stdin.buffer.read())

l = len(m)

# Create a buffer bytearray 'result' with length of message:
result = bytearray(l)

# message XOR key:
for i in range(l):
    result[i] = m[i] ^ k[i]

sys.stdout.buffer.write(result)


"""
$ python xor.py < plaintext > ciphertext.
This would take the contents of the file plaintext, XOR (encrypt) it with the contents of
the file key, and store the resulting ciphertext to the file ciphertext.

The reverse: 
$ python xor.py < ciphertext
would take the contents of the file ciphertext, XOR (decrypt) it with the contents of the file key, and send the resulting plaintext to stdout.
"""

"""
Result:
$ python xor.py < ciphertext
Sometimes i'll start a sentence and I don't even know where it's going. I just hope i find it along the way.
"""