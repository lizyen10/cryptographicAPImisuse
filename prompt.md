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
