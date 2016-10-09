import numpy as np
import operator
import re


def ext_filter(path, extension):
    """ return file-[] with extension, in sorted order"""
    from os import listdir
    from os.path import isfile, join
    filtered_files = [join(path, f) for f in listdir(path) if isfile(join(path, f))]
    return sorted(filtered_files)


def read_raw(filename, xsize=1024, ysize=1024):
    import struct
    with open(filename, 'rb') as f:
        img_data = [ struct.unpack('>f', f.read(4)) for i in range(xsize * ysize) ]
        img_data = np.array(img_data).reshape(xsize, ysize)
    return img_data


def coordinates(x, y):
    from itertools import product
    if type(x) is int:
        x = (0, x)
    if type(y) is int:
        y = (0, y)
    return list(product(xrange(*x), xrange(*y)))


def iterneighbours(x, y, r=1):
    for _x in range(x-r, x+r+1):
        for _y in range(y-r, y+r+1):
            yield _x,_y


def reverse_enum(L):
    for index in reversed(range(len(L))):
        yield index, L[index]

def crop_image(img, corner, xr=50, yr=50):
    x0, y0 = corner
    return np.array(img[y0:y0+yr, x0:x0+xr])


def smooth_array(lst):
    res = np.zeros_like(lst)
    for ii in range(1, len(lst)-1):
        aa,bb,cc = lst[ii-1:ii+2]
        res[ii] = 0.5*bb + 0.25*aa + 0.25*cc
    res[0] = 0.75*lst[0] + 0.25*lst[1]
    res[-1] = 0.75*lst[-1] + 0.25*lst[-2]
    return np.array(res)

def read_rings(ring_file, usecols=(0,1,2)):
    '''
    :param cols: tuple of columns to return
    :returns: list of ring coordinates for each frame
    '''

    data = []
    with open(ring_file) as f:
        for line in f:
            if line.startswith('#'):
                try:
                    data[-1] = np.array(data[-1])[:,usecols]
                except IndexError:
                    pass
                data.append([])
            else:
                d = map(float, line.split())
                if len(d)>0: data[-1].append(d)

    return [np.array(d) for d in data]


def loadtxt(objfile, usecols=None):
    numeric_const_pattern = r"""
        [-+]? # optional sign
        (?:
            (?: \d* \. \d+ ) # .1 .12 .123 etc 9.1 etc 98.1 etc
            |
            (?: \d+ \.? ) # 1. 12. 123. etc 1 12 123 etc
        )
        # followed by optional exponent part if desired
        (?: [Ee] [+-]? \d+ ) ?
    """
    rx = re.compile(numeric_const_pattern, re.VERBOSE)
    data = []

    def _load(fp, usecols):
        for line in fp.readlines():
            if line.startswith('#'):
                continue

            scan = rx.findall(line)
            scan = np.array(map(float, scan))

            if len(scan) == 0:
                continue

            if usecols:
                usecols = list(usecols)
                try:
                    data.append(scan[usecols])
                except IndexError as e:
                    print 'Warning: ', e.message
                    print '         ', scan
            else:
                data.append(scan)

    try:
        _load(objfile, usecols)
    except AttributeError:
        with open(objfile, 'r') as fp:
            _load(fp, usecols)

    return np.array(data)


def stats(arr):
    return arr.size, arr.mean(), arr.std(), arr.sum(), arr.min(), arr.max()

def print_stats(arr):
    print 'size: {}, mean: {:.4f}, std: {:.4f}, sum: {:.4f}, min: {:.4f}, max: {:.4f}'.format(*stats(arr))
