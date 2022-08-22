import streamlit as st

st.set_page_config(page_title="showLatex", page_icon="random")#页面基本设置
st.title('showLatex')

st.text_input("Latex Code", key="latexcode") # 输入latex的框

if st.button('Summit'):
    st.latex(st.session_state.latexcode)
