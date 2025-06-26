import streamlit as st
import pandas as pd

 
st.header("About")
st.subheader("MY sanity for this project")
st.write("It gets worse as a work more on this project as I write this I am one day 1 of the project with about already 4 hours put in. I will keep you posted")
st.subheader("My favorite animals")
st.write("I like most animals however some are mean and rude and thus I don't like those one's")
st.subheader("Hours I put into video games")
st.write("I put in too many hours into video games and why can't talk to people XOXOXO :)")
st.subheader("Trival")






def radio1():
    x = st.radio("First question: Do I like this class? (you're also forced to play as I hide the sidebar if you don't get all the answer selceted) If you are too lazy I did put the answer in the help Every Answer has something and there is a right answer(P.S these are all jokes)", #NEW
             options=['Yes', 'no', 'why ask?', 'I want to leave', 'maybe'],
             index = 4,
             help="no",
             key='q1')
    count = 0
    if x == "Yes":
        st.write('LOL really?')
    elif x == 'no':
        st.write('This is the right answer!!!!!')
        count += 1
    elif x == 'why ask?':
        st.write("Like really why do you ask you're clicking throught this because you were asking")
    elif x == 'I want to leave':
        st.write("I have not seen the sun for 2 days")
    else:
        st.write("Click through if you wondering")
    return count
def radio2():
    c = st.radio('second question: What time did I do this?', #NEW
                 ['a reasonable time', '2 hours before it was due', 'from the hours 12am-6am', 'ai did it for me so no time', 'somewhere someplace sometime'],
                 index = 4,
                 help='from the hours 12am-6am',
                 key = 'q2')
    count = 0
    if c == 'a reasonable time':
        st.write('you have too much faith in me')
    elif c == '2 hours before it was due':
        st.write('you have too little faith in me')
    elif c == 'from the hours 12am-6am':
        st.write('This is the right answer!!!!!')
        st.write('sadly :(')
        count += 1
    elif c == 'ai did it for me so no time':
        st.write('That would be wrong and vailtion of the GT ethics code or something')
    else:
        st.write('This is true I did do it somewhere someplace and sometime, now answer the question')
        st.write('If you can not tell I have not found out how to make it where no answer is selceted already silly me XOXOXO')
    return count


def radio3(): #NEW
    x = st.radio('last quetion: Can you spot the fact Professor howard lecture break rant',
                 ["How we shouldn't tip 5 guy employees", 'How you should like to youtube so you can get cheaper youtube premium',
                  'How to not to become a teacher and why should not become one because it is bad',
                  'How Professor Howard does not know his father and is trying to get his named changed', 'Fun Fact his wife is a physical threapist'],
                 index = 4,
                 help="How to not to become a teacher and why should not become one because it is bad",
                 key = 'q3')
    count = 0
    if x == "How we shouldn't tip 5 guy employees":
        st.write('first rant we got of him from the second lecture but I agree with him, if you make above minual wage you should not ask for a tip')
    elif x =='How you should like to youtube so you can get cheaper youtube premium':
        st.write('He lied to youtube for I think 2 years about how lived in Romainia and was only being charge 2 dollars per mouth for it')
    elif x== 'How to not to become a teacher and why should not become one because it is bad':
        st.write('This is the corrcet answer!!!!!')
        st.write("I think he like his job weither it reasearch or us I don't wanna know because I don't think I will like the answer")
        count += 1
    elif x== 'How Professor Howard does not know his father and is trying to get his named changed':
        st.write('None more explaination need')
    else:
        st.write('This is true he told me about when I sprained my ankle')
    return count


r1 = radio1()
r2 = radio2()
r3 = radio3()


def un_hide_sidebar(r1, r2, r3):
    total = r1 + r2 + r3
    if total == 3:
        st.sidebar.header("🎉 Page Unlocked!")
        st.sidebar.text("I don't have LinkedIn silly me.")
        st.session_state["quiz_passed"] = 1
    else:
        st.sidebar.header("❌ Try again to unlock the sidebar!")
        st.session_state['quiz_passed'] = 0

un_hide_sidebar(r1, r2, r3)





        
