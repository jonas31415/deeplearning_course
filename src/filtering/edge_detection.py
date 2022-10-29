# %load src/filtering/edge_detection_0.py
#----------------------------------
# Exercise: Edge Detection
#----------------------------------
# The original python file can be reloaded by typing %load src/filtering/edge_detection_0.py in the first line of this cell.
# After successfully solving this exercise, type the following command in the first line of this cell:
# %%writefile src/filtering/edge_detection.py
# This will save the result to a python file, which you will need for the next exercises.

class EdgeDetection():
    
    #compute gradient in x and y direction
    def gradient_filter(self,img):
        k_x = np.array([-1, 0, 1])
        k_y = np.array([-1], [0], [1])
        gradient_x = ndimage.convolve(img, k_x)
        gradient_y = ndimage.convolve(img, k_y)
        return gradient_x, gradient_y
    
    #define sobel filter in x and y direction
    def sobel_filter(self,img):
        sx = np.array([-1, 0, 1], [-2, 0, 2], [-1, 0, 1])
        sy = np.array([-1, -2, -1], [0, 0, 0], [1, 2, 1]) 
        sobel_x = ndimage.convolve(img, sx)
        sobel_y = ndimage.convolve(img, sy)
        return sobel_x, sobel_y
    
    #compute magnitude of filtered image of both directions
    def compute_magnitude(self,x,y):
        magnitude = np.hypot(sx,sy)
        return magnitude
