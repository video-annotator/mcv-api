import cv2
from mcvapi.mcvbase import MCVBase

# for compatibility between opencv 2 and 3
try:
    # OpenCV 2
    CV_ADAPTIVE_THRESH_MEAN_C = cv2.cv.CV_ADAPTIVE_THRESH_MEAN_C
    THRESH_BINARY             = cv2.cv.CV_THRESH_BINARY
except:
    # OpenCV 3
    CV_ADAPTIVE_THRESH_MEAN_C = cv2.ADAPTIVE_THRESH_MEAN_C
    THRESH_BINARY             = cv2.THRESH_BINARY


class AdaptativeThreshold(MCVBase):
    
    def __init__(self, **kwargs):
        super(AdaptativeThreshold, self).__init__(**kwargs)
        self._param_adaptive_threshold_method       = CV_ADAPTIVE_THRESH_MEAN_C
        self._param_adaptive_threshold_type         = THRESH_BINARY
        self._param_adaptive_threshold_block_size   = 3
        self._param_adaptive_threshold_c            = 255

    #####################################################################
    ### PROPERTIES ######################################################
    #####################################################################

    @property
    def adaptive_threshold_method(self):        return self._param_adaptive_threshold_method
    
    @property
    def adaptive_threshold_type(self):          return self._param_adaptive_threshold_type

    @property
    def adaptive_threshold_block_size(self):    
        if (self._param_adaptive_threshold_block_size % 2)==0: 
            self._param_adaptive_threshold_block_size += 1
        return self._param_adaptive_threshold_block_size

    @property
    def adaptive_threshold_block_c(self):       return self._param_adaptive_threshold_c
    
    #####################################################################
    ### FUNCTIONS #######################################################
    #####################################################################


    def process(self, frame):
        thresh = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY) if len(frame.shape)>2 else frame
        return cv2.adaptiveThreshold(
            thresh, 255,
            self.adaptive_threshold_method,
            self.adaptive_threshold_type,
            self.adaptive_threshold_block_size,
            self.adaptive_threshold_block_c
        )

    def processflow(self, image):
        res = super(AdaptativeThreshold, self).processflow(image)
        return self.process(res)