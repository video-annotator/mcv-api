
class MCVBase(object):

	def __init__(self, **kwargs): super(MCVBase, self).__init__()

	def process(self, frame):
		#execute only the current filter
		return frame

	def processflow(self, frame):
		#execute the current the parent filters
		return frame

	def clear(self): pass

	@property
	def frame_index(self): return self._frame_index
	@frame_index.setter
	def frame_index(self, value): self._frame_index = value