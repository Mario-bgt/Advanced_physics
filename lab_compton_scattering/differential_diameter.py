from functions import *
import os

angles = np.linspace(20, 150, 10)
angles = np.round(angles, 0)
print(angles)

# calculate the difference between 180 and the angles
diff = ((180 - angles) / 2) + angles
print(diff)

# get the file names that start with dw from the data folder
files = os.listdir('data')
files = [file for file in files if file.startswith('dw')]




