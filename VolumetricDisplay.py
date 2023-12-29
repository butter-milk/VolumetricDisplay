import numpy as np 

class VolumetricDisplay:
    width,height,center = 0,0,0
    rps: int #rotations per second
    display = None
    
    # in general, humans see between 30 to 60 fps, so we just are going to assume a nice 30. Might add a feature to edit this though
    # we assume that we rotate around the z axis, might make this adjustable as well, but for now we choose to work with it
    def __init__(self,width,height,center = 0, rps = 10) -> None:
        self.width = width
        self.height = height
        self.rps = rps
        self.center = center 
        self.display = np.zeros(shape=(height,width))
        pass

    def display_static(self, image):
        #image: 3d numpy array
        #returns a list of images through which the user can loop with even time intervals between them, deltaT = 1/rps
        left = -self.center
        right = self.width - self.center
        image_list = [None for _ in range(self.rps)]
        for i in range(self.rps):
            image_list[i] = np.column_stack([image[ round(t*np.cos(i/self.rps*2*np.pi)), round(t*np.sin(i/self.rps*2*np.pi)),:] for t in range(left, right)])
        return image_list
    
    def display_simulation(self, simulation):
        #simulation: list of (images,time): (3d numpy array, float)
        #return: [(image,no_rotations)]
        image_list = []
        for step in simulation:
            image, time = step
            no_rotations = time*self.rps
            image_list.append((self.display_static(image),no_rotations))
        return image_list
    
