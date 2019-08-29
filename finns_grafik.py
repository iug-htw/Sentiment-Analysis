#! /usr/bin/env python3.7
# -*- coding: utf-8 -*-
# Author: Vanessa Schreck
# Date: 2019 August 26

import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable


ONLY_STATISTICALLY_RELEVANT_VALUES = True

# setting the font to Latex font
params = {'text.usetex': True,
          # 'font.size': 9,
          'font.family': 'STIXGeneral',  # 'lmodern',
          'mathtext.fontset': 'cm',
          'text.latex.unicode': True,
          }
plt.rcParams.update(params)

ttest = pd.read_csv('C:\\Users\\Schreck\\azk_sentiment\\results\\ttest_52k.csv', delimiter=';')

provider_title = {'Amazon Comprehend': 'Amazon',
                  'Google Natural Language': 'Google',
                  'IBM Watson Natural Language Understanding': 'IBM',
                  'Microsoft Azure Cognitive Service': 'Microsoft'}

issue_titles = {'Gender': 'Gender',
                'Origin': 'Origin',
                'Nobiliary_particle': 'Nobility'}


def plot_vline(ax, height):
    a_not_yet, b_not_yet = True, True
    for i, d in enumerate(height):
        if d >= 0 and a_not_yet is True:
            a = i - 1
            a_not_yet = False
        if d > 0 and b_not_yet is True:
            b = i
            b_not_yet = False
    ax.axvline(x=(a + b) / 2, c='red', linewidth=.65)


def plot_broken_axis(ax, x, height):
    divider = make_axes_locatable(ax)
    ax2 = divider.new_vertical(size="100%", pad=0.1)
    fig.add_axes(ax2)

    x0, height0 = zip(*[(x, h) for x, h in zip(x, height) if h < -5])
    x0 = list(x0)
    height0 = list(height0)
    x0.append(x[-1])
    height0.append(0)
    ax.bar(x0, height0, width=.05)
    ax.set_ylim(-6 * 10 ** 14, -2000000)
    ax.spines['top'].set_visible(False)

    ax2.bar(x, height, width=.05)
    ax2.set_ylim(-2, 1.8)
    ax2.tick_params(bottom="off", labelbottom='off')
    ax2.spines['bottom'].set_visible(False)
    ax2.set_xticks([])

    # From https://matplotlib.org/examples/pylab_examples/broken_axis.html
    d = .015  # how big to make the diagonal lines in axes coordinates
    # arguments to pass to plot, just so we don't keep repeating them
    kwargs = dict(transform=ax2.transAxes, color='k', clip_on=False)
    ax2.plot((-d, +d), (-d, +d), **kwargs)  # top-left diagonal
    ax2.plot((1 - d, 1 + d), (-d, +d), **kwargs)  # top-right diagonal

    kwargs.update(transform=ax.transAxes)  # switch to the bottom axes
    ax.plot((-d, +d), (1 - d, 1 + d), **kwargs)  # bottom-left diagonal
    ax.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)  # bottom-right diagonal

    return ax2


fig, axes = plt.subplots(4, 3, figsize=(17.6 / 2.54, 13.2/ 2.54), frameon=False)


for row, provider in enumerate(['Amazon Comprehend', 'Google Natural Language',
                                'IBM Watson Natural Language Understanding', 'Microsoft Azure Cognitive Service']):
    print(provider)
    for col, issue in enumerate(['Gender', 'Origin', 'Nobiliary_particle']):
        print('\t' + issue)
        data = ttest.loc[(ttest['Provider'] == provider) & (ttest['Issue'] == issue)]
        data_an = data.loc[~data['Cohens_d'].isna()]
        # if provider == 'Microsoft Azure Cognitive Service' and issue == 'Nobiliary_particle':
        #     data_an = data_an.loc[data_an['Cohens_d'] > -5]
        if ONLY_STATISTICALLY_RELEVANT_VALUES is True:
            data_an = data_an.loc[data_an['p_value'] <= .05]

        x = list(range(len(data_an)))
        height = sorted(data_an['Cohens_d'].to_list())
        if provider == 'Microsoft Azure Cognitive Service' and issue == 'Nobiliary_particle':
            ax2 = plot_broken_axis(axes[3][2], x, height)
            plot_vline(ax2, height)
            plot_vline(axes[3][2], height)
            # for Microsoft/Nobility, fix y labels, so that decimals are avoided (otherwise they overlap)
            axes[3][2].set_yticks([-5 * 10 ** 14])
            axes[3][2].set_yticklabels(['$-5 \cdot 10^{14}$'])
            ax2.set_yticks([-1, 0, 1])
            ax2.set_yticklabels([-1, 0, 1])
        elif provider == 'Microsoft Azure Cognitive Service' and issue == 'Origin':
            # plot no red line for Microsoft/Origin (which is empty)
            axes[row][col].spines['top'].set_visible(False)
            axes[row][col].spines['right'].set_visible(False)
            axes[row][col].spines['bottom'].set_visible(False)
            axes[row][col].spines['left'].set_visible(False)
            axes[row][col].set_yticklabels([])
            axes[row][col].set_yticks([])
        else:
            axes[row][col].bar(x, height, width=.05)
            # plot red line
            plot_vline(axes[row][col], height)

        # remove xticks
        axes[row][col].set_xticks([])

        # label provider and issues
        if row == 3:
            axes[row][col].set_xlabel(issue_titles[issue])
        if col == 0:
            axes[row][col].set_ylabel(provider_title[provider])


if ONLY_STATISTICALLY_RELEVANT_VALUES is True:
    fig.savefig('C:\\Users\\Schreck\\azk_sentiment\\results\\finns_grafik_only_statistically_relevant_values.eps', format='eps')
else:
    fig.savefig('C:\\Users\\Schreck\\azk_sentiment\\results\\finns_grafik.eps', format='eps')
plt.show()