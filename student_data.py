import sqlite3

# check
print("successful")

# connect to a database
conn = sqlite3.connect('students.db')

# create a cursor object
c = conn.cursor()

# create a table called student_data
# c.execute(""" CREATE TABLE student_data(
#     first_name text,
#     last_name text,
#     email text
# )""")

# commit to database
conn.commit()

# check
print("successful")

# insert values into the table
students_list = [
                ("Joy", "Okum", "Joyokum@gmail.com"),
                ("Love", "Gabe", "loveyG@gmail.com"),
                ("Derek", "Sheperd", "Dereksh@gmail.com"),
                ("Meredith", "Grey", "Meredithgrey19@gmail.com")
                ]

# c.executemany("INSERT INTO student_data VALUES (?,?,?)", students_list)

conn.commit()

# check
print('commit successful')

# query the database
c.execute("SELECT * FROM peers_info")

item = c.fetchall()

# formating the table
# print("FIRST NAME" + "\t\t\tLAST NAME" + "\t\t\tEMAIL")
# print("..........." + "\t\t\t............." + "\t\t\t.........")

# for item in item:
#      print(item[0] + "\t\t\t\t" + item[1]+ "\t\t\t\t " + item[2])

# comit the connection
conn.commit()

# Alter table statement

# c.execute("ALTER TABLE student_data RENAME TO peers_info")
# conn.commit()

# check
print("successful")

# Alter column name
# c.execute("ALTER TABLE peers_info ADD COLUMN age")

# Update statement
c.execute(""" UPDATE peers_info SET age = '45'""")
conn.commit()

# query the database
c.execute("SELECT * FROM peers_info")

item = c.fetchall()

# formating the table
print("FIRST NAME" + "\t\tLAST NAME" + "\t\t\tEMAIL" + "\t\t\t\tAGE")
print("..........." + "\t\t........" + "\t\t\t......." + "\t\t\t\t\t......") 

for item in item:
     print(item[0] + "\t\t\t" + item[1]+ "\t\t\t " + item[2] + "\t\t" + "\t\t" + item[3])


# close the connection
conn.close()