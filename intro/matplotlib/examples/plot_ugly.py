import numpy as np
import matplotlib
matplotlib.use('Agg')
import pylab as pl

matplotlib.rc('grid', color='black', linestyle='-', linewidth=1)

fig = pl.figure(figsize=(5,4),dpi=72)
axes = fig.add_axes([0.01, 0.01, .98, 0.98], axisbg='.75')
X = np.linspace(0, 2, 40, endpoint=True)
Y = np.sin(2 * np.pi * X)
pl.plot(X, Y, lw=.05, c='b', antialiased=False)

pl.xticks(())
pl.yticks(np.arange(-1., 1., 0.2))
pl.grid()
ax = pl.gca()

pl.show()
