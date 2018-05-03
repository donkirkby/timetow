import math
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt

DICE = '⚀⚁⚂⚃⚄⚅'


def label_meridian(longitude):
    index = int(((longitude + 179.5) % 360) // 60)
    return DICE[index]


def label_parallel(latitude):
    index = int(((-latitude + 89.5) % 180) // 30) + 1
    return DICE[index]


f, axes_list = plt.subplots(2)
f.set_size_inches(17, 11)
f.set_dpi(50)
map_ax, time_ax = axes_list
# lon_0 is central longitude of projection.
# resolution = 'c' means use crude resolution coastlines.
# eck4 works well, but no repeated Pacific
m = Basemap(projection='eck4', lon_0=0, resolution='c', ax=map_ax)
m.drawcoastlines()
m.fillcontinents(color='lightgrey')
# draw parallels and meridians.
text_size = 'xx-large'
m.drawparallels(np.arange(-90., 120., 30.),
                labels=[1, 1, 0, 0],
                linewidth=3,
                dashes=[3, 1],
                size=text_size,
                fmt=label_parallel)
m.drawparallels(np.array([float(i)
                          for i in range(-90, 120, 5)
                          if i % 30]),
                size=text_size)
m.drawmeridians(np.arange(180.5, 540., 60.),
                labels=[0, 0, 1, 1],
                linewidth=3,
                dashes=[3, 1],
                size=text_size,
                fmt=label_meridian)
m.drawmeridians(np.array([float(i)
                          for i in range(180, 540, 10)
                          if i % 60]),
                size=text_size)
# m.drawrivers()
m.drawmapboundary()
map_left = 0.05
map_width = 0.91
map_ax.set_position((map_left, 0.12, map_width, 0.909))

calendar_width = 0.6
calendar_left = map_left + map_width/2 - calendar_width/2
time_ax.set_position((calendar_left, 0.05, calendar_width, 0.07))
time_ax.set_axis_off()
rolls = [(d1, d2) for d1 in DICE for d2 in DICE]
for i, (die1, die2) in enumerate(rolls):
    x = i / len(rolls)
    year = 2001 - i - int(math.exp(i/4.2242))
    label = f'{die1}{die2}{year}'
    time_ax.text(x, 0.95, label, rotation=-90, size=text_size)
plt.show()
