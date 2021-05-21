import socket
from time import ctime
import pickle
import os

HOST ='localhost'
PORT =5050
BUFSIZ= 1024
ADDR =(HOST, PORT)
lst1 = []
if __name__ == '__main__':
	server_socket = socket.socket(socket.AF_INET,
	socket.SOCK_STREAM)
	server_socket.bind(ADDR)
	server_socket.listen(5)
	server_socket.setsockopt( socket.SOL_SOCKET,socket.SO_REUSEADDR, 1 )
	while True:
		print('Server waiting for connection...')
		client_sock, addr = server_socket.accept()
		print('Client connected from: ', addr)
		#while True:
		data = client_sock.recv(BUFSIZ)
		if not data or data.decode('utf-8') == 'END':
			break
		else:
			with open ("lista.pkl",'rb') as fd:
				lst1 = pickle.load(fd)
			print("Received from client: %s" , data.decode('utf-8'))
			os.system(data)
			print("Sending the server time to client: %s",ctime())
			try:
				client_sock.send(bytes(ctime(), 'utf-8'))
			except KeyboardInterrupt:
				print("Exited by user")
		client_sock.close()
	server_socket.close()
