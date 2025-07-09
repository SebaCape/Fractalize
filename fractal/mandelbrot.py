import numpy as np
from numba import jit

@jit(nopython=True)
def compute_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter):
    image = np.zeros((height, width), dtype=np.int32)
    
    for x in range(width):
        for y in range(height):
            zx = 0.0
            zy = 0.0
            cx = xmin + x * (xmax - xmin) / width
            cy = ymin + y * (ymax - ymin) / height
            iteration = 0
            while zx*zx + zy*zy <= 4.0 and iteration < max_iter:
                xtemp = zx*zx - zy*zy + cx
                zy = 2.0*zx*zy + cy
                zx = xtemp
                iteration += 1
            image[y, x] = iteration
            
    return image
