'''
version control- Github.com
'''
import streamlit as st
import google.generativeai as genai

st.title("code review and helper.")
code=st.text_area("enter your python code")
click=st.button("check the code.")
if click:
 genai.configure(api_key="AIzaSyAOyTzy2_CxvNV7eq0Oqm-m8sIyJSB4fZ8")

model = genai.GenerativeModel("gemini-1.5-flash")   
response = model.generate_content(f"check if the python {code} code is correct and if it is not correct help to find the error and give correct code.")
st.write(response.text)
