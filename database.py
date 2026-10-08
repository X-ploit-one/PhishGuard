import sqlite3


def create_database():

    connection = sqlite3.connect("phishguard.db")

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS detection_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email_text TEXT,
            prediction TEXT,
            spam_probability REAL,
            risk_score INTEGER,
            risk_level TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()


create_database()