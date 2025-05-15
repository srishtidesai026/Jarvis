import csv
import sqlite3
conn = sqlite3.connect("mai.db")
cursor = conn.cursor()

# query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
# cursor.execute(query)

# query = "INSERT INTO sys_command VALUES(null, 'code blocks', 'C:\\Users\\Srishti P Desai\\OneDrive\Desktop\\CodeBlocks.lnk')"
# cursor.execute(query)

# query = "INSERT INTO sys_command VALUES(null, 'vs code', 'C:\\Users\\Srishti P Desai\\OneDrive\\Desktop\\Visual Studio Code.lnk')"
# cursor.execute(query)

# query = "INSERT INTO sys_command VALUES(null, 'sql', 'C:\\Users\\Srishti P Desai\\OneDrive\\Desktop\\MySQL 8.0 Command Line Client.lnk')"
# cursor.execute(query)

# query = "INSERT INTO sys_command VALUES(null, 'ms edge', 'C:\\Users\\Public\\Desktop\\Microsoft Edge.lnk')"
# cursor.execute(query)
# # conn.commit()

# query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES(null, 'netflix', 'https://www.netflix.com/browse')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES(null, 'udemy', 'https://support.udemy.com/hc/en-us?')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES(null, 'chatgpt', 'https://chatgpt.com/?ref=dotcom')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES(null, 'youtube', 'https://www.youtube.com/')"
# cursor.execute(query)


# query = "DELETE FROM web_command WHERE id=5"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES(null, 'chatgpt', 'https://chatgpt.com/?ref=dotcom')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES(null, 'linkedin', 'https://www.linkedin.com/feed/')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES(null, 'google', 'https://www.google.co.in/')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES(null, 'leetcode', 'https://leetcode.com/')"
# cursor.execute(query)

# query = "DELETE FROM web_command WHERE id=8"
# cursor.execute(query)

query = "INSERT INTO web_command VALUES(null, 'code', 'https://leetcode.com/')"
cursor.execute(query)

query = "CREATE TABLE IF NOT EXISTS contacts(id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(300))"
cursor.execute(query) 


desired_columns_indices = [0, 18]

# read the contacts and load it into sql database
with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        # print(f"Row data: {row}")  
        # print(f"Desired columns: {desired_columns_indices}")  
        # print(f"Row length: {len(row)}") 
        selected_data = [row[i] for i in desired_columns_indices]
        cursor.execute(''' INSERT INTO contacts (id, 'name', 'mobile_no') VALUES (null, ?, ?);''', tuple(selected_data))

conn.commit()
conn.close()





