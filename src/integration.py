#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 8:47:36 2016

@author: steiner

Solução numérica da equação de van de Pol


"""
import scipy, scipy.integrate
import matplotlib.pylab as plt


# Parametros
mu = 1.
beta = 1.

# condicoes iniciais
y0 = .0
v0 = .01

out0 = [y0, v0]

tMax = 100

T = scipy.linspace(0, tMax, 10000)


def vdp(out, t, beta, mu):

    y = out[0]
    v = out[1]

    dv = mu * (1. - y*y)*v - y
    dy = beta * v

    dout = [dy, dv]

    return dout

solution = scipy.integrate.odeint(vdp,
                                  out0,
                                  T,
                                  args=(beta, mu))

Y = solution[:, 0]
V = solution[:, 1]



'''
plt.figure()
plt.grid(True)
plt.xlabel('Tempo')
plt.ylabel('$y$')
plt.show()
'''


fig = plt.figure()

ax1 = fig.add_subplot(211)
ax1.plot(T, Y, 'r-')


ax2 = fig.add_subplot(212)
ax2.plot(Y, V, 'g-')

plt.show()