import socket
import math

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

a = int(input('ENTER 1st num => '))
binary1 = list(map(int, format(a, "b")))

r = 0

while((len(binary1) + r + 1) > pow(2,r)):
    r = r+1

binaryy = [0] * (len(binary1) + r)

j = len(binary1)-1
p = 0

for i in range(0, len(binary1) + r):
    if (pow(2,p) - 1 == i):
        p += 1
    else:
        binaryy[i] = binary1[j]
        j -= 1

# EVEN PARITY

parity = []
    
for j in range(1, r+1):
    list1 = []
    for i in range(1, len(binary1) + r + 1):
        x = format(i, "b")
        if(j <= len(x) and x[0-j] == '1' and binaryy[i-1] == 1):
            list1.append(1)
    if(len(list1)%2 == 0): parity.append(0)
    else: parity.append(1)

j = 0
p = 0
for i in range(0, len(binary1) + r):
    if (pow(2,p) - 1 == i):
        binaryy[i] = parity[j]
        p += 1
        j += 1

binaryy.reverse()
print("HAMMING CODE GENERATED - ", end = " ")
print(binaryy)
msg = ''.join(str(x) for x in binaryy)
print("MESSAGE SENT TO SERVER - " + str(msg))
s.send(bytes(msg,'utf-8'))

msgR = s.recv(1024).decode('utf-8')
print("MESSAGE RECEIVED - " + str(msgR))
