import socket
import pickle
HOST ='localhost'
PORT =5050
BUFSIZ= 4096
ADDR =(HOST, PORT)
lst1 = [1,2,3,4]

if __name__ == '__main__':
	client_sock = socket.socket(socket.AF_INET,
	socket.SOCK_STREAM)
	client_sock.connect(ADDR)
	while True:
		data = 'python3 im_msg.py lst1'
		if not data:
			break
		client_sock.send(data.encode('utf-8'))
		data = client_sock.recv(BUFSIZ)
		with open ("lista.pkl",'wb') as fm:
			pickle.dump(lst1,fm,pickle.HIGHEST_PROTOCOL)
		if not data:
			break
		print(data.decode('utf-8'))
	client_sock.close()
