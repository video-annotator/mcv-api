import cv2
from mcvapi.mcvbase import MCVBase
from mcvapi.blobs.blob import Blob

class FindBlobs(MCVBase):
   
	def __init__(self, **kwargs):
		super(FindBlobs, self).__init__(**kwargs)
		self._param_findblobs_min_area = 0
		self._param_findblobs_max_area = 100000000

	def process(self, frame):
		_, contours, _ = cv2.findContours(frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		
		objectsFound = []
		for cnt in contours:
			m = cv2.moments(cnt); m00 = m['m00']
			
			if self.findblobs_min_area <= m00 <= self.findblobs_max_area:
				if m00!=0: centroid = ( int(round(m['m10']/m00) ), int(round(m['m01']/m00)) )
				else: centroid = (0,0)

				box = cv2.boundingRect(cnt)
				p1, p2 = (box[0], box[1]), (box[0]+box[2], box[1]+box[3])
		
				obj = Blob()
				obj._contour    = cnt
				obj._bounding   = (p1, p2)
				obj._area       = m00
				obj._centroid   = centroid
				objectsFound.append( obj )

		return objectsFound

	def processflow(self, frame):
		frame = super(FindBlobs, self).processflow(frame)
		return self.process(frame)


	#####################################################################
	### PROPERTIES ######################################################
	#####################################################################

	@property
	def findblobs_min_area(self): return self._param_findblobs_min_area
	
	@property
	def findblobs_max_area(self): return self._param_findblobs_max_area