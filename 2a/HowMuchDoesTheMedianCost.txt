# Write your function median_FITS here:
import numpy as np
import time
from astropy.io import fits

def median_fits(strings):
  start = time.time()
  arr = []
  for file in strings:
    hdulist = fits.open(file)
    arr.append(hdulist[0].data)
    hdulist.close()
  
  stack = np.dstack(arr)
  median = np.median(stack, axis = 2)
  memory = stack.nbytes
  memory = memory / 1024
  
  stop = time.time() - start
  return median, stop, memory
  
    
# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with first example in the question.
  result = median_fits(['image0.fits', 'image1.fits'])
  print(result[0][100, 100], result[1], result[2])
  
  # Run your function with second example in the question.
  result = median_fits(['image{}.fits'.format(str(i)) for i in range(11)])
  print(result[0][100, 100], result[1], result[2])