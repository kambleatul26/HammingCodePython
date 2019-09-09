import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print("Connection established with {}".format(address))

    msg = clientsocket.recv(1024).decode('utf-8')
    print("MESSAGE RECEIVED - " + str(msg))

    arr = list(msg)
    arr = list(map(int, arr))
    arr.reverse()
    ansParity = []

    r = 0
    while((len(arr) + 1) > pow(2,r)):
        r = r+1

    for j in range(1, r+1):
        sum = 0
        for i in range(1, len(arr)+1):
            x = format(i, "b")
            if(j <= len(x) and x[0-j] == '1'):
                sum += arr[i-1]

        if(sum%2 == 0): ansParity.append(0)                #EVEN PARITY USED
        else: ansParity.append(1)

    ansParity.reverse()
    print(ansParity)
    tempString = ''.join(str(x) for x in ansParity)
    num = int(tempString, 2)
    if(num == 0):
        print("NO ERROR")
        clientsocket.send(bytes("NO ERROR", 'utf-8'))

    else:
        print("ERROR at INDEX => " + str(num))
        clientsocket.send(bytes("ERROR at INDEX => " + str(num), 'utf-8'))
        
    clientsocket.close()
