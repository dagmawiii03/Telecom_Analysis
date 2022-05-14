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

    st.header("Top 10 Users Experience metrics")
    st.subheader("Average Throughput")
    st.dataframe(df_avgthr)
    st.bar_chart(df_avgthr['Average throughput'])

    st.subheader("Round Trip Time")
    st.dataframe(df_rtt)
    st.bar_chart(df_rtt['Average RTT'])

    st.subheader("TCP")
    st.dataframe(df_tcp)
    st.bar_chart(df_tcp['Average TCP'])

    st.header("Most Frequenct Users")
    st.subheader('frquent Average Throughput')
    st.dataframe(df_frqThr)
    st.bar_chart(df_frqThr['0'])

    st.subheader("frquent Round Trip Time")
    st.dataframe(df_frqrtt)
    st.bar_chart(df_frqrtt['0'])

    st.subheader("frquent TCP")
    st.dataframe(df_frqtcp)
    st.bar_chart(df_frqtcp['0'])
