from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np

def load_fits(filename):
  hdulist = fits.open(filename)
  data = np.array(hdulist[0].data)
  return int(data.argmax() / data.shape[0]), data.argmax() % data.shape[0]



if __name__ == '__main__':
  # Run your `load_fits` function with examples:
  bright = load_fits('image1.fits')
  print(bright)

  # You can also confirm your result visually:
  

  hdulist = fits.open('image1.fits')
  data = hdulist[0].data

  # Plot the 2D image data
  plt.imshow(data.T, cmap=plt.cm.viridis)
  plt.colorbar()
  plt.show()
