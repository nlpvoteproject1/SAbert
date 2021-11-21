# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#streamlit run Deploy_Enduser.py [-- script args]

import streamlit as st
import pandas as pd
import seaborn as sns
#import numpy as np

df = pd.read_csv('p4_labelled_tweets.csv')

df.head(5)


"""
## Irish Population Twitter Sentiment: Abortion Referendum

Model Predictions
"""

class_names = ['v negative','negative', 'neutral', 'positive','v positive']


ax = sns.countplot(x="b_sentiment", data=df)


st.bar_chart(class_names)



df2 = pd.read_csv('labelled_tweets_sub_c.csv')

df2.head(5)


"""
Manually labelled Data
"""

class_names2 = ['v negative','negative', 'neutral', 'positive','v positive']


ax = sns.countplot(x="sentiment", data=df2)


st.bar_chart(class_names2)