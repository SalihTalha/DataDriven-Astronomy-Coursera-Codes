# Write your import_bss function here.
import numpy as np
def hms2dec(h,m,s):
  return 15*(h + m/60.0 + s/3600.0)

def dms2dec(d,m,s):
  if d < 0:
    return -1 * ( -d + m/60.0 + s/3600.0)
  return ( d + m/60.0 + s/3600.0 )

def import_bss():
  cat = np.loadtxt('bss.dat', usecols=range(1, 7)) 
  new = []
  for item, row in enumerate(cat,1):
    new.append((item, hms2dec(row[0], row[1], row[2]), dms2dec(row[3], row[4], row[5])))
  return (new)
  
  
def import_super():
  cat = np.loadtxt('super.csv', delimiter=',', skiprows=1, usecols=[0, 1])
  new = []
  for i, row in enumerate(cat, 1):
    new.append((i, row[0], row[1]))
  return new



# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Output of the import_bss and import_super functions
  bss_cat = import_bss()
  super_cat = import_super()
  print(bss_cat)
  print(super_cat)