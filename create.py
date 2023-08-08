import sqlite3 




def create_tab():
    with open('school.sql','r') as f:
        sql = f.read()

    with sqlite3.connect('school.bd') as con:
        cur = con.cursor()
        cur.executescript(sql)


if __name__=='__main__':
    create_tab()