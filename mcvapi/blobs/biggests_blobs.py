from mcvapi.mcvbase import MCVBase

class BiggestsBlobs(MCVBase):

	
	def __init__(self, **kwargs):
		super(BiggestsBlobs, self).__init__(**kwargs)
		self._param_biggests_blobs_n = 1

	def process(self, blobs):
		blobs = sorted(blobs,key=lambda a:a._area,reverse=True)
		if len(blobs)>self.biggests_blobs_n: return blobs[:self.biggests_blobs_n]
		else: return blobs

	def processflow(self, blobs):
		blobs = super(BiggestsBlobs, self).processflow(blobs)
		return self.process(blobs)

	#####################################################################
	### PROPERTIES ######################################################
	#####################################################################

	@property
	def biggests_blobs_n(self): return self._param_biggests_blobs_n
	