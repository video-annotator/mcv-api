import cv2
import numpy as np
from mcvapi.mcvbase import MCVBase

class MorphologyExClose(MCVBase):
	
	def __init__(self, **kwargs):
		super(MorphologyExClose, self).__init__(**kwargs)
		self._param_morphologyexclose_kernel_size = 3

		self._param_morphologyexclose_kernel = np.ones(
			(self._param_morphologyexclose_kernel_size,self._param_morphologyexclose_kernel_size)
		,np.uint8)

	#####################################################################
	### PROPERTIES ######################################################
	#####################################################################

	@property
	def morphologyexclose_kernel_size(self):  return self._param_morphologyexclose_kernel_size


	#####################################################################
	### FUNCTIONS #######################################################
	#####################################################################


	def process(self, frame):
		return cv2.morphologyEx(frame, cv2.MORPH_CLOSE, self._param_morphologyexclose_kernel)

	def processflow(self, image):
		res = super(MorphologyExClose, self).processflow(image)
		return self.process(res)