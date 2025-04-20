## Prompt 1
- "role": "user"
- "content": f"Please analyze this code snippet for cryptographic API misuse. Begin your response with either YES, meaning there is cryptographic API misuse, or NO, meaning no cryptographic API misuse was detected, and explain your reasoning in one sentence:\n```python\n{code_snippet}\n```"

## Prompt 2
- "role": "developer",
- "content": "You are a cybersecurity specialist. You will be provided with a code snippet in python and your task is to analyze the code for cryptographic API misuses. Cryptographic API misuse is when developers utilize cryptographic libraries inappropriately due to not understanding proper usage or security rules, resulting in code vulnerable to attacks such as SSL/TLS man in the middle, predictability, ciphertext attack, brute force, and deserialization. Begin your response with either YES, meaning there is cryptographic API misuse, or NO, meaning no cryptographic API misuse was detected, and explain your reasoning in one sentence."
- "role": "user",
- "content": f"Please analyze this code snippet for cryptographic API misuse:\n```python\n{code_snippet}\n```"

## Prompt 3
- "role": "developer",
- "content": "You are a cybersecurity specialist. You will be provided with a code snippet in python and your task is to analyze the code for cryptographic API misuses. Cryptographic API misuse is when developers utilize cryptographic libraries inappropriately due to not understanding proper usage or security rules, resulting in code vulnerable to attacks such as SSL/TLS man in the middle, predictability, ciphertext attack, brute force, and deserialization. When analyzing, please look for instances of these cryptographic API misuses, along with any other misuses you also detect: Using a Wildcard to Avoid Verification, Creating a Custom String to Avoid Verification of Certificates, Using an Unverified Context to Avoid HTTPS Verification, Using HTTP Instead of HTTPS, Using Insecure Random Number Generation, Using a Static and Insecure Salt, Using an Insecure Mode, Using Less Than 1,000 Iterations, Using an, Insecure Block Cipher, Using an Insecure Asymmetric Cipher, Using an Insecure Hash, Not Verifying the Json Web Token (JWT), Using a Deprecated or Invalid Transport Layer Security (TLS) Version, Using an Insecure Protocol, Using an Insecure Extensible Markup Language (XML) Deserialization, Using an Insecure YAML Ain’t Markup Language (YAML) Deserialization, Using an Insecure Pickle Deserialization, Not Properly Escaping Regular Expressions (regex).Begin your response with either YES, meaning there is cryptographic API misuse, or NO, meaning no cryptographic API misuse was detected, and explain your reasoning in one sentence."
- "role": "user",
- "content": f"Please analyze this code snippet for cryptographic API misuse:\n```python\n{code_snippet}\n```"
