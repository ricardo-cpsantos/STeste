import streamlit as st

st.title("hi world")

with st.echo():
    a=1
    b=2
    
with st.echo():
    c=a+b
    
st.write(c)


