# !/usr/bin/python3
# -*- coding: utf-8 -*-

class MCVBase(object):
	"""
	Abstract class of a filter.  
	The filters classes should reemplement the methods
	present on this class.
	"""


	def __init__(self, **kwargs): 
		super(MCVBase, self).__init__()

	def process(self, input_data):
		"""Filter implmentation."""
		return input_data

	def processflow(self, input_data):
		"""Process all the filters from the hierarchy."""
		result = super(MCVBase).processflow(input_data)
		return result

	def clear(self): 
		"""
		Method used to reset current filter data.
		Used to re-start an analysis from scratch.
		"""
		pass

	@property
	def frame_index(self): 
		"""
		Some filters require to know which frame it being analysed.
		This property allows you to get and set the index of the video current frame.
		"""
		return self._frame_index
	@frame_index.setter
	def frame_index(self, value): self._frame_index = value