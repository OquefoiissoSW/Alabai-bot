import sqlite3

# def create_table():
    # conn = sqlite3.connect("Students.db", check_same_thread=False)
    # cursor = conn.cursor()
    #
    # create_table_query = """
    #     CREATE TABLE IF NOT EXISTS attendance (
    #     id INTEGER PRIMARY KEY,
    #     surname VARCHAR(255) NOT NULL,
    #     subject VARCHAR(255) NOT NULL,
    #     attendance INTEGER,
    #     marks INTEGER
    #     )
    #     """
    #
    # cursor.execute(create_table_query)
    # cursor.execute("INSERT INTO attendance (surname, subject, attendance, marks) VALUES (?, ?, ?, ?)", ('Литвинов', 'Математика', 60, 45))
    # cursor.execute("INSERT INTO attendance (surname, subject, attendance, marks) VALUES (?, ?, ?, ?)", ('Литвинов', 'Математика', 60, 45))
    # cursor.execute("INSERT INTO attendance (surname, subject, attendance, marks) VALUES (?, ?, ?, ?)", ('Литвинов', 'Математика', 60, 45))
    # cursor.execute("INSERT INTO attendance (surname, subject, attendance, marks) VALUES (?, ?, ?, ?)", ('Литвинов', 'Математика', 60, 45))
    # cursor.execute("INSERT INTO attendance (surname, subject, attendance, marks) VALUES (?, ?, ?, ?)", ('Литвинов', 'Математика', 60, 45))