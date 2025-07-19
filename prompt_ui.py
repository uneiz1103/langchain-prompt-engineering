from langchain_openai import ChatOpenAI
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.header('Research Tool')

paper_input = st.selectbox(
    "Select Research Paper Name",
    [
        "Select...",
        "Attention Is all you need",
        "BERT",
        "GPT-3",
        "Diffusion Models"
    ]
)

style_input = st.selectbox(
    "Select Explanation Style",
    [
        "Beginner-friendly",
        "Technical",
        "Code-Oriented",
        "Mathematical"
    ]
)

length_input = st.selectbox(
    "Select Input lenght",
    [
        "Short (1-2 paragraphs)",
        "Medium (3-5 paragraphs)" , 
        "Long (detailed)"
    ]
)


