import socket
import mainn
from threading import Thread
def server(win):
	sock = socket.socket()
	sock.bind(('', 9091))
	sock.listen(15)
	threads = []
	while 1:
		conn, addr = sock.accept()
		print("New connection:", addr[0])
		f = addr[0]
		print(f)
		win.add_user('user_'+f,f,thr_method='q')
		thread1 = Thread(target=mainn.start, args=(conn, f, win))
		thread1.start()
		threads.append(thread1)
