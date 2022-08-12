from statistics import quantiles
import numpy

# calculating the Quartile of random values
values = [12, 44, 60, 45, 20, 44, 34, 50, 45, 90]

# Defining the Quantile values
quantiles = [0,0.25,0.5,0.75,1]

x = numpy.quantile(values, [0,0.25,0.5,0.75,1])

print(x)

