
import sys

string = sys.stdin.read()
binaryString = string.replace("\n","")
print(binaryString)

bits = 8

if len(binaryString) % 7 == 0:
    bits = 7

resultString = ''

for i in range(0, len(binaryString), bits):
    resultString += chr(int(binaryString[i:i + bits], 2))

# int(string,2): convert string to base 2
# chr() to convert binary to ASCII

sys.stdout.write(resultString + "\n")