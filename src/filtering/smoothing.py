# %load src/filtering/smoothing_0.py
#----------------------------------
# Exercise: Smoothing filter
#----------------------------------
# The original python file can be reloaded by typing %load src/filtering/smoothing_0.py in the first line of this cell.
# After successfully solving this exercise, type the following command in the first line of this cell:
# %%writefile src/filtering/smoothing.py
# This will save the result to a python file, which you will need for the next exercises.

class SmoothingFilter():

    #define box filter, also called mean filter
    def box_filter(self, img):              
        m = (1 / 9.0) * np.array([[1, 1, 1],
                                [1, 1, 1],
                                [1, 1, 1]])        
        mean = ndimage.convolve(img, m)
        return mean

    #define gaussian smoothing filter
    def gaussian_filter(self, img):        
        b = (1 / 16.0) * np.array([[1, 2, 1],
                                  [2, 4, 2],
                                  [1, 2, 1]])
        blurred = ndimage.convolve(img, b)
        return blurred
