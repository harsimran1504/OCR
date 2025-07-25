import cv2
import socket
import numpy
import pickle
# import pickle5 as pickle
# import easyocr

s=socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
ip="192.168.1.42"
port=6969
s.bind((ip,port))

# reader = easyocr.Reader(['en'], gpu=False)

while True:
    x=s.recvfrom(1000000)
    clientip = x[1][0]
    data=x[0]
    loadData=pickle.loads(data)
    showData = cv2.imdecode(loadData, cv2.IMREAD_COLOR)
    cv2.imshow('receiver', showData)

########### EASYOCR ###########

    # grayscale = cv2.cvtColor(loadData, cv2.COLOR_BGR2GRAY)
    # result = reader.readtext(grayscale)
    # text = ""

    # for results in result:
    #     text += results[1] + " "

    # cv2.putText(showData, text, (50, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

    # cv2.imshow("frame", showData)


    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()
