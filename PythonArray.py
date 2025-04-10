#CS162 Arrays in Python
import numpy as np
#Creaing 5x5 array
array = np.random.randint(0,50,size=(5,5), dtype=int)
#Printing entire array
print(array)
#Printing number from 2nd row 3rd column
print(array[1, 2])
#Print the sum of all elements in array
print(np.sum(array))
#Print the mean of each row in the array
#axis=1 -> go across each row
print(np.mean(array,axis=1))
#Print maximum value in each column
#axis=0 -> go down each column
print(np.max(array,axis=0))