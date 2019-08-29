#! /usr/bin/env python3.7
# -*- coding: utf-8 -*-
# Author: Finn Folkerts, Vanessa Schreck
# Date: 2019 May 14

import pandas as pd
import calculations as calc

aws = pd.read_csv('results/aws_52k_scaled.csv', delimiter=';', encoding='utf-8-sig')
azure = pd.read_csv('results/azure_52k_scaled.csv', delimiter=';', encoding='utf-8-sig')
google = pd.read_csv('results/google_52k.csv', delimiter=';', encoding='utf-8-sig')
ibm = pd.read_csv('results/ibm_52k.csv', delimiter=';', encoding='utf-8-sig')

provider = [aws, azure, google, ibm]
services = ['Amazon Comprehend', 'Microsoft Azure Cognitive Service', 'Google Natural Language',
            'IBM Watson Natural Language Understanding']
issues = ['Gender', 'Origin', 'Nobiliary_particle']

# 2 Sample t-test/u-test for independent samples
test_results = pd.DataFrame(columns=['Provider', 'Issue', 'Test', 'Template_ID', 'Statistic', 'p_value', 'Cohens_d'])
i, j = 0, 0
for name in provider:
    for issue in issues:
        df1, df2 = calc.get_resultset(name, subset=issue)  # ,label='negative')
        for tid in df1['Template_ID'].drop_duplicates(keep='first'):
            df1_tid = df1['score'].loc[df1['Template_ID'] == tid]
            df2_tid = df2['score'].loc[df2['Template_ID'] == tid]
            stat, pvalue = calc.get_stats(df1_tid, df2_tid)
            cohens_d = calc.cohensd(df1_tid, df2_tid)
            test_results.loc[j] = services[i], issue, calc.get_stats(df1_tid, df2_tid).__class__, tid, stat, pvalue,\
                cohens_d
            j += 1
    i += 1
# save dataframe to csv file
test_results.to_csv(path_or_buf='results/ttest_52k.csv', index=False, sep=';', encoding='utf-8-sig')
