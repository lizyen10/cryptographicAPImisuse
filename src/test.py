import sqlite3
import mystring
from ephfile import ephfile
import os

# codeQL is downloaded
# Ensure the test_files directory exists
output_dir = "./test_files"
os.makedirs(output_dir, exist_ok=True)

# Path to your PyCryptoBench SQLite database file
db_path = "./data/PyCryptoBench.sqlite"

# Connect to the SQLite database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Fetch all test files from the database (assuming 'main' is the correct table name)
cursor.execute("SELECT * FROM main;")  # Adjust table name if needed
columns = [desc[0] for desc in cursor.description]  # Get column names
rows = cursor.fetchall()

file_count = 0  
max_files = 20  

# Iterate through each row
for row in rows:
    if file_count >= max_files:
        break  # Stop after writing 20 files

    testfile = dict(zip(columns, row))  # Convert row to dictionary
    
    # Extract and decode the file content
    if 'Contents' in testfile:
        if testfile['InterProcedural'] == 1:
            testcontent = mystring.string.frombase64(testfile['Contents'].replace('b64:', ''))
        
            # Use ephfile to create a temporary file
            # with ephfile("testfile.py", testcontent) as eph:
            #     print(f"Temporary file created: {eph()}")
                # At this point, you can analyze or process the test file as needed

            filename = f"testfile{file_count + 1}.py"
            file_path = os.path.join(output_dir, filename)

            with open(file_path, "w", encoding="utf-8") as f:
                print(testfile['FileName'])
                f.write(testcontent)

            file_count += 1

# Close database connection
conn.close()
