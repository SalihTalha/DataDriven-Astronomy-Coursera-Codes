# Write your crossmatch function here.
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

def angular_dist(r1,d1,r2,d2):
  r1 = np.radians(r1)
  d1 = np.radians(d1)
  r2 = np.radians(r2)
  d2 = np.radians(d2)
  a = np.sin(np.abs(d1-d2)/2)**2
  b = np.cos(d1)*np.cos(d2)*np.sin(np.abs(r1-r2)/2)**2 # be careful about d's changed with r's in this equation 
  d = 2 * np.arcsin(np.sqrt(a+b))
  return np.degrees(d)

def find_closest(cat, r, d):
  closest = 0
  closestDistance = 360
  for i, r1, d1 in cat:
    ang = angular_dist(r1, d1, r, d)
    if ang < closestDistance:
      closestDistance = ang
      closest = i
  return closest, closestDistance


def crossmatch(bss, sup, max_dist):
  matches = []
  nmatches = []
  for idb, r, d in bss:
    cl = find_closest(sup, r, d)
    if cl[1] < max_dist:
      matches.append((idb, cl[0], cl[1]))
    else:
      nmatches.append(idb)
      
  return matches, nmatches


# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  bss_cat = import_bss()
  super_cat = import_super()

  # First example in the question
  max_dist = 40/3600
  matches, no_matches = crossmatch(bss_cat, super_cat, max_dist)
  print(matches[:3])
  print(no_matches[:3])
  print(len(no_matches))

  # Second example in the question
  max_dist = 5/3600
  matches, no_matches = crossmatch(bss_cat, super_cat, max_dist)
  print(matches[:3])
  print(no_matches[:3])
  print(len(no_matches))
