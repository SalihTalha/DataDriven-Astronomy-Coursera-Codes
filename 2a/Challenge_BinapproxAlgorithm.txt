# Write your median_bins and median_approx functions here.
import numpy as np

def median_bins(values, B):
  arr = np.array(values)
  mean = np.mean(arr)
  sd = np.std(arr)
  left_bin = 0
  bins = np.zeros(B)
  stepVal = (2*sd) / B
  
  for i in arr:
    if i < mean - sd:
      left_bin += 1
    elif i < mean+sd:
      bin = int((i - (mean-sd) ) / stepVal)
      bins[bin] += 1
  
  
  return mean, sd, left_bin, bins
    
def median_approx(listItems, B):
  mean, sd, left_bin, bins = median_bins(listItems, B)
  N = len(listItems)
  mid = (N + 1 ) / 2
  
  count = left_bin
  
  for b, bincount in enumerate(bins):
    count += bincount
    if count >= mid:
      break
    
  width = 2*sd / B
  median = mean - sd + width * (b + 0.5)
    
  return median
  
# You can use this to test your functions.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your functions with the first example in the question.
  print(median_bins([1, 1, 3, 2, 2, 6], 3))
  print(median_approx([1, 1, 3, 2, 2, 6], 3))

  # Run your functions with the second example in the question.
  print(median_bins([1, 5, 7, 7, 3, 6, 1, 1], 4))
  print(median_approx([1, 5, 7, 7, 3, 6, 1, 1], 4))
