import scipy 
from scipy.fftpack import dct 
from scipy.stats import kurtosis
import cv2
import numpy
from matplotlib import pyplot as plt 
import numpy as np
import tensorflow as tf
import ast 
lst_fr = []

lst_freq = []
lst_kurt = []
path = ' '

windowsize_r = 8
windowsize_c = 8

img = cv2.imread(path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cost1 = []

for r in range(0,gray.shape[0] - windowsize_r, windowsize_r):
	for c in range(0,gray.shape[0] - windowsize_c, windowsize_c):
		window = gray[r:r+windowsize_r,c:c+windowsize_c]
		hist = numpy.histogram(window,bins=256)
		cosine_trans =  dct(window)
		cost = cosine_trans.tolist()
		sort = np.sort(cost)
		print(sort.shape)

		kurt = kurtosis(window)
		#print(kurt)
		kurt = np.expand_dims(kurt,axis = 1)
		mean = np.mean(kurt)
		diff1 = mean - kurt

		print(diff1)
		sum = np.sum(diff1)
		print(sum)
		

		#kurt = np.squeeze(kurt, axis = 2)
		print(kurt.shape)
		for j in sort:
			print(j)
		plt.ylabel("kurtosis")
		plt.xlabel("frequency")
		plt.title("Frequency vs Kurtosis")
		plt.scatter(j,kurt)
		plt.draw()
		plt.show()
		
	