import os

# test file for api.py, checks parsing and evaluation of files is correct 

base_path = './test_files'
output_file = 'api_output.txt'

true_positives = false_negatives = true_negatives = false_positives = 0

with open(output_file, 'w') as out_file:
    for rule_num in range(0, 1): #should be 1, 19 for actual
        for vuln_status in ['HasVuln', 'NoVuln']:
            dir_path = os.path.join(base_path, f'Rule{rule_num}', vuln_status)
            if not os.path.exists(dir_path):
                continue
            for filename in os.listdir(dir_path):
                if filename.endswith('.py'):
                    file_path = os.path.join(dir_path, filename)
                    with open(file_path, 'r') as file:
                        # get rid of comments, dont want ai getting the metadata, only the code
                        lines = file.readlines()
                        code_lines = [
                            line for line in lines
                            if not line.lstrip().startswith('#')
                        ]
                        code_snippet = ''.join(code_lines)

                        # Analyze code
                        #response = analyze_code_snippet(code_snippet).strip()
                        response = "NO"

                        # Check actual and predicted 
                        has_vuln = (vuln_status == 'HasVuln')
                        no_vuln = (vuln_status == 'NoVuln')

                        predicted_vuln = response.startswith('YES')
                        no_predicted_vuln = response.startswith('NO')

                        if has_vuln and predicted_vuln:
                            # file is in HasVuln directory and response says YES
                            true_positives += 1
                        elif has_vuln and no_predicted_vuln:
                            # file is in HasVuln directory and response says NO
                            false_negatives += 1
                            out_file.write(f'False Negative - Rule{rule_num}/{vuln_status}/{filename}:\n{response}\n\n')
                        elif no_vuln and no_predicted_vuln:
                            # file is in NoVuln directory and response says NO
                            true_negatives += 1
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
