import kNN
import matplotlib
import matplotlib.pyplot as plt
from numpy import *

kNN.handwritingClassTest()

#datingDataMat, datingLabels = kNN.file2matrix('datingTestSet2.txt')
#normMat,ranges,minVals = kNN.autoNorm(datingDataMat)
#print normMat
#print minVals
"""
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(datingDataMat[:,1], datingDataMat[:, 2], 15.0 * array(datingLabels), 15.0 * array(datingLabels) )
ax.axis([-2,25,-0.2,2.0])
plt.xlabel('Percentage of Time Spent Playing Video Games')
plt.ylabel('Liters of Ice Cream Consumed Per Week')
plt.show()
"""