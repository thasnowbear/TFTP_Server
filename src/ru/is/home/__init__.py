
#           opcode  operation
#             1     Read request (RRQ)
#             2     Write request (WRQ)
#             3     Data (DATA)
#             4     Acknowledgment (ACK)
#             5     Error (ERROR)

import socket, sys, struct, string

host = sys.argv[1]
transfermode = sys.argv[2]
filename = sys.argv[3]
#UDP_PORT = sys.argv[4]

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
mode = "octet"

def read ():
    nextblock = 1
    lastpkt = s
    
    if len(data) == 516:
        Receiving = True;
    #While loop to recvieve all packages.
    while Receiving:
        #if last package was just received - sending last ACK pack.
        if len(data) != 516:
            Receiving = False;
            ack = struct.pack("!HH", 4 , nextblock)
            sock.sendto(ack,(UDP_IP,svar[1]))
        #receiving packages.
        else:
            ack = struct.pack("!HH", 4 , nextblock)
            sock.sendto(ack,(UDP_IP,svar[1]))
            data, svar = sock.recvfrom(1024)
            strong += data [4:]
            nextblock += 1

def write ():
    #CREATE FILE AND WRITE TO IT.
    fo = open(filename, "wb")
    fo.write(strong)
    #Closing open files and socket
    fo.close()
    sock.close()
    print('File Recieved')

def request (trmode, filenm):
    format = "!H%ds" % (len(filenm)+1)
    format += "%ds" % (len(mode)+1)
    s = struct.pack(format, trmode , filenm, mode)
    sock.sendto(s,(host,69))
    data, svar = sock.recvfrom(1024)
    port = svar[1]
    if trmode == 1:
        read(port, filenm)
    elif trmode == 2:
        write(port, filenm)

if transfermode == "lesa":
    request(1, filename)
elif transfermode == "skrifa":
    request(2, filename)
else
    print('Please use Servername Read/Write FileName')

   