# No Roll Contendere (Cryptographic API Misuse Analysis)

The first rule of cryptography is, "Don't roll your own!" This means that programmers looking to add "security" to their application are going to leverage an existing cryptographic library (e.g., OpenSSL). Unfortunately, the most common cryptographic libraries are similar in complexity as rolling your own. Thus, a growing body of research seeks to identify misuses such cryptographic library's Application Programmer Interface (API). Note that a library's API is the set of ways that your software can interact with the library; there are secure and insecure ways to interact with a library. For this project, you will examine how a set of programs uses a cryptographic library's API. Conventionally, this analysis is intraprocedural, but your analysis will look at the opportunity and challenges of interprocedural API usage analysis. Your end goal is to identify API misuses.

## To Do After Spring Break
- first do research for papers on interprocedural cryptographic api misuse analysis - for related work and also to show if you bring something novel to the table, or if you are recreating the work of some paper. (can your paper be a reproduction?)
1. Build a tool for interprocedural analysis - start from interprocedural.md file
2. Paper will be something like: Interprocedural cryptographic API misuse analysis with CodeQL or something along those lines? Maybe will use more than just CodeQL
3. Background will delve into cryptographic api misuse and its dangers, and then intraprocedural analysis and how its the common one and how its done, then what interprocedural analysis brings to the table.
4. Have related work on interpreceural analysis of crypto api misuse, (do research on this!!) and show what your paper brings to the table
5. introduce your tool and methodology, and then the test cases and the actual testing, and results. then analyis of results and conclusions, then future work. 

## Outline
1. TBD - something like: Introduce cryptographic APIs and their uses – what cryptography helps secure (data) and why that is important for security. Then go into potential cryptographic API misuses and what dangers it poses. Then ...
2. Benchmarking tool to detect interprocedural cryptographic API misuse. Build interprocedural test cases and use tools capable of interprocedural analysis. Compare them to tools only capable of intraprocedural analysis?
3. Score and analyze the results of the benchmarking, and conclude which tools are best for interprocedural analysis, or for which test cases, or which combination of tools?

## Ideas
### Benchmarking tool

Benchmarking in code analysis refers to the process of systematically evaluating and comparing the performance, accuracy, and effectiveness of static or dynamic code analysis tools. It helps determine which tool performs best in detecting security vulnerabilities, code quality issues, or compliance violations.

Benchmarking helps answer questions like:
- Which tool detects the most security vulnerabilities (true positives)?
- Which tool generates the fewest false positives (incorrect warnings)?
- How fast does each tool analyze the code?
- How comprehensive is the tool in detecting cryptographic API misuse or other security flaws?

## Interprocedural API usage analysis

From project description:
- Examine how a set of programs uses a cryptographic library's API. 
- Conventionally, this analysis is intraprocedural, but your analysis will look at the opportunity and challenges of **interprocedural API usage analysis**. 
- Your end goal is to identify API misuses.

Your benchmarking tool **partially** addresses the project's goal, but it does not fully cover **interprocedural API usage analysis** as described. Let’s break it down:

---

### **🔍 What You're Doing with the Benchmarking Tool**
✅ Running static analysis tools (Bandit, Semgrep, CodeQL) on test cases  
✅ Measuring their effectiveness in detecting **cryptographic API misuse**  
✅ Comparing detection accuracy, false positives, performance, etc.  

---

### **⚠️ What’s Missing? (Interprocedural Analysis Focus)**
Your project description states:
> "Conventionally, this analysis is intraprocedural, but your analysis will look at the opportunity and challenges of interprocedural API usage analysis."

**Key difference:**
- **Intraprocedural analysis**: Only looks at **one function at a time** (e.g., checking if `hashlib.md5()` is used incorrectly in a single function).  
- **Interprocedural analysis**: Tracks **API usage across multiple functions and files** (e.g., checking if a key is hardcoded in one function and then improperly used in another function in a different module).  

### **❓ Does Benchmarking Cover Interprocedural API Analysis?**
❌ **Not fully.**  
- Your benchmarking tool evaluates **how well existing tools detect API misuse**, but **most static analysis tools are intraprocedural by default**.  
- The benchmarking tool **doesn’t analyze function calls across files**—it just checks how well existing tools do so.

---

### **🔧 How to Adapt Your Project for Interprocedural Analysis**
To properly address **interprocedural cryptographic API misuse**, you could:
1. **Extend your benchmark with interprocedural test cases.**  
   - Design code samples where **a cryptographic API is misused across multiple functions and modules**.
   - Check whether Bandit, Semgrep, or CodeQL can detect these issues.  

2. **Use or Modify an Analysis Tool for Interprocedural Detection.**  
   - **CodeQL** supports interprocedural analysis but may need custom queries.  
   - **Joern** (a security-focused code analysis tool) specializes in **interprocedural flow tracking**.  
   - **ML-based tools like Graph-based models** can also detect cross-function API misuse.

3. **Analyze the Limitations of Existing Tools.**  
   - Run experiments to show **how existing tools fail** at interprocedural cases.
   - Suggest improvements, such as **taint analysis across function calls**.

---

### **✅ Conclusion: Adjusting Your Project to Fully Cover the Requirement**
🔹 **YES,** your benchmarking **partially** contributes to interprocedural API analysis by showing how existing tools perform.  
🔹 **BUT**, you need to **evaluate their interprocedural capabilities specifically** or **extend your project to conduct interprocedural analysis directly**.  


Paper 8

In this part, we present an example of using the OpenAI API with the ChatGPT model. The provided Python code demonstrates how to interact with the API to generate a response for a given text prompt. This is a useful application for various tasks such as content generation, question-answering, and conversational AI.
The code begins by importing the necessary libraries and setting up the API key for authentication. A function called chat_with_gpt is defined, which takes the input prompt and makes an API call to the GPT model using the specified parameters. The generated response is then processed and printed to the console.
This example demonstrates the ease of integrating OpenAI’s ChatGPT API into your Python applications, enabling you to leverage the power of GPT models for a wide range of tasks.

1 import openai
2
3 openai . api_key = " your_openai_api_key_here "
4
5 def chat_with_gpt ( prompt ):
6 response = openai . Completion . create (
7 engine ="text - davinci -002 ",
8 prompt =prompt ,
9 max_tokens =50 ,
10 n=1,
11 stop =None ,
12 temperature =0.8 ,
13 )
14 return response . choices [0]. text . strip ()
15
16 prompt = " Write a brief introduction to the history of computers ."
17 response_text = chat_with_gpt ( prompt )
18
19 print ( response_text )

Importing required libraries: We start by importing the openai library, which is the official Python library
for OpenAI’s API.
- Setting the API key: We set the API key for OpenAI by assigning it to openai.api_key. Replace "your_openai_api_key_here" with your actual API key.
- Defining the chat_with_gpt function: We define a function called chat_with_gpt that takes a single argument, prompt. This function will call the OpenAI API and return the generated response

API call:
Inside the function, we use the openai.Completion.create() method to make an API call. This method
takes several parameters:
- engine: The ID of the GPT model. In our example, we use the "text-davinci-002" engine.
- prompt: The text prompt that we want the model to respond to.
- max_tokens: The maximum number of tokens (words or word pieces) in the generated response.
- n: The number of generated responses.
- stop: An optional sequence that indicates the end of a response.
- temperature: Controls the randomness of the output. A higher value makes the output more random, while a lower value makes it more deterministic.

- Processing the response: After making the API call, we extract the generated text from the response.choices[0].text attribute and remove any leading or trailing whitespace using the strip() method.

Using the function:
We define a variable prompt containing the text we want the model to respond to and then call the chat_with_gpt function with this prompt. The generated response is stored in the response_text variable.

Printing the response:
Finally, we print the generated response to the console using the print() function
