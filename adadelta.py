#!/usr/bin/env python

import sys
import numpy

from matplotlib import pyplot

n_steps = 100000
gradient = float(sys.argv[1])
decay_rate = float(sys.argv[2])
epsilon = float(sys.argv[3])

mean_gradient2 = 0
mean_step2 = 0

steps = numpy.zeros(n_steps)
for i in range(n_steps):
    mean_gradient2 = decay_rate * mean_gradient2 + (1 - decay_rate) * gradient ** 2
    steps[i] = ((mean_step2 + epsilon) / (mean_gradient2 + epsilon)) ** 0.5 * gradient
    mean_step2 = decay_rate * mean_step2 + (1 - decay_rate) * steps[i] ** 2

#pyplot.plot(numpy.log10(range(1, n_steps + 1)), steps)
pyplot.plot(steps)
pyplot.show()
import IPython; IPython.embed()
