import sqlite3

conn = sqlite3.connect("sample.db")

conn.execute("CREATE TABLE users(username text, password text)")

conn.execute("INSERT INTO users VALUES ('admin', 'admin@123')")

conn.commit()

conn.close()
