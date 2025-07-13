import cv2
import easyocr

reader = easyocr.Reader(['en'], gpu=False)
vidcapt = cv2.VideoCapture(0)

while True:

    ret, frame = vidcapt.read()

    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    result = reader.readtext(grayscale)
    text = ""

    for results in result:
        text += results[1] + " "

    cv2.putText(frame, text, (50, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

    cv2.imshow("frame", frame)    

    if cv2.waitKey(1) == ord("q"):
        break

vidcapt.release()
cv2.destroyAllWindows()