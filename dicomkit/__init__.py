#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os 
import png
import numpy as np
import pydicom
from .model import ScaleImage
from .contrast import contrast_auto

def mri_to_png(mri_file, png_file, do_auto_contrast=False):
    image_2d = extract_grayscale_image(mri_file)

    if do_auto_contrast:
        image_2d = contrast_auto(image_2d)
    
    w = png.Writer(image_2d.width, image_2d.height, greyscale=True)
    w.write(png_file, image_2d.image)

def extract_grayscale_image(mri_file):
    plan = pydicom.read_file(mri_file)
    shape = plan.pixel_array.shape

    image_2d = plan.pixel_array.astype(float)

    image_2d_scaled = (np.maximum(image_2d,0) / image_2d.max()) * 255.0
    
    image_2d_scaled = np.uint8(image_2d_scaled)

    return ScaleImage(image_2d_scaled, shape[1], shape[0])