import os
from selenium import webdriver
from langchain.llms import OpenAI
from langchain import PromptTemplate, LLMChain
from agent import agent_executor
from dotenv import load_dotenv

load_dotenv()

# Chrome Driver Initialization
options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=C:\\Users\\jonet\\AppData\\Local\\Google\\Chrome\\User Data\\Default")

os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_KEY")

template = """Question: {question}

Answer: Let's think step by step."""
prompt = PromptTemplate(template=template, input_variables=["question"])
llm = OpenAI()
llm_chain = LLMChain(prompt=prompt, llm=llm)


def new_request(userInput):
    return llm_chain.run(userInput)


def autoGTP(userInput):
    agent_executor.run(userInput)


agent_executor("Write a paper about the history Mac computers. I want the paper to be 5 paragraphs.")
