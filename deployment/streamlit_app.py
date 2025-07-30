import streamlit as st
import eda
import prediction

st.set_page_config(
    page_title='Safe or Unsafe',
    layout='wide',
    initial_sidebar_state='expanded'
)

page = st.sidebar.selectbox('Pages', ('EDA', 'Prediction'))

if page == 'EDA':
    eda.run()

else:
    prediction.run()