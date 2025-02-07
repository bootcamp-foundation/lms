from pprint import pprint
from db import DB
import settings


db = DB(
    host=settings.HOST,
    port=settings.PORT,
    user=settings.USER,
    password=settings.PASSWORD,
    db_name=settings.DB_NAME
)


students = db.get_studetns()

for student in students:
    print(student)
    

db.close()
