import streamlit as st
import pandas as pd


if not st.session_state.get('quiz_passed', 0): #NEW
    st.header("🔒 You have not passed the trivia quiz. Go back to the home page.")
    st.stop
else:
    st.header('Weekly hours I put into the video games I own')
    st.write('I have 5 game below Fortnite, Minecraft, Roblox, Clash of Clans, and Clash Royale')
    Fornite = 22
    minecraft = 20
    roblox = 3
    clans = 12
    royale = 5
    
    df = pd.DataFrame({'fortnite': [Fornite], 'minecraft': [minecraft],
                       'roblox': [roblox], 'clans': [clans],
                       'royale': [royale]},
                      index = ['Weekly Hours'])
    df = df.transpose() #NEW
    st.bar_chart(df)





    
