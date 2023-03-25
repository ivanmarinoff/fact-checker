# fact checking with prompt chaining

This repo is a simple demonstration of using [langchain](https://github.com/hwchase17/langchain) \
and concept by [Jasper](https://twitter.com/0xjasper) to do fact-checking with prompt chaining. \
How it works:
- you ask your desired LLM a question
- the LLM generates an initial answer to the question
- the LLM self-interrogates what the assumptions were that went into that answer
- the LLM sequentially determines if each of these assumptions are true
- the LLM generates a new answer to the question, incorporating the new information

## to run
We using OpenAI’s APIs, so we will first need to install their SDK:
`pip install openai`

In advance, in the root directory of the project, you need to create an `.env` \
file with the recorded value of your preston API key.
Then import your personal API key using this command:
`import os`\
`from dotenv import load_dotenv`\
`load_dotenv()`\
`os.environ.get("OPENAI_API_KEY")`\
Also, follow these API key security recommendations:
`https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety`

Make sure you have langchain installed (`pip install langchain`). Then run

`python3 fact_checker.py 'insert question here'`

*Be sure to wrap your question in quotes if you're passing it as a command line argument,\
or use the direct way I added to write questions in the input console.*

## example

Question: *"What type of mammal lays the biggest eggs?"*


**Initial answer:**
The biggest eggs laid by any mammal belong to the elephant.

**Assumptions made:**
- The elephant is a mammal 
- Mammals lay eggs 
- Eggs come in different sizes 
- Elephants lay bigger eggs than other mammals

**Verification of assumptions:**
- The elephant is a mammal: TRUE 
- Mammals lay eggs: FALSE - Most mammals give birth to live young.
- Eggs come in different sizes: TRUE 
- Elephants lay bigger eggs than other mammals: FALSE - Elephants do not lay eggs.

**New answer:**
This question cannot be answered because elephants do not lay eggs and most mammals give birth to live young.

## credits
Proof of concept by [Jasper](https://twitter.com/0xjasper)

Huge thanks to @hwchase17 and the langchain project!
