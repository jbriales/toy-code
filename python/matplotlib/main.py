#!/usr/bin/env python2
# coding=utf-8
"""
Toy example for plotting
"""
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


def main():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Set up the grid in polar
    theta = np.linspace(0, 2 * np.pi, 90)
    r = np.linspace(0, 3, 50)
    tt, rr = np.meshgrid(theta, r)

    # Then calculate xx, yy, and zz
    xx = rr * np.cos(tt)
    yy = rr * np.sin(tt)
    zz = np.sqrt(xx ** 2 + yy ** 2) - 1

    # Set the zz values outside your range to NaNs so they aren't plotted
    # zz[zz < 0] = np.nan
    # zz[zz > 2.1] = np.nan
    ax.plot_wireframe(xx, yy, zz)
    # Does it work if coordinates are flattened beforehand (1D array instead of 2D mesh?)
    try:
        ax.plot_wireframe(xx.flatten(), yy.flatten(), zz.flatten())
    except ValueError:
        print("Caught error: Arguments xx,yy,zz must be 2-dimensional.")

    # ax.set_zlim(0, 2)

    plt.show()

    return
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Make data
    u = np.linspace(0, 2 * np.pi, 10)
    v = np.linspace(0, np.pi, 10)
    # u = np.linspace(0, 2 * np.pi, 100)
    # v = np.linspace(0, np.pi, 100)
    xx = 10 * np.outer(np.cos(u), np.sin(v))
    yy = 10 * np.outer(np.sin(u), np.sin(v))
    zz = 10 * np.outer(np.ones(np.size(u)), np.cos(v))

    # Plot the surface
    ax.plot_surface(xx, yy, zz, color='b', alpha=0.1)
    ax.plot_surface(0.25*xx, 0.25*yy, 0.25*zz, color='r', alpha=1)

    plt.show()

    return
    # Plot data
    x = np.linspace(0, 5, 20)
    y = x ** 2

    # A figure with manual axes
    fig = plt.figure()
    axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])  # left, bottom, width, height (range 0 to 1)
    curve = axes.plot(x, y, 'r', alpha=0.1, label=r"$y = x^2$")
    axes.set_xlabel(r'$x$')
    axes.set_ylabel(r'$y$')
    axes.set_title('the new title')
    axes.grid(True)

    axes_inner = fig.add_axes([0.2, 0.5, 0.4, 0.3])  # inset axes
    axes_inner.plot(y, x, 'g', label=r"$x = \sqrt{y}$")
    axes_inner.set_xlabel(r'$y$')
    axes_inner.set_ylabel(r'$x$')
    axes_inner.set_title('inverse')

    axes.legend(loc='best')
    axes_inner.legend(loc='best')

    plt.show()
    return

    # A figure with automatic and tight axes
    fig, axes = plt.subplots(nrows=1, ncols=2)
    for ax in axes:
        ax.plot(x, y, 'r')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title('title')

    fig.tight_layout()
    plt.show()

    print("Plot done")


if __name__ == '__main__':
    main()
