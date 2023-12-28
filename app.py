import streamlit as st
import sys
from model import connector


st.title("Chatbot with Simple Book API")

USER_AVATAR = "👤"
BOT_AVATAR = "🤖"

password = st.sidebar.text_input("Enter Your Open API Key", type="password",placeholder="sk-j*****************************")

st.sidebar.markdown('<a href="https://pk.linkedin.com/in/therafiali" target="_blank"><img src="https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg" width="30" height="30"></a>', unsafe_allow_html=True)
st.sidebar.write("Here is my linkedin")

st.sidebar.markdown('<a href="https://github.com/therafiali" target="_blank"><img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width="30" height="30"></a>', unsafe_allow_html=True)
st.sidebar.write("Here is my Github")

st.sidebar.markdown('<a href="https://twitter.com/therafiali" target="_blank"><img src="https://cdn4.iconfinder.com/data/icons/social-messaging-ui-color-shapes-2-free/128/social-twitter-square2-512.png" width="30" height="30"></a>', unsafe_allow_html=True)
st.sidebar.write("Here is my Twitter")



with st.form(key="my_form"):
    text = st.text_area("Enter your text here",placeholder="How Can I Help You!")
    
    
    if st.form_submit_button("Submit"):
        result = connector(password,text)
        st.markdown(f"<div style='background-color:#D4F1F4; padding:10px; margin-bottom: 20px; border-radius: 10px;'>{result}</div>", unsafe_allow_html=True)

