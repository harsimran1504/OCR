import cv2
import socket
import pickle5 as pickle
import os
import numpy as np

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF,1000000)
server_ip= "192.168.1.163" #ip of reciever, laptop ip is 192.168.1.42
server_port= 6969	

vidcapt = cv2.VideoCapture(0)
while True:
	ret, frame = vidcapt.read()
	cv2.imshow('sending', frame)
	ret, buffer = cv2.imencode(".jpg",frame,[int(cv2.IMWRITE_JPEG_QUALITY),30])
	x_as_bytes = pickle.dumps(buffer)
	s.sendto((x_as_bytes),(server_ip,server_port))
	
	if cv2.waitKey(1) == ord('q'):
		break

cv2.destroyAllWindows()
vidcapt.release()
