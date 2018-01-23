#!/bin/env python
# -*- coding: utf-8 -*-

"""
This package produces a button that closes all subplots upon click.

.. versioncreated:: 1.0

.. codeauthor:: Oliver James Hall <ojh251@student.bham.ac.uk>
"""

import matplotlob.pyplot as plt
from matplotlib.widgets import Button

def close_plots():
    '''
    A function that plots a button to instantly close all subplots. Useful when
    plotting a large number of comparisons.

    Returns:
        matplotlib.figure.Figure: 1 by 1 plot containing a 'close all' button.

        matplotlib.widgets.Button: A button widget required for button function.

    '''
    fig, ax = plt.subplots(figsize=(1,1))
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    closeax =plt.axes([0.1,0.1,0.8,0.8])

    button = Button(closeax, 'Close Plots', color='white', hovercolor='r')
    return fig, button

def close(event):
    ''' A simple plt.close('all') function for use with close_plots().'''
    plt.close('all')
