import sqlite3
class DataStorage:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS rules (
                id INTEGER PRIMARY KEY,
                rule_string TEXT NOT NULL
            );
        """)
        self.conn.commit()
    def insert_rule(self, rule_string):
        self.cursor.execute("INSERT INTO rules (rule_string) VALUES (?)", (rule_string,))
        self.conn.commit()
    def get_rules(self):
        self.cursor.execute("SELECT * FROM rules")
        return self.cursor.fetchall()
