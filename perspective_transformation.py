import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
	_, frame = cap.read()

	cv2.circle(frame,(155,120),5,(255,0,0),-1)
	cv2.circle(frame,(480,120),5,(255,0,0),-1)
	cv2.circle(frame,(20,475),5,(255,0,0),-1)
	cv2.circle(frame,(620,475),5,(255,0,0),-1)

	points1 = np.float32([[155,120],[480,120],[20,475],[620,475]])
	points2 = np.float32([[0,0],[500,0],[0,600],[500,600]])

	mat = cv2.getPerspectiveTransform(points1,points2)

	result = cv2.warpPerspective(frame,mat, (500,600))

	cv2.imshow("Frame",frame)
	cv2.imshow("PerspectiveTransform",result)
	# print(_)

	key = cv2.waitKey(1)
	if key == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()