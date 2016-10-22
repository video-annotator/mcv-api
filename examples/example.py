import cv2, pyforms

from mcvgui.filters.adaptative_threshold import AdaptativeThreshold

#mask = PolygonsMask(polygons_file='/home/ricardo/bitbucket/geometry-designer/arena.dat')
#mask = AdaptativeThreshold()

mask = pyforms.startApp(AdaptativeThreshold)


cap = cv2.VideoCapture('/home/ricardo/Desktop/01Apollo201403210900/01Apollo201403210900MergedCascata.MP4')

while cap.isOpened():
	ret, frame = cap.read()

	frame = mask.processflow(frame)
	#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	cv2.imshow('frame',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
