from mcv_api.masks.polygons_mask import PolygonsMask
import cv2

mask = PolygonsMask(polygons_file='/home/ricardo/bitbucket/geometry-designer/arena.dat')

cap = cv2.VideoCapture('/home/ricardo/bitbucket/single-fly-tracker/Circle_and_Square.avi')

while cap.isOpened():
	ret, frame = cap.read()

	frame = mask.process(frame)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	cv2.imshow('frame',gray)
	if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
