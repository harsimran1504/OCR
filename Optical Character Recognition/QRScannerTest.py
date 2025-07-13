import cv2
import time

vidcapt = cv2.VideoCapture(0)
detector= cv2.QRCodeDetector()

while True:

	startTime = time.time()

	ret, frame = vidcapt.read()

	posText, points, _ = detector.detectAndDecode(frame)

	cv2.putText(frame, posText, (50, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

	cv2.imshow("frame", frame)

	print(f"Time taken: {int(round((time.time()-startTime)*1000))}ms")


	if cv2.waitKey(1) & 0xFF == ord("q"):
		break

vidcapt.release()
cv2.destroyAllWindows()