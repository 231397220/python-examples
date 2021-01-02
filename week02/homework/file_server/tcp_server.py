#!/usr/bin/env python
# coding: utf-8

import socket


TCP_IP = '0.0.0.0'
TCP_PORT = 10001
BUFFER_SIZE = 1024

s = socket.socket()
s.bind((TCP_IP, TCP_PORT))
s.listen(10)
with open('received_file', 'wb') as f:
    print('file opened')
    conn, addr = s.accept()
    while True:
        print('receiving data...')
        data = conn.recv(BUFFER_SIZE)
        f.write(data)
        print('data=%s', (data))
        if not data:
            f.close()
            print('file close()')
            break
        # write data to a file

print('Successfully get the file')
s.close()
print('connection closed')
