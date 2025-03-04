# Popular Static Code Analysis Tools

## 1. Bandit (Python)

### How it works:
- Bandit analyzes Python code for security vulnerabilities, including cryptographic misuse.
- Uses AST (Abstract Syntax Tree) parsing to inspect source code.
- Comes with built-in checks for weak cryptography (e.g., using MD5, DES, or `random` instead of `secrets`).

### Installation & Usage:
```sh
pip install bandit
bandit -r your_project/
```

---

## 2. Semgrep (Multi-language)

### How it works:
- Pattern-based static analysis tool that supports custom rules.
- Can detect insecure cryptographic patterns using pre-built rules.
- Lightweight and fast, works by matching source code structures rather than running the code.

### Installation & Usage:
```sh
pip install semgrep
semgrep --config=p/r2c-security .
```

### Example rule for weak crypto detection:
```yaml
rules:
  - id: weak-md5-hash
    patterns:
      - pattern: hashlib.md5(...)
    message: "MD5 is a weak hash function. Use SHA-256 instead."
    languages: [python]
    severity: ERROR
```

---

## 3. CodeQL (Multi-language)

### How it works:
- A query-based analysis tool that scans source code using a database representation.
- Used by GitHub Advanced Security to find vulnerabilities in open-source projects.

### Installation & Usage:
```sh
codeql database create mydb --language=python --source-root=your_project/
codeql analyze mydb codeql/python-queries --format=sarif
```

---

## 4. SonarQube (Multi-language)

### How it works:
- Performs deep static analysis with security rules for cryptography, hardcoded secrets, etc.
- Provides a web dashboard for vulnerability tracking.

### Installation & Usage:
```sh
sonar-scanner -Dsonar.projectKey=your_project -Dsonar.sources=. -Dsonar.host.url=http://localhost:9000
```

---

## 5. Flawfinder (C/C++)

### How it works:
- Scans C/C++ source code for known security flaws, including weak cryptographic functions.
- Uses a predefined database of insecure functions.

### Installation & Usage:
```sh
sudo apt install flawfinder
flawfinder your_project/
```

---

## How They Work (General Workflow)
1. **Code Parsing:** The tool reads and parses the source code.
2. **Pattern Matching:** Uses predefined rules or queries to identify insecure patterns.
3. **Abstract Syntax Tree (AST) Analysis:** Some tools analyze code structure beyond simple text matching.
4. **Data Flow & Control Flow Analysis:** Advanced tools track how data moves through the code to detect subtle security issues.
5. **Reporting:** The tool outputs findings, typically in JSON, SARIF, or a UI dashboard.

## Automation

How to automate running multiple static analysis tools (Bandit, Semgrep, and CodeQL) on a given project directory. The script will:  

1. **Run each tool** and collect results.  
2. **Save outputs** to JSON files.  
3. **Summarize findings** in a structured way.  

---

### **Requirements:**
Before running the script, install the necessary tools:

```bash
pip install bandit semgrep
# Install CodeQL manually: https://github.com/github/codeql-cli-binaries/releases
```

---

### **Automation Script**
This script takes a project directory as input and runs Bandit, Semgrep, and CodeQL:

```python
import subprocess
import json
import os

# Define paths and configurations
PROJECT_DIR = "./your_project"  # Change this to your target project directory
OUTPUT_DIR = "analysis_results"
CODEQL_DB = "codeql_db"

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

def run_bandit():
    """Run Bandit and save the results."""
    output_file = os.path.join(OUTPUT_DIR, "bandit_results.json")
    cmd = ["bandit", "-r", PROJECT_DIR, "-f", "json", "-o", output_file]
    subprocess.run(cmd, stdout=subprocess.DEVNULL)
    print(f"Bandit results saved to {output_file}")

def run_semgrep():
    """Run Semgrep with security rules and save the results."""
    output_file = os.path.join(OUTPUT_DIR, "semgrep_results.json")
    cmd = ["semgrep", "--config", "p/r2c-security", "--json", "-o", output_file, PROJECT_DIR]
    subprocess.run(cmd, stdout=subprocess.DEVNULL)
    print(f"Semgrep results saved to {output_file}")

def run_codeql():
    """Run CodeQL analysis and save results."""
    # Step 1: Create CodeQL database
    subprocess.run(["codeql", "database", "create", CODEQL_DB, "--language=python", "--source-root", PROJECT_DIR],
                   stdout=subprocess.DEVNULL)
    # Step 2: Run analysis
    output_file = os.path.join(OUTPUT_DIR, "codeql_results.sarif")
    cmd = ["codeql", "analyze", CODEQL_DB, "codeql/python-queries", "--format=sarif", "-o", output_file]
    subprocess.run(cmd, stdout=subprocess.DEVNULL)
    print(f"CodeQL results saved to {output_file}")

def summarize_results():
    """Summarize findings from Bandit and Semgrep."""
    summary = {"bandit": [], "semgrep": []}

    # Load Bandit results
    bandit_file = os.path.join(OUTPUT_DIR, "bandit_results.json")
    if os.path.exists(bandit_file):
        with open(bandit_file, "r") as f:
            data = json.load(f)
            summary["bandit"] = data.get("results", [])

    # Load Semgrep results
    semgrep_file = os.path.join(OUTPUT_DIR, "semgrep_results.json")
    if os.path.exists(semgrep_file):
        with open(semgrep_file, "r") as f:
            data = json.load(f)
            summary["semgrep"] = data.get("results", [])

    # Save summary
    summary_file = os.path.join(OUTPUT_DIR, "summary.json")
    with open(summary_file, "w") as f:
        json.dump(summary, f, indent=4)

    print(f"Summary saved to {summary_file}")

if __name__ == "__main__":
    print("Running static analysis tools...")
    run_bandit()
    run_semgrep()
    run_codeql()
    summarize_results()
    print("Analysis complete!")
```

---

### **How to Use:**
1. **Modify `PROJECT_DIR`** to point to your target source code directory.
2. **Run the script:**
   ```bash
   python benchmark_static_tools.py
   ```
3. The results will be stored in the `analysis_results/` folder.

---

### **Next Steps:**
- Add more static analysis tools (e.g., SonarQube, Flawfinder).
- Parse CodeQL results in SARIF format for better insights.
- Visualize findings using Python (e.g., Matplotlib, Pandas).

Yes! Let's integrate these static analysis tools into your benchmarking setup step by step.

---

## **Steps to Integrate Static Analysis into Your Benchmarking Tool**
We'll extend your benchmarking framework to:
1. **Run multiple static analysis tools** (Bandit, Semgrep, CodeQL).
2. **Collect and store results** in a structured format (JSON).
3. **Evaluate each tool's performance** in detecting cryptographic API misuse.
4. **Generate reports** for easy comparison.

---

## **Step 1: Define Benchmarking Criteria**
We will evaluate tools based on:
- **True Positives (TP):** Correctly detected cryptographic API misuse.
- **False Positives (FP):** Incorrectly flagged secure code.
- **False Negatives (FN):** Missed actual vulnerabilities.
- **Execution Time:** How fast the tool runs.

---

## **Step 2: Set Up Your Test Cases**
Create a `test_cases/` directory with Python scripts containing:
1. **Correct cryptographic usage**
2. **Common cryptographic mistakes** (e.g., weak ciphers, hardcoded keys)

Example (`test_cases/weak_hash.py`):
```python
import hashlib
password = "mypassword".encode()
hashed = hashlib.md5(password).hexdigest()  # Insecure: MD5 is weak
print(hashed)
```

Example (`test_cases/secure_hash.py`):
```python
import hashlib
import os
password = "mypassword".encode()
salt = os.urandom(16)
hashed = hashlib.pbkdf2_hmac('sha256', password, salt, 100000)  # Secure
print(hashed)
```

---

## **Step 3: Automate Running Static Analysis**
We'll create a `benchmark.py` script to:
- Run Bandit, Semgrep, and CodeQL.
- Store results in JSON.
- Compare performance.

```python
import subprocess
import json
import os
import time

# Directories
TEST_DIR = "test_cases"
OUTPUT_DIR = "benchmark_results"
CODEQL_DB = "codeql_db"

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

def run_bandit():
    """Run Bandit and save results."""
    output_file = os.path.join(OUTPUT_DIR, "bandit_results.json")
    start_time = time.time()
    cmd = ["bandit", "-r", TEST_DIR, "-f", "json", "-o", output_file]
    subprocess.run(cmd, stdout=subprocess.DEVNULL)
    end_time = time.time()
    print(f"Bandit completed in {end_time - start_time:.2f}s. Results saved to {output_file}")

def run_semgrep():
    """Run Semgrep and save results."""
    output_file = os.path.join(OUTPUT_DIR, "semgrep_results.json")
    start_time = time.time()
    cmd = ["semgrep", "--config", "p/r2c-security", "--json", "-o", output_file, TEST_DIR]
    subprocess.run(cmd, stdout=subprocess.DEVNULL)
    end_time = time.time()
    print(f"Semgrep completed in {end_time - start_time:.2f}s. Results saved to {output_file}")

def run_codeql():
    """Run CodeQL and save results."""
    # Step 1: Create CodeQL database
    subprocess.run(["codeql", "database", "create", CODEQL_DB, "--language=python", "--source-root", TEST_DIR],
                   stdout=subprocess.DEVNULL)
    # Step 2: Run analysis
    output_file = os.path.join(OUTPUT_DIR, "codeql_results.sarif")
    start_time = time.time()
    cmd = ["codeql", "analyze", CODEQL_DB, "codeql/python-queries", "--format=sarif", "-o", output_file]
    subprocess.run(cmd, stdout=subprocess.DEVNULL)
    end_time = time.time()
    print(f"CodeQL completed in {end_time - start_time:.2f}s. Results saved to {output_file}")

def parse_results():
    """Parse results and generate a summary."""
    summary = {"bandit": [], "semgrep": [], "codeql": []}

    # Load Bandit results
    bandit_file = os.path.join(OUTPUT_DIR, "bandit_results.json")
    if os.path.exists(bandit_file):
        with open(bandit_file, "r") as f:
            data = json.load(f)
            summary["bandit"] = [{"filename": r["filename"], "issue": r["issue_text"]} for r in data.get("results", [])]

    # Load Semgrep results
    semgrep_file = os.path.join(OUTPUT_DIR, "semgrep_results.json")
    if os.path.exists(semgrep_file):
        with open(semgrep_file, "r") as f:
            data = json.load(f)
            summary["semgrep"] = [{"filename": r["path"], "message": r["extra"]["message"]} for r in data.get("results", [])]

    # Save summary
    summary_file = os.path.join(OUTPUT_DIR, "summary.json")
    with open(summary_file, "w") as f:
        json.dump(summary, f, indent=4)

    print(f"Summary saved to {summary_file}")

if __name__ == "__main__":
    print("Running benchmarking for static analysis tools...")
    run_bandit()
    run_semgrep()
    run_codeql()
    parse_results()
    print("Benchmarking completed!")
```

---

## **Step 4: Run the Benchmark**
```bash
python benchmark.py
```
Results will be stored in `benchmark_results/summary.json`.

---

## **Step 5: Evaluate Performance**
Now, compare the tools based on:
1. **Detection Accuracy** – Which tools detected the most vulnerabilities?
2. **False Positives** – Did any tool report incorrect findings?
3. **Execution Speed** – Which tool runs the fastest?
