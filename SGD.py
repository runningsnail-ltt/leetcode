# -*- coding:utf-8 -*-
import os
import sys
from collections import Counter
import math
import numpy

class Solution(object):
    def SGD(self,data,epoch):
        """
        
        :param data: 
        :return: 
        """


        w = numpy.random.random()
        b = 0
        c = 0.001


        for i in range(epoch):
            ydata = [0, 0, 0, 0, 1, 1, 1]

            for x,y  in zip(data,ydata):
                z = -(w * x + b)
                h = 1 / (1 + math.exp(z))
                gd = (y - h) * x

            w = w - c * gd
            b = b - c * (y - h)
        return w,b

data = [1,2,1,1,1,3,2]
epoch = 1
print Solution().SGD(data,1)
