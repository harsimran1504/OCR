import cv2
import socket
import pickle5 as pickle
import easyocr
import time
import threading


def get_time_ms():
    return int(round(time.time() * 1000))


s=socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
port=6969
s.bind((socket.gethostname(),port))

reader = easyocr.Reader(['en'], gpu=True)

global keep_connecting
keep_connecting = True

global latest_data
latest_data = None

def receive_data():
    global keep_connecting
    global latest_data
    while keep_connecting:
        latest_data = s.recvfrom(1000000)

connection_thread = threading.Thread(target=receive_data, name="connection thread")
connection_thread.start()

while True:
    if(latest_data is None):
        continue
    x = latest_data
    clientip = x[1][0]
    data=x[0]
    loadData=pickle.loads(data)
    showData = cv2.imdecode(loadData, cv2.IMREAD_COLOR)
    
    det=cv2.QRCodeDetector()
    val, pts, st_code=det.detectAndDecode(showData)

    cv2.putText(showData, val, (50, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

    cv2.imshow("frame", showData)


    if cv2.waitKey(1) == ord('q'):
        keep_connecting = False
        connection_thread.join()
        s.close()
        break
        
cv2.destroyAllWindows()