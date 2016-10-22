
class MCVBase(object):

	def __init__(self, **kwargs): super(MCVBase, self).__init__()

	def process(self, frame):
		#execute only the current filter
		return frame

	def processflow(self, frame):
		#execute the current the parent filters
		return frame