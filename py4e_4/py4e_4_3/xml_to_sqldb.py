# to process xml and sqlite . 
import xml.etree.ElementTree as ET
import sqlite3

# makes a new file for data to be stored in .
conn = sqlite3.connect('trackdb.sqlite')
# handle of file to work in .
cur = conn.cursor()

# delete if database already has relevent tables from previous exicutions of the script.
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Genre;
''')
# makes all the tables etc relevent to the assignment.
cur.executescript('''

CREATE TABLE Artist (
  id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
  name    TEXT UNIQUE
);

CREATE TABLE Genre (
  id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
  name    TEXT UNIQUE
);

CREATE TABLE Album (
  id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
  artist_id  INTEGER,
  title   TEXT UNIQUE
);

CREATE TABLE Track (
  id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
  title TEXT  UNIQUE,
  album_id  INTEGER,
  genre_id  INTEGER,
  len INTEGER, rating INTEGER, count INTEGER
);

''')

# make a handle for xml file .
fname = input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'Library.xml'

# i don't understand it properly , it makes a function that grabs key value from xml that is placed in a unusual location ?.
# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>
def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text    
        if child.tag == 'key' and child.text == key :
            found = True
    return None

# process the xml file , extract the desired data , further narrow it to make it ready for sqlite operations.
stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')
print('Dict count:', len(all))
for entry in all:
    if ( lookup(entry, 'Track ID') is None ) : continue

    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    genre = lookup(entry, 'Genre')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')

    if name is None or artist is None or genre is None or album is None : 
        continue

    print(name, artist, album, count, rating, length)

# add the extracted xml data into sqlite tables and rows , becouse name or other fields are unqie ignore function is used to skip the process is same data is previosly recorded , also get id of the entry and save it for later use.
    cur.execute('''INSERT OR IGNORE INTO Artist (name) 
        VALUES ( ? )''', ( artist, ) )
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Genre (name) 
        VALUES ( ? )''', ( genre, ) )
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
    genre_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]

# replace works same as ignore except as name suggest it replaces the entry .
    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count) 
        VALUES ( ?, ?, ?, ?, ?, ? )''', 
        ( name, album_id, genre_id, length, rating, count ) )

# save the changes to the db file on drive .
    conn.commit()

