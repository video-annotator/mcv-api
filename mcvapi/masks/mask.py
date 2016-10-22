from mcvapi.mcvbase import MCVBase
import numpy as np, cv2


class Mask(MCVBase):
	
	def __init__(self):
		self._param_mask_img = None

	@property
	def mask_maskimg(self): return self._param_mask_img


	def process(self, frame):
		if self.mask_maskimg is not None:
			if len(frame.shape)==2:
				return cv2.bitwise_and(frame, self.mask_maskimg)
			else:
				a,b,c = cv2.split(frame)
				a = cv2.bitwise_and(a, self.mask_maskimg)
				b = cv2.bitwise_and(b, self.mask_maskimg)
				c = cv2.bitwise_and(c, self.mask_maskimg)
				return cv2.merge( (a,b,c) )
		else:
			return frame

	def processflow(self, frame):
		frame = super(Mask, self).processflowself(frame)
		return Mask.process(self, frame)	