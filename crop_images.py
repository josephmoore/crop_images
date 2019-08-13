#!/usr/bin/python3
import argparse
import os
from glob import glob
from PIL import Image
import concurrent.futures
import time

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--source', help='image or directory of images to be cropped', required=True) 
parser.add_argument('-t', '--ftype', help='image file type, e.g. jpg png, only required if dest=dir')
parser.add_argument('-c', '--coords', help='crop coords: left, top, right, bottom', nargs='+', type=int, required=True)
parser.add_argument('-d', '--dest', help='image or directory of images to save crop to', required=True)
args = parser.parse_args()

src = args.source
ftype = args.ftype
dst = args.dest
COORDS = tuple(args.coords)

#coords = (489,269,759,458)

def crop_image(src_img):
    im = Image.open(src_img)
    im_crop = im.crop(COORDS)
    im_crop.save(dst)

def crop_multi_image(src_img):
    image_name = os.path.basename(src_img)
    im = Image.open(src_img)
    im_crop = im.crop(COORDS)
    im_crop.save(dst + image_name)

def get_image_paths(src_dir, ftype):
    img_list = []
    for f in glob(src_dir + "*." + ftype):
        img_list.append(f)
    return img_list

def crop_all_images(img_list):
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(crop_multi_image, img_list)

def main():
    if os.path.isdir(src):
        img_list = get_image_paths(src, ftype)
        crop_all_images(img_list)
    elif os.path.isfile(src):
        crop_image(src)

if __name__ == "__main__":
    start_time= time.time()
    main()
    duration = time.time() - start_time
    print(f"finished in {duration} seconds.")
