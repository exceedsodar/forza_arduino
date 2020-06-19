import logging
import socket
import time, sys
log = logging.getLogger('udp_server')
import struct
msgFromClient = "Hello UDP Server"
bytesToSend = str.encode(msgFromClient)

forza_format = 'iIfffffffffffffffffffffffffffffffffffffffffffffffffffiiiiifffffffffffffffffHBBBBBBbbb'
'''

'''
def udp_server(host='192.168.88.18', port=1234):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serverAddressPort=(host,port)
    log.info("Listening on udp %s:%s" % (host, port))
    s.bind((host, port))
    while True:
        bytesAddressPair = s.recvfrom(1024)

        message = bytesAddressPair[0]

        address = bytesAddressPair[1]

        clientMsg = "Message from Client:{}".format(message)
        clientIP = "Client IP Address:{}".format(address)

        print(clientMsg)
        print(clientIP)
        s.sendto(bytesToSend, address)

def test_send(host='192.168.88.18', port=1234):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serverAddressPort=(host,port)
    log.info("Listening on udp %s:%s" % (host, port))
    s.bind((host, port))
    while True:
        bytesAddressPair = s.recvfrom(1024)

        message = bytesAddressPair[0]

        address = bytesAddressPair[1]

        clientMsg = "Message from Client:{}".format(message)
        clientIP = "Client IP Address:{}".format(address)

        print(clientMsg)
        print(clientIP)
        s.sendto(bytesToSend, address)

def get_all_data():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    log.info("Listening on udp %s:%s" % (host, port))
    s.bind((host, port))
    bytesAddressPair = s.recvfrom(1024)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientMsg = "Message from Client:{}".format(message)
    clientIP = "Client IP Address:{}".format(address)
    print(clientMsg)
    print(clientIP)
    return clientMsg

def get_data(int=0,test=b""):
    data=-1
    if int>81 or int<0:
        raise Exception("Invalid index")
    else:
        if test:
            all_data=test
        else:
            all_data = get_all_data()
        data = all_data[int*4:int*4+4]
    return data

def convert_data(format="i",data=b""):
    res=0
    try:
        res = struct.unpack(format,data)
    except Exception as e:
        pass
    return res and res[0] or 0

def get_forza_data(i=0,test=b""):
    data = get_data(i,test)
    res = convert_data(forza_format[i],data)
    return res

# test=b"\x01\x00\x00\x00\x0e\x14\x87\x0f\xfb\x9f\x0cF\xf8\xffGDKI\x05F\x12\x8e\x88@\x1f\xac_\xc1\x8cK\x9a\xbf\xa2;\x9fA\x80L;\xc1?'\x1dB\xa0\t\x05>$\xbc\x1e\xbeqiA\xbdD\\N?\xe5\xa0\x18=\xd6:\x7f\xbe\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x93d1Csd1C\xcf50C\x9750C\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xb4x\x8f\xbd\xb4x\x8f\xbd(\\\x8f\xbd(\\\x8f\xbdm\x01\x00\x00\x04\x00\x00\x00T\x03\x00\x00\x02\x00\x00\x00\x04\x00\x00\x00#\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00)\xbc\x92\xc3ao\x07C\xff\x8a\x0e\xc5oI6BN\xe2\xa3H@Q\xbcC\xd6\xf3\x8eBnd\x8dB\x97=\x9fB\x97=\x9fB\xfa\xa0\x8fA\x00\x00\x80?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xed\x93\xdfC\x00\x00\x00\xff\x00\x00\x00\x04\x00\x81\x00\x00"
# i=61

# res = get_forza_data(i,test)
# print("\r"+str(res),end="")
# FORMAT_CONS = '%(asctime)s %(name)-12s %(levelname)8s\t%(message)s'
# logging.basicConfig(level=logging.DEBUG, format=FORMAT_CONS)

def send_sriel_test():
    ser = serial.Serial()
    ser.baudrate = 19200
    ser.port = 'COM1'  # write port on which you connected your Arduino
    ser.write(b'sending string to Arduino')
    ser.close()

def monitor_data(i=0,host='192.168.88.13',port=1024):
    serverAddressPort = (host,port)
    print("create socket")
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print("Sent.. Listening on udp %s:%s" % (host, port))
    s.sendto(bytesToSend, serverAddressPort)


    while True:
        bytesAddressPair = s.recvfrom(1024)
        message = bytesAddressPair[0]
        address = bytesAddressPair[1]
        res = convert_data(forza_format[i], message)
        print("\r" + str(res), end="")

monitor_data(i=61)