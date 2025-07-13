import cv2
import pytesseract
try:
    from PIL import Image
except ImportError:
    import Images

# https://www.youtube.com/watch?v=Y7XBsFzByTQ

# Reference this video and create queuing system https://www.youtube.com/watch?v=EkSaIJTruTA&t=366s

pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract"

vidcapt = cv2.VideoCapture(0)

while True:

	ret, frame = vidcapt.read()

	frameH, frameW, _ = frame.shape

	grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	text = pytesseract.image_to_string(grayscale)

	box = pytesseract.image_to_boxes(grayscale)

	for boxes in box.splitlines():
		boxes = boxes.split(' ')
		x, y, w, h = int(boxes[1]), int(boxes[2]), int(boxes[3]), int(boxes[4])
		cv2.rectangle(frame, (x, frameH-y), (w, frameW-h), (0, 0, 255), 3)

	cv2.putText(frame, text, (50, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

	cv2.imshow("frame", frame)
	cv2.imshow("grayscale", grayscale)


	if cv2.waitKey(1) == ord("q"):
		break

vidcapt.release()
cv2.destroyAllWindows()