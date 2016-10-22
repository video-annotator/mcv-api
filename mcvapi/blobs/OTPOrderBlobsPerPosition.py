import numpy as np
from tools import *
from OTPBase import OTPBase



class OTPOrderBlobsPerPosition(OTPBase):
    """
    Order the blobs by position
    Return: Ordered blobs
    """


    def __init__(self, **kwargs):
        super(OTPOrderBlobsPerPosition, self).__init__(**kwargs)
        self._orderblobs_last_blobs = []
    

    def compute(self, blobs):
        if len( blobs )<self._param_n_blobs:
            self._ordering_result = 0 #not enought blobs to order
        elif len(self._orderblobs_last_blobs)==self._param_n_blobs:
            #################### SELECT BLOBS BY POSITION ########################
            #### Blobs are identified by their distance to the previous position
            combs = combinations( blobs, self._orderblobs_last_blobs )
            
            classifications = []
            for comb in combs:
                classification = sum([lin_dist(b1._centroid, b2._centroid) for b1,b2 in comb])
                classifications.append([classification, [b1 for b1,b2 in comb]])

            classifications = sorted(classifications, key=lambda x: x[0], reverse=False)
            r = classifications[0]
            self._orderblobs_last_blobs = r[1]
            self._ordering_result = 1
            return r[1]
        else:
            self._orderblobs_last_blobs = blobs

        return blobs

    def process(self, blobs):
        blobs = super(OTPOrderBlobsPerPosition, self).process(blobs)
        return OTPOrderBlobsPerPosition.compute(self, blobs)
