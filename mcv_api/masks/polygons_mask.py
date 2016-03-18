from mcv_api.OTPBase import OTPBase
import numpy as np

class PolygonsMask(OTPBase):
	
	def __init__(self, polygons_file=None):
		self._polygons_mask = None
		self._polygons      = None

		if polygons_file is not None: self.load(polygons_file)




	def load(self, polygons_file):
		self._polygons = []
		with open(polygons_file) as file:

			for line in file:
				vals = line.split(';')
				name = values[0]
				poly = eval(values[1])
				self._polygons.append( (name, poly) )

			self._polygons = np.array(self._polygons)


	def compute(self, frame):
		if self._polygons_mask==None:
			self._polygons_mask = np.zeros_like(frame)
			cv2.fillPoly( self._polygons_mask, self._polygons, (255,255,255) )
		return cv2.bitwise_and(frame, self._polygons_mask)

	def process(self, frame):
		frame = super(OTPMaskFromGeometry, self).process(frame)
		return OTPMaskFromGeometry.compute(self, frame)	