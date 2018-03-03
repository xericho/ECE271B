import numpy as np
from PIL import Image

f = np.load('females.npy')

for i in range(3):
	print('Extracting image {}...'.format(i))
	im = Image.fromarray(f[i])
	im.save('./data/female{:06d}.jpg'.format(i))


