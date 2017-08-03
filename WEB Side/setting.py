from bluetooth import *

HOST = ''          # Symbolic name
PORT = 999999   # Non-privileged port
s=BluetoothSocket( RFCOMM )
print(s)
s.bind((HOST, PORT))
s.listen(1)

conn, addr = s.accept()

print('Connected by', addr)
while True:
    data = conn.recv(1024)
    print(data)
    if not data: break
   # conn.send(data)
conn.close()