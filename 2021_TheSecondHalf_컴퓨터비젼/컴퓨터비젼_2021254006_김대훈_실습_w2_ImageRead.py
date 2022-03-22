import argparse
import cv2

parser = argparse.ArgumentParser()
parser.add_argument('--path', default='C:\Lena.png',help='Image path')
params = parser.parse_args()

img = cv2.imread(params.path)

#assert img is not None

print('read {}'.format(params.path))
print('shape:',img.shape)
print('dtype:',img.dtype)

img = cv2.imread(params.path, cv2.IMREAD_GRAYSCALE)
#assert img is not None
print('read {} as grayscale'.format(params.path))
print('shape:',img.shape)
print('dtype:',img.dtype)