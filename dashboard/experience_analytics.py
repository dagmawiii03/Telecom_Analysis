import streamlit as st
import pandas as pd
import sys
import os

def application():
    st.title ('user_Experience_Analytics')
    st.header ("Data visualization")

    df_avgthr = pd.read_csv ('data/top10avgThroughput.csv')
    df_rtt = pd.read_csv('data/top10rtt.csv')
    df_tcp = pd.read_csv('data/top10tcp.csv')
    df_frqThr = pd.read_csv('data/most_freqAvgThr.csv')
    df_frqrtt = pd.read_csv('data/most_freqRTT.csv')
    df_frqtcp = pd.read_csv('data/most_freqTCP.csv')
