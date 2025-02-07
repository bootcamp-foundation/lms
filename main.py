from db import DB
import settings


db = DB(
    host=settings.HOST,
    port=settings.PORT,
    user=settings.USER,
    password=settings.PASSWORD,
    db_name=settings.DB_NAME
)

db.insert_student('Vali', 20)

db.close()
