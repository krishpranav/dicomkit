#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from model import ScaleImage

def shade_at_precentile(hist, precentile):
    n = np.sum(hist)
    cumulative_sum = np.cumsum(hist)
    
    return np.argmax(cumulative_sum/n >= precentile)

def contrast_auto(image):
    ''' auto contrast functionality '''
    hist, _ = np.histogram(image.image.ravel(), bins=np.arange(0, 256))
    p_low = shade_at_precentile(hist, .01)
    p_high = shade_at_precentile(hist, .99)
    a = 255.0/(p_high - p_low)
    b = -1.0 * a * p_low

    result = (image.image.astype(float) * a) + b
    result = result.clip(0, 255.0)
    
    return ScaleImage(np.uint8(result), image.width, image.height)