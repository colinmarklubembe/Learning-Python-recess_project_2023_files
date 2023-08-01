"""a) Show a context manager for file handling that automatically opens and closes a file."""


class FileHandler:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


# Usage of the context manager
with FileHandler('test.txt', 'w') as f:
    f.write('Hello World')

# Read from the file after writing
with FileHandler('test.txt', 'r') as f:
    content = f.read()

print(content)
# The file will be automatically closed after exiting the 'with' block


""" b) Shows a context manager for managing a database connection."""
import sqlite3


class DatabaseHandler:
    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()


# Usage example
with DatabaseHandler('test.db') as db:
    db.execute('CREATE TABLE IF NOT EXISTS users (name TEXT, age INTEGER)')
    db.execute('INSERT INTO users VALUES (?, ?)', ('John', 25))
    db.commit()

# Read from the database after writing
with DatabaseHandler('test.db') as db:
    cursor = db.execute('SELECT * FROM users')
    for row in cursor:
        print(row)
# The database will be automatically closed after exiting the 'with' block


"""c) Show a multithreading and multiprocessing  that allows us to run the function for different amounts of time."""

import time
import threading
import multiprocessing


def timer(seconds):
    time.sleep(seconds)
    print(f'Finished sleeping for {seconds} seconds')


# Multithreading
thread1 = threading.Thread(target=timer, args=(5,))
thread2 = threading.Thread(target=timer, args=(10,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

# Multiprocessing
process1 = multiprocessing.Process(target=timer, args=(5,))
process2 = multiprocessing.Process(target=timer, args=(10,))

process1.start()
process2.start()

process1.join()
process2.join()
