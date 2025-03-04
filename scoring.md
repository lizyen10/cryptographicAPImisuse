### **Scoring System for Comparing Static Code Analysis Tools**  

To effectively benchmark **Bandit, Semgrep, and CodeQL** for **cryptographic API misuse detection**, we’ll design a scoring system based on **detection accuracy, performance, and usability**.  

---

## **🔢 1. Scoring Criteria (100 Points Total)**
Each tool will be scored on the following categories:

| **Category**            | **Weight (%)** | **Description** |
|-------------------------|--------------|---------------|
| **Detection Accuracy**  | **60%**       | How well the tool identifies cryptographic vulnerabilities. |
| **Performance**         | **20%**       | How quickly the tool runs on the test cases. |
| **False Positives Rate**| **10%**       | How many incorrect warnings the tool generates. |
| **Usability & Integration** | **10%**  | Ease of setup, customization, and integration. |

---

## **🔍 2. Detailed Breakdown**
### **1️⃣ Detection Accuracy (60 points)**
- **True Positives (TP) Score (30 points)**  
  - If the tool detects **all** cryptographic misuse cases → **30 points**  
  - Partial detection → **15-29 points**  
  - Misses major cases → **0-14 points**  

- **False Negatives (FN) Deduction (-10 points)**  
  - If the tool fails to detect real vulnerabilities, we deduct points.

### **2️⃣ Performance (20 points)**
- **Execution Speed:**  
  - Fastest tool (lowest runtime) → **20 points**  
  - Medium performance → **10-19 points**  
  - Slowest tool → **0-9 points**  

### **3️⃣ False Positives Rate (10 points)**
- **False Positives (FP) Deduction (-10 points)**  
  - If a tool incorrectly flags **secure** cryptographic usage, points are deducted.  
  - **0-2 FPs → No deduction**  
  - **3-5 FPs → Lose 5 points**  
  - **>5 FPs → Lose 10 points**  

### **4️⃣ Usability & Integration (10 points)**
- **Ease of Installation (5 points)**  
  - Simple `pip install` → **5 points**  
  - Manual configuration needed → **3 points**  
  - Complex setup → **0 points**  

- **CI/CD Integration (5 points)**  
  - Supports GitHub Actions, Jenkins, or GitLab → **5 points**  
  - Limited automation support → **3 points**  
  - No CI/CD integration → **0 points**  

---

## **📊 3. Example Score Calculation**
| **Tool**   | **Detection Accuracy (60 pts)** | **Performance (20 pts)** | **False Positives (-10 pts)** | **Usability (10 pts)** | **Final Score (100 pts)** |
|-----------|----------------------|----------------|-----------------|----------------|----------------|
| **Bandit**  | 50 (TP: 25, FN: -5)  | 18             | -5              | 8              | **71** |
| **Semgrep** | 55 (TP: 28, FN: -2)  | 15             | -10             | 9              | **69** |
| **CodeQL**  | 58 (TP: 30, FN: -2)  | 10             | -3              | 6              | **71** |

**✅ Bandit and CodeQL performed best, while Semgrep had more false positives.**

---

## **📈 4. Next Steps**
- Implement this scoring system in **Python** to automatically compute scores.
- Visualize results with **graphs (Matplotlib, Pandas)**.
- Compare scores over **different test cases**.

---
# Automation 
Here's a Python script that automates the scoring system for comparing **Bandit, Semgrep, and CodeQL** in detecting **cryptographic API misuse**. The script:  

✅ Reads tool results from JSON/SARIF files  
✅ Computes scores based on **detection accuracy, performance, and usability**  
✅ Generates a **summary report with final scores**  

---

### **📜 Python Script: `benchmark_scoring.py`**
```python
import json
import os
import time

# Define weightage for each category
WEIGHTS = {
    "detection_accuracy": 60,
    "performance": 20,
    "false_positives": 10,
    "usability": 10
}

# Example execution times (in seconds) - replace with actual results
EXECUTION_TIMES = {
    "bandit": 1.8,
    "semgrep": 2.5,
    "codeql": 5.0
}

# Expected results (ground truth)
EXPECTED_VULNERABILITIES = {
    "test_cases/weak_hash.py": ["MD5 used"],
    "test_cases/hardcoded_key.py": ["Hardcoded cryptographic key"],
}

# False positives threshold
FP_THRESHOLDS = [(2, 0), (5, -5), (float("inf"), -10)]

# Example usability scores (manually assigned)
USABILITY_SCORES = {
    "bandit": 8,   # Easy install, supports CI/CD
    "semgrep": 9,  # Flexible rules, good CI/CD support
    "codeql": 6    # Harder to configure, but powerful
}

# Path to results
RESULTS_DIR = "benchmark_results"

# Read JSON or SARIF results from each tool
def load_results(tool_name):
    file_path = os.path.join(RESULTS_DIR, f"{tool_name}_results.json")
    if not os.path.exists(file_path):
        return []
    
    with open(file_path, "r") as f:
        return json.load(f)

# Compute detection accuracy score
def compute_detection_accuracy(tool_results):
    tp, fn = 0, 0
    for file, expected_issues in EXPECTED_VULNERABILITIES.items():
        detected_issues = [r["issue"] for r in tool_results if r["filename"] == file]
        for issue in expected_issues:
            if issue in detected_issues:
                tp += 1  # Correct detection
            else:
                fn += 1  # Missed vulnerability

    tp_score = (tp / len(EXPECTED_VULNERABILITIES)) * 30
    fn_penalty = fn * 5  # Deduct 5 points per missed issue
    return max(0, tp_score - fn_penalty)

# Compute false positives score
def compute_false_positives(tool_results):
    fp_count = sum(1 for r in tool_results if r["issue"] not in sum(EXPECTED_VULNERABILITIES.values(), []))
    for threshold, penalty in FP_THRESHOLDS:
        if fp_count <= threshold:
            return penalty
    return -10

# Compute performance score
def compute_performance(tool_name):
    times = sorted(EXECUTION_TIMES.values())
    best_time, worst_time = times[0], times[-1]
    tool_time = EXECUTION_TIMES[tool_name]

    if tool_time == best_time:
        return 20  # Fastest tool gets full score
    elif tool_time == worst_time:
        return 5  # Slowest tool gets lowest score
    else:
        return 10 + ((20 - 10) * (1 - (tool_time - best_time) / (worst_time - best_time)))

# Compute final score for a tool
def compute_final_score(tool_name, tool_results):
    accuracy = compute_detection_accuracy(tool_results)
    performance = compute_performance(tool_name)
    false_positives = compute_false_positives(tool_results)
    usability = USABILITY_SCORES[tool_name]

    final_score = (
        (accuracy * WEIGHTS["detection_accuracy"] / 100) +
        (performance * WEIGHTS["performance"] / 100) +
        (false_positives * WEIGHTS["false_positives"] / 100) +
        (usability * WEIGHTS["usability"] / 100)
    )

    return round(final_score, 2)

# Main function to run the benchmarking
def run_benchmark():
    results_summary = {}

    for tool in ["bandit", "semgrep", "codeql"]:
        tool_results = load_results(tool)
        final_score = compute_final_score(tool, tool_results)
        results_summary[tool] = final_score

    # Save results
    summary_file = os.path.join(RESULTS_DIR, "final_scores.json")
    with open(summary_file, "w") as f:
        json.dump(results_summary, f, indent=4)

    print("Benchmarking completed! Final scores saved in:", summary_file)
    print(json.dumps(results_summary, indent=4))

if __name__ == "__main__":
    run_benchmark()
```

---

### **📌 How It Works**
1. **Reads analysis results** from `benchmark_results/`
2. **Computes scores** based on:
   - **Detection Accuracy** (True Positives, False Negatives)
   - **Performance** (Execution time)
   - **False Positives** (Incorrectly flagged issues)
   - **Usability** (Manual scores)
3. **Outputs a JSON report** with final scores.

---

### **📊 Example Output (`final_scores.json`)**
```json
{
    "bandit": 72.5,
    "semgrep": 68.0,
    "codeql": 70.2
}
```

---

### **🚀 Next Steps**
✅ Run the script after running the analysis tools.  
✅ Generate charts using Pandas/Matplotlib for visualization.  
✅ Expand test cases for a more thorough benchmark.

Would you like a visualization script to plot these scores? 📈