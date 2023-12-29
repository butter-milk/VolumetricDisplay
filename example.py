from VolumetricDisplay import VolumetricDisplay
import numpy as np

#A simple example to see how it works
v = VolumetricDisplay(width=10,height=10)
image = np.zeros(shape=(10,10,10))
image[0,0,:]=3
image[:,0,0] = 1
image[0,:,0] = 2
images_to_display = v.display_static(image)
for m in images_to_display:
    print(m)