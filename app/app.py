import socket
import mainn
from PyQt5 import QtWidgets

def conn_w_ip(name,ip,port,win):

    sock = socket.socket()

    try:
        sock.connect((ip, port))
        win.add_user(name, ip,sock)
    except socket.error as exc:
        print("HELLO")
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("ERROR")
        msg.setInformativeText(str(exc))
        msg.setDetailedText("You may try again")
        print("WTF???")
        msg.exec_()








