import sys
import numpy as np

print("Mensaje recibido")
def im_msg(msg):
	print(msg)
	return 

if __name__=="__main__":
	S2 = 0
	
	Ar=np.array(np.mat(sys.argv[1]))
	mensaje = im_msg(Ar)
	print(Ar)
	S2 = np.sum(Ar)
	print(S2)
	#mensaje=im_msg(sys.argv[1])
