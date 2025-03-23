import sqlite3
import mystring
from ephfile import ephfile

# codeQL is downloaded

# Path to your PyCryptoBench SQLite database file
db_path = "./data/PyCryptoBench.sqlite"

# Connect to the SQLite database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Fetch all test files from the database (assuming 'main' is the correct table name)
cursor.execute("SELECT * FROM main;")  # Adjust table name if needed
columns = [desc[0] for desc in cursor.description]  # Get column names
rows = cursor.fetchall()

# Iterate through each row
for row in rows:
    testfile = dict(zip(columns, row))  # Convert row to dictionary
    
    # Extract and decode the file content
    if 'Contents' in testfile:
        if testfile['InterProcedural'] == 1:
            testcontent = mystring.string.frombase64(testfile['Contents'].replace('b64:', ''))
        
            # Use ephfile to create a temporary file
            # with ephfile("testfile.py", testcontent) as eph:
            #     print(f"Temporary file created: {eph()}")
                # At this point, you can analyze or process the test file as needed

            with open("./test_files/testfile.py", "w", encoding="utf-8") as f:
                print(testfile['FileName'])
                f.write(testcontent)
                
            print("File 'testfile.py' has been created and saved.")
            break  # Exit after the first iteration

# Close database connection
conn.close()
