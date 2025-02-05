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
cursor.execute("SELECT * FROM staff;")

employees = cursor.fetchall()
for employee in employees:
    print(employee[0], employee[1], employee[2])

