from langchain_openai import ChatOpenAI
import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate, load_prompt

load_dotenv()
model = ChatOpenAI()

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

template = load_prompt('template.json')



if st.button("Summarize"):
    chain = template | model
    result = chain.invoke({
    'paper_input': paper_input,
    'style_input': style_input,
    'length_input': length_input
    })

    st.write(result.content)