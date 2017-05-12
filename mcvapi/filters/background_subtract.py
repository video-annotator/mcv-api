import cv2
import numpy as np
from mcvapi.mcvbase import MCVBase

class BackgroundSubtract(MCVBase):
	
	def __init__(self, **kwargs):
		super(BackgroundSubtract, self).__init__(**kwargs)
		self._param_background_subtract_image 	    = None
		self._param_background_subtract_threshold   = None
		

	#####################################################################
	### PROPERTIES ######################################################
	#####################################################################

	@property
	def background_subtract_image(self):        return self._param_background_subtract_image
	@background_subtract_image.setter
	def background_subtract_image(self, value): self._param_background_subtract_image = value
	
	@property
	def background_subtract_threshold(self):    return self._param_background_subtract_threshold


	#####################################################################
	### FUNCTIONS #######################################################
	#####################################################################


	def process(self, frame):
		if len(frame.shape)>2: frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		background = self.background_subtract_image

		if background is not None and len(background.shape)>2:
			background = cv2.cvtColor(background, cv2.COLOR_BGR2GRAY)
		
		if background is not None and len(background)>1:
			diff 		= cv2.absdiff(frame , background)
			ret , res 	= cv2.threshold(diff, self.background_subtract_threshold , 255, cv2.THRESH_BINARY )
			return res
		else:
			return np.zeros_like(frame)

	def processflow(self, image):
		res = super(BackgroundSubtract, self).processflow(image)
		return self.process(res)