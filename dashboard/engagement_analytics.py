import streamlit as st
import pandas as pd
import os
import sys

def application():

    st.title("User Engagement Analysis")

    st.header("Data Visualization")
    df_email = pd.read_csv('data/top10_email_users.csv')
    df_game = pd.read_csv('data/top10_gameApp_users.csv')
    df_google = pd.read_csv('data/top10_google_users.csv')
    df_netflix = pd.read_csv('data/top10_netflix_users.csv')
    df_otherAct = pd.read_csv('data/top10_otherAct_users.csv')
    df_social = pd.read_csv('data/top10_socialMedia_users.csv')
    df_youtube = pd.read_csv('data/top10_youtube_users.csv')
    df_session = pd.read_csv('data/top10_user_session.csv')
    df_DLUL = pd.read_csv('data/top10_DLUL_users.csv')

    st.header("Top 10 Users Engaged Per Each Application")
    st.subheader("Email App")
    st.dataframe(df_email)
    st.bar_chart(df_email.Email_Total_Data)

    st.subheader("Game")
    st.dataframe(df_game)
    st.bar_chart(df_game.Gaming_Total_Data)