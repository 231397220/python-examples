#!/usr/bin/env python
# coding: utf-8

import socket

'''
建立tcp连接后发送执行的文件
'''

TCP_IP = '127.0.0.1'
TCP_PORT = 10001
SEND_FILE_NAME = "sam_text.txt"
BUFFER_SIZE= 1024

class SendMessages():
    def __init__(self, ip, port, sock):
        self.ip = ip
        self.port = port
        self.sock = sock
        print(f"New thread started for {ip} : {str(port)} ")

    def send_file(self, SEND_FILE_NAME):
        with open(SEND_FILE_NAME, 'rb') as f:
            while True:
                data = f.read(BUFFER_SIZE)
                while (data):
                    self.sock.send(data)
                    #print('Sent ',repr(l))
                    data = f.read(BUFFER_SIZE)
                if not data:
                    f.close()
                    self.sock.close()
                    break


tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def main():
    while True:
        print(f"Got connection {TCP_IP},{TCP_PORT}")
        tcpsock.connect((TCP_IP, TCP_PORT))
        new_sock = SendMessages(TCP_IP, TCP_PORT, tcpsock)
        new_sock.send_file(SEND_FILE_NAME)


if __name__ == "__main__":
    main()
