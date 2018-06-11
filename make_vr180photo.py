# -*- coding: utf-8 -*-
import sys
import os
import shutil
import base64
from libxmp import XMPFiles, XMPMeta

# Usage
if len(sys.argv) < 5:
    print('[Usage]')
    print('  $ python {0} [Left image path] [Right image path] [Image width] [Image height]'.format(sys.argv[0]))
    print('  * The image type must be jpeg.')
    print('  * These images must be same width and height.')
    print('  * Output merged vr image file named {Left image file}.vr.jpg.')
    exit()

# Arguments
limage_path = sys.argv[1]
rimage_path = sys.argv[2]
image_width = int(sys.argv[3])
image_height = int(sys.argv[4])
if not os.path.isfile(limage_path):
    print('Left image path ({0}) is not exists.'.format(limage_path))
    exit()
if not os.path.isfile(rimage_path):
    print('Right image path ({0}) is not exists.'.format(rimage_path))
    exit()

# Copy left image file
limage_dir = os.path.split(limage_path)[0]
limage_fname = os.path.splitext(os.path.split(limage_path)[1])[0]
vrimage_path = os.path.join(limage_dir, limage_fname + '.vr.jpg')
shutil.copyfile(limage_path, vrimage_path)

# Load image's xmp
vrimage_file = XMPFiles(file_path=vrimage_path, open_forupdate=True)
lxmp = vrimage_file.get_xmp()
#print(lxmp)

# Google's namespace
XMP_GIMAGE = 'http://ns.google.com/photos/1.0/image/'
XMP_GPANO = 'http://ns.google.com/photos/1.0/panorama/'
XMPMeta.register_namespace(XMP_GIMAGE, 'GImage')
XMPMeta.register_namespace(XMP_GPANO, 'GPano')

# Set GPano properties
lxmp.set_property(XMP_GPANO, 'ProjectionType', 'equirectangular')
lxmp.set_property_int(XMP_GPANO, 'CroppedAreaLeftPixels', image_width/2)
lxmp.set_property_int(XMP_GPANO, 'CroppedAreaTopPixels', 0)
lxmp.set_property_int(XMP_GPANO, 'CroppedAreaImageWidthPixels', image_width)
lxmp.set_property_int(XMP_GPANO, 'CroppedAreaImageHeightPixels', image_height)
lxmp.set_property_int(XMP_GPANO, 'FullPanoWidthPixels', image_width*2)
lxmp.set_property_int(XMP_GPANO, 'FullPanoHeightPixels', image_height)
lxmp.set_property_int(XMP_GPANO, 'InitialViewHeadingDegrees', 180)

# Encode right image to BASE64
rimage_data = open(rimage_path, 'rt').read()
rimage_base64 = base64.b64encode(rimage_data)

# Set GImage properties
lxmp.set_property(XMP_GIMAGE, 'Mime', 'image/jpeg')
lxmp.set_property(XMP_GIMAGE, 'Data', rimage_base64)

# Put XMP.
if vrimage_file.can_put_xmp(lxmp):
    vrimage_file.put_xmp(lxmp)
    print(vrimage_file.get_xmp())
    print("Done!")

vrimage_file.close_file()
