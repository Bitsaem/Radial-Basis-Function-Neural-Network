#!/usr/bin/python
# -*- coding: utf-8 -*-
# Andrew D Yates

import pylab

t = pylab.arange(0.0, 2.0, 0.01)
s = pylab.sin(2*pylab.pi*t)
pylab.plot(t, s, linewidth=1.0)

pylab.xlabel('time (s)')
pylab.ylabel('voltage (mV)')
pylab.title('About as simple as it gets, folks')
pylab.grid(True)
pylab.savefig("test.png")
pylab.show()
