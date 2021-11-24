# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#streamlit run Deploy_Enduser.py [-- script args]

import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt
#import altair as alt
#import numpy as np
#import seaborn as sns

df = pd.read_csv('p4_labelled_tweets.csv')

df2=df["b_sentiment"]


"""
## Irish Population Twitter Sentiment: Abortion Referendum


Model Predictions
"""

s_values=df2.value_counts()

st.bar_chart(s_values)

"""
Where 0 = Neutral, 1 = Very Negative, 2 = Negative, 3 = Positive, 4 = Very Positive

"""

st.write(df.head())


df3 = pd.read_csv('labelled_tweets_sub_c.csv')

df4=df3["sentiment"]


"""

##

Manually labelled Data


"""

s_values_m=df4.value_counts()

st.bar_chart(s_values_m)

"""
Where 0 = Neutral, 1 = Very Negative, 2 = Negative, 3 = Positive, 4 = Very Positive

"""

st.write(df4.head())
