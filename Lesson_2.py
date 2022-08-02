import sqlite3

# program to create SGA_1_3_learners database
conn = sqlite3.connect('SGA_1_3_learners.db')
c = conn.cursor()

# create a table called Learners
# c.execute("""CREATE TABLE Learners(
#                     First_name text,
#                     Last_name text,
#                     Email text
#             )""")

# print("program successfull")

# Add rows to input into the table called Learners database
Learners_list = [("Abubakar", "Adisa", "adisaabubakar@gmail.com"),
                 ("Adebisi", "Afolabi", "wasola.afolabi@yahoo.com"),
                 ("Adedoyin", "Abass", "doyinabass0@gmail.com"),
                 ("Awonaike", "Tawakalitu", "purpleduralumin@gmail.com"),
                 ("Babajide", "Adesugba", "jide_ade@hotmail.com"),
                 ("Bukola", "Ajayi", "bukolam.ajayi@gmail.com"),
                 ("Binta", "Umar", "ubinta63@yahoo.com"),
                 ("Christian", "Uzondu", "uzonduchristian2@gmail.com"),
                 ("Cynthia", "Awiya", "awiyac@yahoo.com"),
                 ("Deborah", "Olorunnishola", "deboraholuwatobi247@gmail.com"),
                 ("Eke", "Ihuoma", "ihuomaeke28@gmail.com"),
                 ("Esther", "Akpanowo", "estherakpanowo@gmail.com"),
                 ("Eniola", "Osadare ", "dorcasosadare@gmail.com"),
                 ("Etariemi", "Louis", "etariemilouis@gmail.com"),
                 ("Faith", "Amure", "amuretalodabif@gmail.com"),
                 ("Ganiyat", "Shittu", "ganiyatas@gmail.com"),
                 ("Gideon", "Uko", "ukogideon13@gmail.com"),
                 ("Idowu", "Adesanya", "idsworld22@yahoo.com"),
                 ("Joyce", "Ezeonwu", "joyceokore@gmail.com"),
                 ("Kehinde", "Orolade", "kehindeorolade@gmail.com"),
                 ("Kafayat", "Ibrahim", "kafayatadenike10@gmail.com"),
                 ("Lawrence", "Aneshimokha", "anelawrence1@gmail.com"),
                 ("Mariam", "Adeoti", "adetutuadebola28@gmail.com"),
                 ("Ogechi", "Njemanze", "ogenjemz@gmail.com"),
                 ("Omowunmi", "Awonirana", "mowunmi11@gmail.com"),
                 ("Placidus", "Ali", "Placidusali@gmail.com"),
                 ("Praise", "Emmanuel", "praiseemmanuel9ic@gmail.com"),
                 ("Prince", "Ekeocha", "prince.ekeocha@gmail.com"),
                 ("Rasheedat", "Sikiru", "rasheedatsikiru@gmail.com"),
                 ("Ramotallah", "Jubril", "jubrilramotallah03@gmail.com"),
                 ("Sheriiff", "Azeez", "SheriffOlaitan71@gmail.com"),
                 ("Stephen", "Ogungbile", "stephenfunso@gmail.com"),
                 ("Temitope", "Bamidele", "bamideletemitope42@gmail.com"),
                 ("Theresa", "Karamor", "teriekarie@gmail.com"),
                 ("Tina", "Uyateide", "tinauyats@gmail.com"),
                 ("Victoria", "Chukwuno", "chukwunovictoria@gmail.com")
]

# Add the multiple rows into the SGA_1_3_learners table
c.executemany('INSERT INTO Learners VALUES(?, ?, ?)', Learners_list)

c.execute("SELECT * FROM learners")

rows = c.fetchall()

# formating the table
print("first_name" + "\t" + "last_name"+ "\t\t email \n"f"{'.' * 100}")

for row in rows:
    first_name, last_name, email = row
    print(f"{first_name:16}{last_name:8}\t\t{email}")

print ("we have inserted", c.rowcount, 'records to the table')


# commit the changes to db
conn.commit()

conn.close()

