"""27. WAP to find mean, median, mode, standard
deviation, variance of the elements of a list using
statistics module."""

import statistics
list3=[8,7,4,1]
print(list3)
print('Mean :',statistics.mean(list3))
print('Median :';,statistics.median(list3))
try:
    print('Mode :', statistics.mode(list3))
except statistics.StatisticsError:
    print('Your have no repeating ')
print('Standard deviation :', statistics.pstdev(list3))
print('Variance :', statistics.variance(list3))
