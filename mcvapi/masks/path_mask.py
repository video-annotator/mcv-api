from mcvapi.mcvbase import MCVBase
import numpy as np, cv2


class PathMask(MCVBase):
	
	def __init__(self, **kwargs):
		self._param_pathmask_paths  = kwargs.get('mask_paths', [])
		self._param_pathmask_radius = kwargs.get('mask_radius', 30)
		
	def process(self, frame):
		paths = self.mask_paths
		mask  = np.zeros_like(frame)			
		for path in paths:
			position = path[self.frame_index] if isinstance(path, list) else path.get_position(self.frame_index) 
			if position is not None: cv2.circle(mask, position, self.mask_radius, (255,255,255), -1)			
		return cv2.bitwise_and(frame, mask)

	def processflow(self, frame):
		frame = super(PathMask, self).processflow(frame)
		return PathMask.process(self, frame)

	@property
	def mask_radius(self): return self._param_pathmask_radius

	@property
	def mask_paths(self):  return self._param_pathmask_paths
	@mask_paths.setter
	def mask_paths(self, value):  self._param_pathmask_paths = value
	