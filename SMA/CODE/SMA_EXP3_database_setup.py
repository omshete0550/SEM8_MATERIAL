import pymysql
import csv
from datetime import datetime 

DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "Admin@99878"
DB_NAME = "YCOMBINATOR"

connection = pymysql.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME
)

cursor = connection.cursor()

csv_file = "preprocessed_comments.csv" 

with open(csv_file, mode="r", encoding="utf-8") as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  

    for row in csv_reader:
        id, link, author, comment_name, date, time, _ = row
        
        try:
            date = datetime.strptime(date, "%d-%m-%Y").strftime("%Y-%m-%d")
        except ValueError:
            print(f"Skipping row with invalid date: {date}")
            continue 
        

        insert_query = """
        INSERT INTO comments (id, link, author, comment_name, date, time)
        VALUES (%s, %s, %s, %s, %s, %s);
        """
        cursor.execute(insert_query, (id, link, author, comment_name, date, time))

connection.commit()
cursor.close()
connection.close()

print("Data inserted successfully!")