import sqlite3
import mystring
import os

# Base output directory
base_output_dir = "./test_files"

# Create Rule1 to Rule18 subdirectories with HasVuln and NoVuln
for rule_number in range(0, 19):
    for vuln_label in ["HasVuln", "NoVuln"]:
        dir_path = os.path.join(base_output_dir, f"Rule{rule_number}", vuln_label)
        os.makedirs(dir_path, exist_ok=True)

# Path to your PyCryptoBench SQLite database file
db_path = "./data/PyCryptoBench.sqlite"

# Connect to the SQLite database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Fetch all test files from the database (adjust table name if needed)
cursor.execute("SELECT * FROM main;")
columns = [desc[0] for desc in cursor.description]
rows = cursor.fetchall()

print("Columns:", columns)

file_count = 0

# Iterate through each row
for row in rows:
    testfile = dict(zip(columns, row))

    if 'Contents' in testfile and testfile['InterProcedural'] == 1:
        testcontent = mystring.string.frombase64(testfile['Contents'].replace('b64:', ''))

        rule_number = testfile.get('Rule')
        has_vuln = testfile.get('HasVuln')

        if rule_number is None or has_vuln is None:
            continue  # Skip if required fields are missing

        vuln_folder = "HasVuln" if has_vuln == 1 else "NoVuln"
        rule_dir = os.path.join(base_output_dir, f"Rule{rule_number}", vuln_folder)
        os.makedirs(rule_dir, exist_ok=True)

        filename = f"testfile{file_count + 1}.py"
        file_path = os.path.join(rule_dir, filename)

        # Create metadata comments
        metadata_comments = "# Test Case Metadata\n"
        for col_name, value in testfile.items():
            if col_name != 'Contents':
                metadata_comments += f"# {col_name}: {value}\n"

        with open(file_path, "w", encoding="utf-8") as f:
            print(f"Saving: {testfile['FileName']} to {file_path}")
            f.write(metadata_comments + "\n" + testcontent)

        file_count += 1

print(f"Total files saved: {file_count}")

# Close database connection
conn.close()
