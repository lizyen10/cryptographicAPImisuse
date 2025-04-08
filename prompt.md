Here are different types of prompts you can use to test how **prompt engineering** affects the accuracy of LLMs in detecting cryptographic API misuse:

---

### **1. Baseline Prompt (Minimal Information)**
*"Analyze the following Python code and identify any security vulnerabilities."*  
➡️ This prompt is vague and may lead to general security checks rather than focusing on cryptographic API misuse.

---

### **2. Targeted Security Prompt**
*"Analyze the following Python code and identify any **cryptographic API misuse**. Focus specifically on weak key usage, insecure modes, hardcoded secrets, and other cryptographic vulnerabilities."*  
➡️ This ensures the LLM looks specifically at cryptographic security issues rather than general security flaws.

---

### **3. Structured Prompt with Step-by-Step Analysis**
*"Analyze the following Python code and identify any cryptographic API misuse. Follow these steps:  
1. List all cryptographic function calls.  
2. Check if secure best practices are followed (key length, mode, entropy, etc.).  
3. Identify if function calls propagate insecure data across multiple functions.  
4. Provide a summary of vulnerabilities and suggestions for secure alternatives."*  
➡️ Encourages a **systematic review**, reducing the chance of the LLM missing interprocedural misuses.

---

### **4. Few-Shot Learning Prompt (Providing Examples)**
*"Here are examples of cryptographic API misuse and secure alternatives:  

❌ Insecure Example:  
```python
from Crypto.Cipher import AES  
cipher = AES.new("hardcodedkey123", AES.MODE_ECB)  # Weak key + ECB mode
```

✅ Secure Alternative:  
```python
from Crypto.Cipher import AES  
import os  
key = os.urandom(32)  
cipher = AES.new(key, AES.MODE_GCM)  # Secure key + GCM mode
```

Now, analyze the following Python code and identify any similar cryptographic API misuses."*  
➡️ **Providing examples helps guide the LLM’s expectations** and improves detection accuracy.

---

### **5. Chain-of-Thought (CoT) Prompt for Reasoning**
*"Analyze the following Python code for cryptographic API misuse. Explain your reasoning **step by step**, identifying potential security risks and how they could be exploited before providing a final answer."*  
➡️ Encourages **explainability**, making it easier to assess if the LLM correctly understands the vulnerabilities.

---

### **6. Taint Tracking Prompt (Interprocedural Focus)**
*"Analyze the following Python code for cryptographic API misuse. Specifically, trace **how cryptographic keys and sensitive data** are passed between functions and modules. Identify any cases where insecure data is used in cryptographic operations."*  
➡️ This helps test whether the LLM can **track data flow across functions**, which is crucial for interprocedural misuse.

---

### **7. Comparative Prompt (LLM Self-Evaluation)**
*"Analyze the following Python code for cryptographic API misuse.  
- First, identify any potential vulnerabilities.  
- Then, compare your findings against best practices from OWASP, NIST, or other security guidelines.  
- If there are discrepancies, explain why."*  
➡️ Encourages the LLM to **cross-check its own results** against known standards.

---

### **Testing & Evaluation Plan**
To measure the impact of these prompts on accuracy:
1. **Use a consistent set of cryptographic misuse test cases** (e.g., from PyCryptoBench).
2. **Run multiple LLMs** (e.g., GPT-4, Claude, Mistral) on each prompt.
3. **Compare accuracy & completeness** of the results.
4. **Analyze false positives and false negatives**.
5. **Test across different complexity levels** (single function vs. interprocedural).

Please analyze this code snippet for cryptographic API misuse. Begin your response with either YES, meaning there is cryptographic API misuse, or NO, meaning no cryptographic API misuse was detected, and explain your reasoning in one sentence


You are a cybersecurity specialist. You will be provided with a code snippet in python and your task is to analyze the code for cryptographic API misuses. Cryptographic API misuse is when developers utilize cryptographic libraries inappropriately due to not understanding proper usage or security rules, resulting in code vulnerable to attacks such as SSL/TLS man in the middle, predictability, ciphertext attack, brute force, and deserialization. When analyzing, please look for instances of these cryptographic API misuses, along with any other misuses you also detect: Using a Wildcard to Avoid Verification, Creating a Custom String to Avoid Verification of Certificates, Using an Unverified Context to Avoid HTTPS Verification, Using HTTP Instead of HTTPS, Using Insecure Random Number Generation, Using a Static and Insecure Salt, Using an Insecure Mode, Using Less Than 1,000 Iterations, Using an, Insecure Block Cipher, Using an Insecure Asymmetric Cipher, Using an Insecure Hash, Not Verifying the Json Web Token (JWT), Using a Deprecated or Invalid Transport Layer Security (TLS) Version, Using an Insecure Protocol, Using an Insecure Extensible Markup Language (XML) Deserialization, Using an Insecure YAML Ain’t Markup Language (YAML) Deserialization, Using an Insecure Pickle Deserialization, Not Properly Escaping Regular Expressions (regex).Begin your response with either YES, meaning there is cryptographic API misuse, or NO, meaning no cryptographic API misuse was detected, and explain your reasoning in one sentence.

Identify any cryptographic API misuse in this code: 

- do a third round of prompts, giving each type of crypto misuse from the benchmark?
- or just do that in second one - part of definition.
- define the type of crypto api misuse that you are looking for to the API. benchmark's definition may differ from what LLM thinks.
    - i did use paper 1's def of cryto api misuse, but adding in each type may help? 
    - if you give each type of misuse that each benchmark test is catered to, is that too obvious?
    - maybe give the attack surface it is representing? - paper 1 table 1

When analyzing, please look for instances of these cryptographic API misuses, along with any other misuses you also detect: Using a Wildcard to Avoid Verification, Creating a Custom String to Avoid Verification of Certificates, Using an Unverified Context to Avoid HTTPS Verification, Using HTTP Instead of HTTPS, Using Insecure Random Number Generation, Using a Static and Insecure Salt, Using an Insecure Mode, Using Less Than 1,000 Iterations, Using an, Insecure Block Cipher, Using an Insecure Asymmetric Cipher, Using an Insecure Hash, Not Verifying the Json Web Token (JWT), Using a Deprecated or Invalid Transport Layer Security (TLS) Version, Using an Insecure Protocol, Using an Insecure Extensible Markup Language (XML) Deserialization, Using an Insecure YAML Ain’t Markup Language (YAML) Deserialization, Using an Insecure Pickle Deserialization, Not Properly Escaping Regular Expressions (regex).

We identified and created misuse patterns that encompass 18
different potential cryptographic API misuses. Each potential
cryptographic API misuse type requires specific slicing and
variable verification. We extrapolate these tasks to potentially
misused modules. These misuse patterns are shown in Table I.
We chose these misuse patterns since they represent different
types of attack and attack surfaces. Identifying potential standard
library misuses or taint analysis using methods such as
“os.system” or “eval” is not cryptographic misuse and therefore
is beyond the scope of this work. Researchers and developers
can extend the current misuse patterns by including cryptographic
patterns in their specifications


    

we are testing interprocedrual, but just define crypto misuse to the AI. we want to test how well it is at detecting interprocedural crypto api misuse compared to the static tool, static tool just has rules on crypto api misuse, thus llm will get definition of crypto api misuse?
    - we do interprocedrual- Involve vulnerabilities spanning multiple methods, challenging the tool to trace complex method invocations. - we challenge the static tool and llm to see if it is accurate at detcting vulnerabilities between functions
- define interprocedrual? or just see how well ai is at detecting crypto api misuse in interprocedrual files?

-	This refines the prompt adding the intent in the user prompt as well. This helps make it more clear and specific. 
-	Adds some domain specificity with the definition of crypto api misuse.
-	Defines a role for the LLM
-	Usage of system and user, not just user
-	Uses reflection pattern, asking the LLM to give rationale

- uses user roles to influence how the model interprets the input - developer and user
- clear instructions
- one sentnece for consciseness, and cost and latency
- code snippets is text to reference?

Price of gpt 4o mini - gpt-4o-mini-2024-07-18
Input:
$0.150 / 1M tokens
Cached input:
$0.075 / 1M tokens
Output:
$0.600 / 1M tokens

run the script 3 times per prompt? and average the results, but analyze the results separately

testing all 3 prompts each 3 times (plus a few test runs earlier) came to 15 cents
