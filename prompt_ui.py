from langchain_openai import ChatOpenAI
import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

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

# Template
template = PromptTemplate(
    """ 
    Explain the research paper 
    '{paper_input}' 
    in a 
    {style_input} 
    style. Make the explanation 
    {length_input}.
    """,
    input_variables= ['paper_input', 'style_input', 'length_input']
)

prompt = template.invoke({
    'paper_input': paper_input,
    'style_input': style_input,
    'length_input': length_input
})

if st.button("Summarize"):
    result = model.invoke(prompt)
    st.write(result.content)