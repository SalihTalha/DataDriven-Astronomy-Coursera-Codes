# Write your mean_datasets function here
import numpy as np
import csv
def mean_datasets(strings):
  dataSets = []
  for file in strings:
    data = np.loadtxt(file, delimiter=',')
    dataSets.append(data)
  arr = np.array(dataSets)
  arr = np.sum(arr, axis = 0)
  arr = arr / (len(strings))
  arr = np.round(arr, 1)
  return arr
    

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with the first example from the question:
  print(mean_datasets(['data1.csv', 'data2.csv', 'data3.csv']))

  # Run your function with the second example from the question:
  print(mean_datasets(['data4.csv', 'data5.csv', 'data6.csv']))
