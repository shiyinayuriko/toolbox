import sys
import base64

if(sys.argv.__len__() == 1):
    sourceFile = input("input source file\n")
else:
    sourceFile = sys.argv[1]

counter = [0,0]
cardlist = []
currentCounter = 0

with open(sourceFile, "r", encoding="utf8") as f:
    for line in f:
        if line.strip().isdigit():
            card = int(line)
            cardlist.append(card)
            counter[currentCounter] += 1
        elif line.startswith("!side"):
            currentCounter+=1


print(cardlist)
print(counter)

byteArray = bytearray()
for c in counter:
    byteArray+= c.to_bytes(4,byteorder="little")
for c in cardlist:
    byteArray+= c.to_bytes(4,byteorder="little")

b64 = base64.b64encode(byteArray)
print(b64)