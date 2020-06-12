# Write your calc_stats function here.
import numpy as np

def calc_stats(string):
  data = np.loadtxt(string, delimiter=',')
  data = data.flatten()
  length = data.size
  mean = sum(data) / length
  ind = length / 2
  data = np.sort(data)
  median = data[int(ind)]
  if length % 2 == 0:
    median = ( data[int(length / 2)] + data[int(length / 2 - 1)] ) / 2
  return np.round(mean,1), np.round(median,1)


# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your `calc_stats` function with examples:
  mean = calc_stats('data.csv')
  print(mean)