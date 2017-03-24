from mcvapi.mcvbase import MCVBase
import numpy as np, cv2


class PolygonsMask(MCVBase):
	
	def __init__(self, **kwargs):
		self._param_polygons_mask  = None
		self._param_polygons_polys = None

	def process(self, frame):		
		if self._param_polygons_mask is None:
			self._param_polygons_mask = np.zeros_like(frame)
			cv2.drawContours(self._param_polygons_mask, self._param_polygons_polys, -1, (255,255,255), -1)		
		return cv2.bitwise_and(frame, self._param_polygons_mask)

	def processflow(self, frame):
		frame = super(PolygonsMask, self).processflow(frame)
		return PolygonsMask.process(self, frame)

	def clear(self): 
		self._param_polygons_mask = None
		pass