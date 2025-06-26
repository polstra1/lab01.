import streamlit as st
import pandas as pd


if not st.session_state.get('quiz_passed', 0): #NEW
    st.header("🔒 You have not passed the trivia quiz. Go back to the home page.")
    st.stop
else:
    st.header("Favorite Animal")
    st.write('My favorite animal has two key characteristic. How fluffy it is and how nice is it.')
    fluffy = st.slider('How fluffy the animal is', 0, 50)
    nice = st.slider('How nice the animal is',0, 50)
    df = pd.DataFrame({'Fluffy': [fluffy], 'Nice': [nice]}, index=['Animal'])
    st.bar_chart(df) #NEW
