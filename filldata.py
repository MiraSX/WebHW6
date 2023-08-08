from datetime import datetime, timedelta
from faker import Faker
import sqlite3
from random import randint, choice

fake = Faker('uk-UA')

NUM_STUDENTS = 60
NUM_TEACHERS = 5
NUM_GRADES = 20


subjects  = ('Foreign language', 'Math', 'History', 'Biology', 'Arts', 'Chemistry', 'Physics' , 'Sociology')

groups = ['Goit-13', 'Goit-12', 'Goit-11']


con = sqlite3.connect('school.bd')
cur = con.cursor()

def data_teachers():
    teachers = [fake.name() for _ in range(NUM_TEACHERS)]
    sql = 'INSERT INTO teachers(fullname) VALUES (?);'
    cur.executemany(sql, zip(teachers,))

def data_groups():
    sql = 'INSERT INTO groups(name) VALUES (?);'
    cur.executemany(sql, zip(groups,))

def data_students():
    students = [fake.name() for _ in range(NUM_STUDENTS)]
    list_group_id = [randint(1, len(groups)) for _ in range(NUM_STUDENTS)]
    sql = 'INSERT INTO students(fullname, group_id) VALUES (?, ?);'
    cur.executemany(sql, zip(students,list_group_id))

def data_subjects():
    list_teacher_id = [randint(1, NUM_TEACHERS) for _ in range(len(subjects))]
    sql = 'INSERT INTO subjects(name, teacher_id) VALUES (?, ?);'
    cur.executemany(sql, zip(subjects, list_teacher_id))

def data_rates():
    start_date = datetime.strptime('2022-09-01', '%Y-%m-%d')
    finish_date = datetime.strptime('2023-05-31', '%Y-%m-%d')
    sql = 'INSERT INTO rates(student_id, subject_id, rate, date_of) VALUES (?, ?, ?, ?)'

    def get_list_date (start_date, finish_date):
        result =[]
        current_day = start_date
        while current_day < finish_date:
            if current_day.isoweekday()<6:
                result.append(current_day)
            current_day+= timedelta(1)
        return result
    
    list_date = get_list_date(start_date, finish_date)

    grades = []
    for day in list_date:
        random_discipline = randint(1, len(subjects))
        random_students = [randint(1, NUM_STUDENTS) for _ in range(5)]
        for student in random_students:
            grades.append((random_discipline, student, randint(1, 12), day.date()))
    cur.executemany(sql, grades)

if __name__ == "__main__":
    data_groups()
    data_rates()
    data_teachers()
    data_students()
    data_subjects()
    con.commit()
    con.close()
    
