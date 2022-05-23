import rsa
from rsa import blocksize
import socket
import time


def end_dialog(sock):
    sock.close()
    print("Hvatit")


def recv_block(sock):
    n = 0
    data = bytearray(blocksize)
    while n < blocksize:
        data1 = bytearray(blocksize - n)
        n1, addr = sock.recvfrom_into(data1, blocksize - n)
        data[n:n + n1] = data1[:n1]
        n += n1
    return data


def update_f(file, s, win):
    f = open(file, 'a')
    f.write(s + '\n')
    f.close()
    win.new_msg(file)


def recieve(sock, d, n, file, win):
    while True:
        data = (1).to_bytes(blocksize, 'little', signed=False)
        message = []
        while int.from_bytes(data, 'little', signed=False) != n + 1:
            try:
                data = recv_block(sock)
            except:
                print("Connection is closed")
                return
            message.append(data)
        data = rsa.decode_rsa_s(message, d, n)
        if data == "/stop":
            break

        update_f(file, "Ne ty:" + data, win)


def sendd(sock, e, n, s):
    s1 = rsa.encode_rsa_s(s, e, n)
    try:
        for i in s1:
            sock.send(i)
    except:
        print("Connetion closed4")
        return


def start(sock, file, win):
    s = "123"
    try:
        f = open("keys")
    except:
        rsa.gen_keys()
        f = open("keys")
    finally:
        e, n, d = map(int, f.read().split('\n'))
    sock.send(e.to_bytes(blocksize, 'little', signed=False))
    e = int.from_bytes(sock.recv(blocksize), 'little', signed=False)
    sock.send(n.to_bytes(blocksize, 'little', signed=False))
    n2 = int.from_bytes(sock.recv(blocksize), 'little', signed=False)
    print(e,n2)
    recieve(sock, d, n, file,win)
