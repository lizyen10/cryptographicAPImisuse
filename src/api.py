from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
openai_api_key = os.getenv("MY_API_KEY")

client = OpenAI(api_key=openai_api_key)

def analyze_code_snippet(code_snippet: str):
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    max_completion_tokens=500,
    n=1,
    store= False, 
    temperature=0.5,
    messages=[
            {
                "role": "user",
                "content": f"Please analyze this code snippet for cryptographic API misuse. Begin your response with either YES, meaning there is cryptographic API misuse, or NO, meaning no cryptographic API misuse was detected, and explain your reasoning in one sentence:\n```python\n{code_snippet}\n```"
            }
        ]
    )

    return completion.choices[0].message.content

def main():

    base_path = './test_files'
    output_file = 'api_output.txt'

    true_positives = false_negatives = true_negatives = false_positives = 0

    with open(output_file, 'w') as out_file:
        for rule_num in range(1, 19): #should be 1, 19 for actual
            for vuln_status in ['HasVuln', 'NoVuln']:
                dir_path = os.path.join(base_path, f'Rule{rule_num}', vuln_status)
                if not os.path.exists(dir_path):
                    continue
                for filename in os.listdir(dir_path):
                    if filename.endswith('.py'):
                        file_path = os.path.join(dir_path, filename)
                        with open(file_path, 'r') as file:
                            #get rid of comments, dont want ai getting the metadata, only the code
                            lines = file.readlines()
                            code_lines = [
                                line for line in lines
                                if not line.lstrip().startswith('#')
                            ]
                            code_snippet = ''.join(code_lines)

                            # Analyze code
                            response = analyze_code_snippet(code_snippet).strip()

                            # Check actual (ground truth) and predicted (response)
                            has_vuln = (vuln_status == 'HasVuln')
                            no_vuln = (vuln_status == 'NoVuln')

                            predicted_vuln = response.startswith('YES')
                            no_predicted_vuln = response.startswith('NO')

                            if has_vuln and predicted_vuln:
                                # file is in HasVuln directory and response says YES
                                true_positives += 1
                                out_file.write(f'True Positive - Rule{rule_num}/{vuln_status}/{filename}:\n{response}\n\n')
                            elif has_vuln and no_predicted_vuln:
                                # file is in HasVuln directory and response says NO
                                false_negatives += 1
                                out_file.write(f'False Negative - Rule{rule_num}/{vuln_status}/{filename}:\n{response}\n\n')
                            elif no_vuln and no_predicted_vuln:
                                # file is in NoVuln directory and response says NO
                                true_negatives += 1
                                # did not write to file because there was no crypto misuse, and was correctly detected
                            elif no_vuln and predicted_vuln:
                                # file is in NoVuln directory and response says YES
                                false_positives += 1
                                out_file.write(f'False Positive - Rule{rule_num}/{vuln_status}/{filename}:\n{response}\n\n')

    # Print summary
    print("=== Evaluation Summary ===")
    print(f"True Positives: {true_positives}")
    print(f"False Negatives: {false_negatives}")
    print(f"True Negatives: {true_negatives}")
    print(f"False Positives: {false_positives}")
                        

if __name__ == "__main__":
    main()



