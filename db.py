import mysql.connector
import settings


connection = mysql.connector.connect(
    host=settings.host,
    port=settings.port,
    user=settings.user, 
    password=settings.password
)
cursor = connection.cursor()

cursor.execute("USE company_db;")

cursor.execute("""
    INSERT INTO staff (full_name, age, salary, contact)
    VALUE (%s, %s, %s, %s)
""", ('ali', 12, 1200.90, '123456'))
connection.commit()

cursor.execute("SELECT * FROM staff;")


employees = cursor.fetchall()
for employee in employees:
    print(employee)

cursor.close()
connection.close()

