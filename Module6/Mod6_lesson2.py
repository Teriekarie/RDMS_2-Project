from statistics import quantiles
import numpy

# calculating the Quartile of random values
values = [12, 44, 60, 45, 20, 44, 34, 50, 45, 90]

# Defining the Quantile values
quantiles = [0,0.25,0.5,0.75,1]

x = numpy.quantile(values, [0,0.25,0.5,0.75,1])

print(x)


# Calculating percentiles
values = [10, 32, 64, 45, 24, 96, 60, 89]

x = numpy.percentile(values, 75)

print(x)

# calculating interquartile range

from scipy import stats
values = [10, 32, 64, 45, 24, 96, 60, 89]

x = stats.iqr(values)

print(x)
