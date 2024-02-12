
# app dev framework
import streamlit as st

# import dependencies
from langchain.llms import GPT4All
from langchain import PromptTemplate, LLMChain

# python toolchain imprts
# from langchain.agents.agent_toolkits import create_python_agent
# from langchain.tools.python.tool import PythonREPLTool

# Path to weigth directory
PATH = r'C:\Users\Izzham Burhan\AppData\Local\nomic.ai\GPT4All\gpt4all-falcon-newbpe-q4_0.bin'


# Intance of llm
llm = GPT4All(model=PATH, verbose=True)

# Prompt Template
prompt = PromptTemplate(input_variables=['question'],
                        template="""
                        Question : {question}

                        Answer : Let's think step by step
                        """
                        )

# LLM chain
chain = LLMChain(prompt = prompt, llm=llm)

#  create a python agent
# python_agent = create_python_agent(llm =llm , tool=PythonREPLTool(), verbose=True)


st.title(':smile_cat: BorakGPT')


# Prompt text box
prompt = st.text_input('Jom Tanya apa apa')

# if we hit enter to this
if prompt :
    # pass the prompt to llm chain
    response = chain.run(prompt)

    # do this
    st.write(response)