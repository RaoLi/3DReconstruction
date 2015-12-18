import numpy as np
import cv2

#local modules
from common import splitfn

#built-in modules
import os 

USAGE = '''
USAGE: calib.py [--save <filename>] [--debug <output path> [--square_size] [<image mask>]]
'''

if __name__ == '__main__':
    import sys
    import getopt
    from glob import glob
    
    args, img_mask = getopt.getopt(sys.argv[1:], '', ['save=', 'debug=', 'squre_size='])
    args = dict(args)
    try:
        img_mask = img_mask[0]
    except:
        img_mask = '../data/left*.jpg'
        
    img_names = glob(img_mask)
    debug_dir = args.get('--debug')
    square_size = float(args.get('--square_size', 1.0))
    
    pattern_size = (9,6)
    pattern_points = np.zeros((no.prod(pattern_size),3), np.float32)
    pattern_points[:,:2] = np.indices(pattern_size).T.reshape(-1, 2)
    pattern_points *=square_size