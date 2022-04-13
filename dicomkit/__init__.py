import os
import png
import pydicom
import numpy as np
from .model import ScaleImage
from .contrast import contrast_auto

def mri_to_png(mri_file, png_file, do_contrast_auto=False):

    image_2d = extract_grayscale_image(mri_file)

    if do_contrast_auto:
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


def convert_file(mri_file_path, png_file_path, contrast_auto=False):
    if not os.path.exists(mri_file_path):
        raise Exception('Source file "%s" does not exists' % mri_file_path)

    if os.path.exists(png_file_path):
        print('Removing existing output file %s' % png_file_path)
        os.remove(png_file_path)

    mri_file = open(mri_file_path, 'rb')
    png_file = open(png_file_path, 'wb')

    mri_to_png(mri_file, png_file, contrast_auto)

    png_file.close()


def convert_folder(mri_folder, png_folder, contrast_auto=False):
    os.makedirs(png_folder)

    for mri_sub_folder, subdirs, files in os.walk(mri_folder):
        for mri_file in os.listdir(mri_sub_folder):
            mri_file_path = os.path.join(mri_sub_folder, mri_file)

            if os.path.isfile(mri_file_path):

                rel_path = os.path.relpath(mri_sub_folder, mri_folder)
                png_folder_path = os.path.join(png_folder, rel_path)
                if not os.path.exists(png_folder_path):
                    os.makedirs(png_folder_path)
                png_file_path = os.path.join(png_folder_path, '%s.png' % mri_file)

                try:
                    convert_file(mri_file_path, png_file_path, contrast_auto)
                    print('SUCCESS: %s --> %s' % (mri_file_path, png_file_path))
                except Exception as e:
                    print('FAIL: %s --> %s : %s' % (mri_file_path, png_file_path, e))
                    os.remove(png_file_path) if os.path.exists(png_file_path) else None