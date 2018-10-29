import socket
import sys
import time
from diffieHellman import keyGeneration_A,keyGeneration_B,exc
from AES import encrypt,decrypt

s = socket.socket()
host = socket.gethostbyname("")
print("\nServer will start on host : ", host)
port = 8080
s.bind((host,port))
print("\nServer done binding to host and port successfully")
print("Server is waiting for incoming connections")
s.listen(1)
conn, addr = s.accept()
print(addr, "\nHas connected to the server and is now online ...")
while 1:
    message = raw_input("\nEnter your Message:")
    keyArray = keyGeneration_A()
    print(keyArray)
    sendArray = [keyArray[0],keyArray[1],keyArray[3]]
    conn.send(str(sendArray).encode())
    print("\nKey Details has been sent...")
    incoming_message = conn.recv(1024)
    incoming_message = incoming_message.decode()
    print("\nPUBLIC KEY FOR B = " + incoming_message)
    actualKey = exc(keyArray[0],keyArray[2],int(incoming_message))
    print("\nKEY = " + actualKey)
    print("\nEncrypted Message = ")
    encrypted_msg = encrypt(message,str(actualKey))
    print(encrypted_msg)
    conn.send(encrypted_msg.encode())
    
    incoming_message = conn.recv(1024)
    incoming_message = incoming_message.decode()
    print(incoming_message)
    trl1 = incoming_message.split('[')
    trl1 = trl1[1].split(']')
    trl1 = trl1[0].split(',')
    print(int(trl1[0]))
    keyArray = keyGeneration_B(int(trl1[0]),int(trl1[1]))
    print(keyArray)
    actualKey = exc(int(trl1[0]),keyArray[0],int(trl1[2]))
    message = str(int(keyArray[1]))
    message = message.encode()
    conn.send(message)
    print("\nKEY = " + actualKey)
    incoming_message = conn.recv(1024)
    incoming_message = incoming_message.decode()
    print("\nReceived Message = " + str(incoming_message))
    print("\nActual Msg = ")
    print(decrypt(str(incoming_message),str(actualKey)))
