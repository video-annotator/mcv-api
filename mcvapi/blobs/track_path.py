from mcvapi.blobs.path import Path
from mcvapi.mcvbase import MCVBase

class TrackPath(MCVBase):

	def __init__(self, **kwargs):
		super(TrackPath, self).__init__(**kwargs)
		self._trackpath_paths = []
	

	def process(self, blobs):

		# First time
		if len(self._trackpath_paths)==0 or len(self._trackpath_paths)!=len(blobs): 
			self._trackpath_paths = [Path(b) for b in blobs]			
		else:
			for i, b in enumerate(blobs): self._trackpath_paths[i].append(b)

		return self._trackpath_paths

	def processflow(self, blobs):
		blobs = super(TrackPath, self).processflow(blobs)
		return self.process(blobs)
