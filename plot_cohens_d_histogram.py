import pandas as pd
import matplotlib.pyplot as plt
import os


# setting the font to Times Roman and enabling Tex font
params = {'text.usetex': True,
          'font.family': 'Times Roman'}
plt.rcParams.update(params)

# load data
PARENT_FOLDER = os.path.dirname(os.path.realpath(__file__))
ttest = pd.read_csv(PARENT_FOLDER + '/results/ttest_52k.csv',
                    delimiter=';')


provider_title = {'Amazon Comprehend': 'Amazon',
                  'Google Natural Language': 'Google',
                  'IBM Watson Natural Language Understanding': 'IBM',
                  'Microsoft Azure Cognitive Service': 'Microsoft'}

issue_titles = {'Gender': 'Gender',
                'Origin': 'Origin',
                'Nobiliary_particle': 'Nobility'}


def plot_vline(ax, height):
    # find indices of largest negative and smallest positive entry
    a_not_yet, b_not_yet = True, True
    for i, d in enumerate(height):
        if d >= 0 and a_not_yet is True:
            a = i - 1
            a_not_yet = False
        if d > 0 and b_not_yet is True:
            b = i
            b_not_yet = False
    # plot a red vertical line in the middle of these two indices
    ax.axvline(x=(a + b) / 2, c='red', linewidth=.65)


def main():
    fig, axes = plt.subplots(4, 3,
                             figsize=(17.6 / 2.54, 13.2 / 2.54),
                             frameon=False
                             )

    # adjust spacing between subplots
    fig.subplots_adjust(hspace=0.15, wspace=0.26)

    for row, provider in enumerate(['Amazon Comprehend',
                                    'Google Natural Language',
                                    'IBM Watson Natural Language Understanding',
                                    'Microsoft Azure Cognitive Service']):
        for col, issue in enumerate(['Gender',
                                     'Origin',
                                     'Nobiliary_particle']):
            # set y limits and labels (same for all subplots)
            axes[row][col].set_ylim(-15, 15)
            axes[row][col].set_yticks([-10, 0, 10])
            axes[row][col].set_yticklabels(['$-10$', 0, 10])

            # get data to be plotted
            data = ttest.loc[(ttest['Provider'] == provider) & (ttest['Issue'] == issue)]
            # get rid of NaNs
            data_an = data.loc[~data['Cohens_d'].isna()]
            # only plot statistically significant values
            data_an = data_an.loc[data_an['p_value'] <= .05]

            x = list(range(len(data_an)))
            height = sorted(data_an['Cohens_d'].to_list())

            # plot bars and red lines
            if provider == 'Microsoft Azure Cognitive Service' and issue == 'Origin':
                # plot nothing for Microsoft/Origin
                axes[row][col].spines['top'].set_visible(False)
                axes[row][col].spines['right'].set_visible(False)
                axes[row][col].spines['bottom'].set_visible(False)
                axes[row][col].spines['left'].set_visible(False)
                axes[row][col].set_yticklabels([])
                axes[row][col].set_yticks([])
            else:
                # bar plot
                axes[row][col].bar(x, height, width=.05)
                # plot red line
                plot_vline(axes[row][col], height)

            # remove xticks
            axes[row][col].set_xticks([])

            # label provider and issues
            if row == 3:
                axes[row][col].set_xlabel(issue_titles[issue], labelpad=7)
            if col == 0:
                axes[row][col].set_ylabel(provider_title[provider])

    fig.savefig('C:\\Users\\Schreck\\azk_sentiment\\results\\cohens_d_histogram.eps', format='eps')


if __name__ == '__main__':
    main()
