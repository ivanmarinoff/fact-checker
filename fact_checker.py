from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains import SimpleSequentialChain
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.callbacks import get_openai_callback
import sys
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
os.environ.get("OPENAI_API_KEY")

#  # This is a config to streamlit
# st.set_page_config(page_title="Fact Checker", page_icon=":robot:", layout="centered")
# st.header("Fact Checker")
#
#
# def get_text():
#     input_text = st.text_area(label="Enter question", key="input_text")
#     return input_text
#
# input_text = get_text()
#
# st.markdown("## Answer is:")



def fact_check(question):
    llm = OpenAI(temperature=0.7)
    template = """{question}\n\n"""
    prompt_template = PromptTemplate(input_variables=["question"], template=template)
    question_chain = LLMChain(llm=llm, prompt=prompt_template)

    template = """Here is a statement:
    {statement}
    Make a bullet point list of the assumptions you made when producing the above statement.\n\n"""
    prompt_template = PromptTemplate(input_variables=["statement"], template=template)
    assumptions_chain = LLMChain(llm=llm, prompt=prompt_template)

    template = """Here is a bullet point list of assertions:
    {assertions}
    For each assertion, determine whether it is true or false. If it is false, explain why.\n\n"""
    prompt_template = PromptTemplate(input_variables=["assertions"], template=template)
    fact_checker_chain = LLMChain(llm=llm, prompt=prompt_template)

    template = """In light of the above facts, how would you answer the question '{}'""".format(question)
    template = """{facts}\n""" + template
    prompt_template = PromptTemplate(input_variables=["facts"], template=template)
    answer_chain = LLMChain(llm=llm, prompt=prompt_template)

    overall_chain = SimpleSequentialChain(chains=[question_chain, assumptions_chain, fact_checker_chain, answer_chain],
                                          verbose=True)

    return overall_chain.run(question)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        question = input(sys.argv[1])  # added input()
    else:
        question = f"Your question is: {input()}\n"
    print(question)
    answer = fact_check(question)
    print(answer)
    # st.markdown(answer)
    # if input_text:
    #     formatted_answer = fact_check(question=answer)
    #
    #     st.write(answer)

    llm = OpenAI(model_name="text-davinci-002", n=2, best_of=2)
    with get_openai_callback() as cb:
        result = llm(question)
        print(f"Token Usage Tracking: {cb.total_tokens}")


