import mysql.connector


class DB:

    def __init__(self, host: str, port: str, user: str, password: str, db_name: str):
        self.__connection = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password
        )
        if self.is_connected():
            self.__cursor = self.__connection.cursor()

            self.__cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
            self.__cursor.execute(f"USE {db_name}")

            self.__start()
        else:
            raise mysql.connector.Error("Connection Error")

    def __start(self):
        self.__create_student_table()
        self.__create_course_table()

    def __create_student_table(self):
        self.__cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(64),
                age INT
            );
        """)
        self.__commit()

    def insert_student(self, name: str, age: int):
        self.__cursor.execute("""
            INSERT INTO students (name, age)
            VALUES (%s, %s)
        """,
        (name, age)
        )
        self.__commit()

    def get_studetns(self) -> list[tuple]:
        self.__cursor.execute("""
            SELECT * FROM students
        """)
        return self.__cursor.fetchall()

    def __create_course_table(self):
        pass

    def __commit(self):
        self.__connection.commit()

    def is_connected(self) -> bool:
        return self.__connection.is_connected()

    def close(self):
        self.__cursor.close()
        self.__connection.close()

