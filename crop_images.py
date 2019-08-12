#!/usr/bin/python3
import argparse
import os
from glob import glob
from PIL import Image

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--source', help='image or directory of images to be cropped', required=True) 
parser.add_argument('-t', '--ftype', help='image file type, e.g. jpg png')
parser.add_argument('-c', '--coords', help='crop coords: left, top, right, bottom', nargs='+', type=int, required=True)
parser.add_argument('-d', '--dest', help='image or directory of images to save crop to', required=True)
args = parser.parse_args()

src = args.source
ftype = args.ftype
dst = args.dest
coords = tuple(args.coords)

#coords = (489,269,759,458)

def crop_image(src_img, coords):
    image_name = os.path.basename(src_img)
    im = Image.open(src_img)
    im_crop = im.crop(coords)
    return im_crop

def get_image_paths(src_dir, ftype):
    img_list = []
    for f in glob(src_dir + "*." + ftype):
        img_list.append(f)
    return img_list

def main():
    if os.path.isdir(src):
        img_list = get_image_paths(src, ftype)
        for img_path in img_list:
            img = crop_image(img_path, coords)
            img.save(dst + os.path.basename(img_path))

    elif os.path.isfile(src):
        img = crop_image(src, coords)
        img.save(dst)

if __name__ == "__main__":
    main()
