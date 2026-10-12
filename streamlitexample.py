import streamlit as st
import time

def do_something():
    print('a button click')
    
st.title("welcome to streamlit tutorial")
st.header('H2')  
st.subheader('H3')

st.write('text, df, chart, dict — auto renders')

st.markdown('**Bold** and *italic*')

name = st.text_input('Your name', placeholder='e.g. Aarav')
st.write(name)
print(name)

text = st.text_area('Paste text', height=200)
choice = st.selectbox('Pick one', ['A','B','C'])

flag = st.checkbox('Include hashtags', value=True)

file = st.file_uploader('Upload', type=['txt','pdf'])

if st.button('Go', type='primary'): 
    do_something()
    
st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

if st.button("Aloha", type="tertiary"):
    st.write("Ciao")
    
col1, col2 = st.columns(2)  
with col1: 
    st.write('A')
    st.button('col1',type='secondary')
    
with col2:
    st.write('B')
    st.selectbox('course',['genai','python','salesforce'])
    
with st.sidebar: 
    st.header('Settings')
    temp = st.slider('Temperature', 0.0, 2.0, 0.7)
    
with st.expander('Show more'): 
    st.write('details')
    st.write('summary point')
    
t1,t2 = st.tabs(['Tab1','Tab2'])  
with t1: 
    st.write('...')
    
with t2:
    st.write('......')
    st.text_input('entername')
    
with st.spinner('Loading...'): 
    time.sleep(5)

st.success('Done!')  
st.error('Failed!') 
st.info('FYI')

with st.chat_message('user'): 
    st.write('hello')
    
msg = st.chat_input('Type...')
st.write(msg)

