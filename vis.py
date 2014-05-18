import results
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import sys

parameters = ['overhead_ratio', 'started', 'response_prob', 'dropped', 'rtt_med', 'delivery_prob', 'removed', 'rtt_avg', 'latency_avg', 'delivered', 'hopcount_avg', 'relayed', 'buffertime_avg', 'created', 'aborted', 'buffertime_med', 'hopcount_med', 'latency_med']

mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')
x, y, z = results.get(
  x_kwd="bufferSize",
  y_kwd="TTL",
  z_kwd="delivery_prob"
)
ax.plot(x, y, z, label='Epidemic routing on SIGCOMM09')
ax.legend()
ax.set_xlabel('Buffer Size (bytes)')
ax.set_ylabel('TTL (minutes)')
ax.set_zlabel('Delivery probability')

plt.show()
