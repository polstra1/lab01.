import streamlit as st
import pandas as pd


if not st.session_state.get('quiz_passed', 0): #NEW
    st.header("🔒 You have not passed the trivia quiz. Go back to the home page.")
    st.stop()
else:
    st.header("My sanity for this project")
    st.subheader("This chart below shows what happens to my sanity the more time I spend on this porject")
    hours = st.slider("How many hours I spent on this project", 0, 50)
    x = list(range(hours + 1))
    y = [max(0, 100 - h * 2) for h in x]
    df = pd.DataFrame({'Hours': x, 'Hope(%)': y})
    df = df.set_index('Hours') 
    st.line_chart(df) #NEW
        




