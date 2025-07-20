import sqlite3


conn = sqlite3.connect("students.db")
#connn = sqlite3.connect("courses.db")
cursor = conn.cursor()
#cursor2 = connn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMERY KEY AUTOINCRIMENT,
    name TEXT,
    age INTEGER,
    major TEXT
)''')


cursor.execute('''CREATE TABLE IF NOT EXISTS courses(
    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name TEXT
)
''')


cursor.execute('''CREATE TABLE IF NOT EXISTS student_courses(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_id INTEGER,
    student_id INTEGER,
    FOREIGN KEY(course_id) REFERENCES courses(id),
    FOREIGN KEY(student_id) REFERENCES students(id) 
)
''')

