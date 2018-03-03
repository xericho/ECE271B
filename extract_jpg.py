import numpy as np
from PIL import Image

data=np.load('face_dataset20k_part0.npy')
labels=np.load('all_labels.npy')
f = data[labels==-1]

for i in range(f.shape[0]):
	print('Extracting image {}...'.format(i))
	im = Image.fromarray(f[i])
	### CHANGE PATH
	im.save('./data/female{:06d}.jpg'.format(i))


