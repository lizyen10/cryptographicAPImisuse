Precision, Recall, and F-score are common metrics used to evaluate the performance of classification models, including in security vulnerability detection. Here’s a breakdown of what they mean:

---

### **1. Precision (Positive Predictive Value)**
**Formula:**  
\[
\text{Precision} = \frac{\text{True Positives}}{\text{True Positives} + \text{False Positives}}
\]

- Measures **how many of the detected cryptographic misuses are actually correct**.
- A high precision means fewer **false positives** (incorrectly flagged secure code as insecure).
- Important when false positives are costly (e.g., unnecessary fixes in secure code).

✔ **Example:**  
If an LLM detects 10 vulnerabilities, but only 7 are correct, then:
\[
\text{Precision} = \frac{7}{7+3} = 0.7 \text{ (or 70%)}
\]

---

### **2. Recall (Sensitivity or True Positive Rate)**
**Formula:**  
\[
\text{Recall} = \frac{\text{True Positives}}{\text{True Positives} + \text{False Negatives}}
\]

- Measures **how many actual cryptographic misuses were detected out of all existing misuses**.
- A high recall means fewer **false negatives** (missed vulnerabilities).
- Important when **missing vulnerabilities is critical** (e.g., security analysis).

✔ **Example:**  
If there were 15 total cryptographic misuses in the test cases and the LLM correctly detected 7:
\[
\text{Recall} = \frac{7}{7+8} = 0.466 \text{ (or 46.6%)}
\]

---

### **3. F1-Score (Harmonic Mean of Precision & Recall)**
**Formula:**  
\[
F_1 = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}
\]

- **Balances precision and recall** to provide an overall measure of accuracy.
- **High F1-score means the model is good at both detecting and correctly identifying vulnerabilities**.
- Useful when both **false positives and false negatives are problematic**.

✔ **Example:**  
If **Precision = 0.7** and **Recall = 0.466**, then:
\[
F_1 = 2 \times \frac{0.7 \times 0.466}{0.7 + 0.466} = 2 \times \frac{0.326}{1.166} = 0.56 \text{ (or 56%)}
\]

---

### **Which Metric is More Important?**
- If **false positives** (incorrect vulnerability detections) are bad → **Precision is more important**.
- If **false negatives** (missed vulnerabilities) are bad → **Recall is more important**.
- If **both false positives and false negatives matter** → **F1-score is the best metric**.

---

Would you like help setting up a script to calculate these metrics for your LLM evaluation? 🚀