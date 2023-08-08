import sqlite3



def getdata(script):
    with sqlite3.connect('school.bd') as con:
        with open(script, 'r') as f:
            
            cur = con.cursor()
            cur.execute(f.read())
            return cur.fetchall()


if __name__ == '__main__':
    print (getdata('query_10.sql'))