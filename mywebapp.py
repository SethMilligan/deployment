import streamlit as st 

st.title("My Streamlit App")

st.header("This is my containerized app")

if 'buttonState' not in st.session_state:
    st.session_state.buttonState = False

def clickFn():
    st.session_state.buttonState = True

st.button("Click me!", on_click=clickFn)

if st.session_state.buttonState:
    st.write("You've clicked this button!")

st.button("Reset")