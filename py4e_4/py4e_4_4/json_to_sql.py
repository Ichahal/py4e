# to process json and sqlite.
import json
import sqlite3

# make a new file to store data in , handle for file to work in .
conn = sqlite3.connect('roster_data.sqlite')
cur = conn.cursor()

# delete if database already has relevent tables from previous exicutions of the script.
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;
''')

# makes all the tables etc relevent to the assignment.
cur.executescript('''
CREATE TABLE User (
  id    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
  name  TEXT UNIQUE  
);

CREATE TABLE Course (
  id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
  title  TEXT UNIQUE  
);

CREATE TABLE Member (
user_id     INTEGER,
course_id   INTEGER,
role        INTEGER,
PRIMARY KEY (user_id, course_id)
);

''')

# make a handle for json file .
fname = input('Enter file name: ')
if len(fname) < 1 :
  fname = 'roster_data.json'

# process the json file and extract the desired data and narrow it down to excute sql.
str_data = open(fname).read()
json_data = json.loads(str_data)

for entry in json_data:

    name = entry[0]
    title = entry[1]
    roleincourse = entry[2]

    print((name, title, roleincourse))

    # excute sql and make database of processed json data.
    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES ( ? )''', ( name, ) )
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES ( ? )''', ( title, ) )
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES ( ?, ?, ? )''',
        ( user_id, course_id, roleincourse ) )

    conn.commit()

