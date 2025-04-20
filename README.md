# Detecting Interprocedural Cryptographic API Misuse in Python

In this project I compare the detection ability of Semgrep and gpt-4o-mini for interprocedural cryptographic API misuse in Python test cases. 

## Installations
- pip install openai
- pip install python-dotenv

## OpenAI API
- https://openai.com/api/
- To use this repo, you need an API key
- Pricing depends on the model. I use gpt-4o-mini-2024-07-18. 
    - https://platform.openai.com/docs/pricing
- Initial $5 charge to start using the API

## Benchmark Database
- PyCryptoBench: https://github.com/franceme/pycryptobench
- Downloaded their sqlite file to my repo since DBHub.io (where it is originally hosted) is gone. 
- Parsed through database and isolated interprocedural test cases in test.py. 

## Implementation

I downloaded the VS code extension of Semgrep, version 1.10.3, and was able to access and run this extension in a virtual environment running WSL: Ubuntu-24.04. 

Through the VS code extension, I ran Semgrep on all the test cases in my workspace and manually went through the results, flagging them as true positive, false positive, true negative, or false negative, and noting the reasoning given. 

I accessed the GPT-4o-mini model through OpenAI’s API through a Python script, api.py, in VS code. My script automated the counting of false positives, false negatives, true negatives, and true positives, and also printed the LLM output to a file, api_output.txt, for manual analysis of the responses. 

Since LLMs have variable responses to the same prompt, to account for this variability, I ran the script 3 times on each of the 3 prompts and averaged the results for each prompt to account for differences in LLM responses.

## Files
- test.py
    - File to parse through PyCryptoBench sqlite file and grab relevant test cases
- api.py
    - File to access OpenAI API for LLM testing
- test_api.py
    - File to check for accurate parsing of files and detection of misuse for api.py
    - Created to minimize the amount of times one has to run api.py and actually call the API
- api_output.py
    - Initially blank. The file api.py writes the LLM output to each run.
    - I copied each test run's output to its own file in the llm_output directory. 
    - api_output_1, 2, 3 are for prompt 1
    - api_output_4, 5, 6 are for prompt 2
    - api_output_7, 8, 9 are for prompt 3
- prompt.md
    - holds the prompts I used for the LLM testing
- calculate.py
    - file to calculate recall, precision, F score, and F2 score
- api_results.md
    - Holds the evaluation results for the LLM after each test, and the averaged results I used for calculations
- test_files/
    - The PyCryptoBench test files (filtered by script in test.py). Divided into subdirectories Rule 0 through 18, each with folders HasVuln (has vulnerability) and NoVuln (does not have vulnerability). 

## Running this repo
- To run testing with Semgrep, download the VS code extension of Semgrep from semgrep.dev. After intstallation, click the Semgrep extension icon and click, Semgrep: scan all files in workspace. 
- To run testing with the LLM, get an API key from OpenAI, and then put it in an .env file as MY_API_KEY = your_api_key in the same directory as api.py. Navigate to api.py and run ```python api.py```.