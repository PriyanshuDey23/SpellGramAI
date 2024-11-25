from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
import os
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain

from prompt  import *


# Load environment variables from the .env file
load_dotenv()

# Access the environment variables just like you would with os.environ
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")




# Response Format For my LLM Model
def checker_chain(input_text):
    # Define the LLM
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-002", temperature=1, api_key=GOOGLE_API_KEY)  
    # Define the prompt
    PROMPT_TEMPLATE = PROMPT  # Imported
    prompt = PromptTemplate(
            input_variables=["input_text"], # input in prompt
            template=PROMPT_TEMPLATE,
        )
      
    llm_chain = LLMChain(llm=llm, prompt=prompt)

    # Generate response
    response = llm_chain.run({"input_text": input_text})
    return response

# Streamlit app
st.set_page_config(page_title="SpellGramAI")
st.header("SpellGramAI")

# Input text
text = st.text_area("Enter your incorrect text", height=200)

# Summarize button
if st.button("Summarize"):

        response = checker_chain(input_text=text)
        st.write (response)
