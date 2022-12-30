import sys
from db import get_connection
from entities import list

class ListModel():
    @classmethod
    def get_students(self):
        try:
            connection = get_connection()
            students = []
            with connection.cursor() as cursor:
                cursor.execute("""SELECT identify_card, name, direction, gender, phone_number, birth_date, career, genre, register_date, participation_date, age FROM students
                ORDER BY name ASC""")
                result = cursor.fetchall()
                for row in result:
                    student=list(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
                    students.append(student.to_json())
            connection.close()
            return students
        except Exception as ex:
            raise Exception(ex)


class FormModel():
    @classmethod
    def form(self, students):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO  students (identify_card, name, direction, gender, phone_number, birth_date, career, genre, register_date, participation_date, age)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s , %s, %s, %s)""".format(), (students.identify_card, students.name, students.direction, students.gender, students.phone_number, students.birth_date, students.career, students.genre, students.register_date, students.participation_date, students.age)) 
                affected_row = cursor.rowcount
                connection.commit()
            connection.close()
            
            return affected_row
        except Exception as ex:
            raise Exception(ex)
 