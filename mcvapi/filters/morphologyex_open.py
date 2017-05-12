import cv2
import numpy as np
from mcvapi.mcvbase import MCVBase

class MorphologyExOpen(MCVBase):
	
	def __init__(self, **kwargs):
		super(MorphologyExOpen, self).__init__(**kwargs)
		self._param_morphologyexopen_kernel_size = 3

		self._param_morphologyexopen_kernel = np.ones(
			(self._param_morphologyexopen_kernel_size,self._param_morphologyexopen_kernel_size)
		,np.uint8)

	#####################################################################
	### PROPERTIES ######################################################
	#####################################################################

	@property
	def morphologyexopen_kernel_size(self):  return self._param_morphologyexopen_kernel_size


	#####################################################################
	### FUNCTIONS #######################################################
	#####################################################################


	def process(self, frame):
		return cv2.morphologyEx(frame, cv2.MORPH_OPEN, self._param_morphologyexopen_kernel)

	def processflow(self, image):
		res = super(MorphologyExOpen, self).processflow(image)
		return self.process(res)