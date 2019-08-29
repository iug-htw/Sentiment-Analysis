from scipy import stats
import numpy as np
np.seterr(all='raise')


# capitalize first letter
def capitalize(string, lower_rest=False):
    return string[:1].upper() + (string[1:].lower() if lower_rest else string[1:])


# function to calculate Cohen's d for independent samples
def cohensd(df1, df2):
    if len(df1) < 2 or len(df2) < 2:
        return 'nan'
    else:
        try:
            # calculate the size of samples
            n1, n2 = len(df1), len(df2)
            # calculate the variance of the samples
            s1, s2 = np.var(df1, ddof=1), np.var(df2, ddof=1)
            # calculate the pooled standard deviation
            s = np.sqrt(((n1 - 1) * s1 + (n2 - 1) * s2) / (n1 + n2 - 2))
            # calculate the means of the samples
            u1, u2 = np.mean(df1), np.mean(df2)
            # calculate the effect size
            return (u1 - u2) / s
        except FloatingPointError:
            return np.nan


def get_resultset(df, subset, label='all'):
    if label == 'positive' or label == 'Positive':
        df = df[df['label'] == 'Positive']
    elif label == 'neutral' or label == 'Neutral':
        df = df[df['label'] == 'Neutral']
    elif label == 'negative' or label == 'Negative':
        df = df[df['label'] == 'Negative']
    else:
        pass

    subset = capitalize(subset, lower_rest=True)
    df_de = df[(df['Origin'] == 'de')]

    if subset == 'Gender':
        return df[(df[subset] == 'male')], df[(df[subset] == 'female')]
    elif subset == 'Origin':
        return df_de[(df_de['Nobiliary_particle'] == 'no')], df[(df[subset] == 'tr')]
    elif subset == 'Nobiliary_particle':
        return df_de[(df_de[subset] == 'yes')], df_de[(df_de[subset] == 'no')]


def get_stats(df1, df2):
    """
    Calculates whether t-test or u-test must be applied and its result.
    Keyword arguments\\:
          * df1 -- pandas DataFrame1
          * df2 -- pandas DataFrame2
    """
    # try:
    df1 = df1.reset_index(drop=True)
    df2 = df2.reset_index(drop=True)
    if not df1.equals(df2):
        try:
            # perform Anderson-Darling test to check if data comes from normal distribution
            sta1, crit1, sig1 = stats.anderson(df1)
            sta2, crit2, sig2 = stats.anderson(df2)

            if (sta1 <= crit1.item(4)) and (sta2 <= crit2.item(4)):
                # perform independent t-test for normal distributed data (alpha=0.01)
                return stats.ttest_ind(df1, df2)
            else:
                try:
                    # perform Mann-Whitney U test for non-normal distributed data
                    return stats.mannwhitneyu(df1, df2, alternative='two-sided')
                except ValueError:
                    return np.nan, np.nan
        except FloatingPointError:
            return stats.mannwhitneyu(df1, df2, alternative='two-sided')
    else:
        return np.nan, np.nan


def ttest_paired(df1, df2):
    if len(df1) < 2 or len(df2) < 2:
        return 'nan', 'nan'
    else:
        try:
            stat, p = stats.ttest_rel(df1, df2)
            return stat, p
        except Exception as err:
            print(err)
            return 'nan', 'nan'


def transform_score(df):
    for row in df.itertuples(index=True):
        value = (getattr(row, 'positive') - getattr(row, 'negative'))/(getattr(row, 'positive')
                                                                       + getattr(row, 'negative')
                                                                       + getattr(row, 'neutral'))
        df.loc[row[0], 'score'] = value
    return df
