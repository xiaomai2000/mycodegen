import sqlite3

def create_sample_db(db_name='example.db'):
    """Create a sample SQLite database with three tables."""
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    # Create customer table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customer (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')

    # Create department table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS department (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')

    # Create sales_tran table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sales_tran (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER,
            department_id INTEGER,
            amount REAL NOT NULL,
            date TEXT NOT NULL,
            FOREIGN KEY (customer_id) REFERENCES customer (id),
            FOREIGN KEY (department_id) REFERENCES department (id)
        )
    ''')

    # Insert sample data into customer table
    cursor.execute("INSERT INTO customer (name, email) VALUES ('John Doe', 'john@example.com')")
    cursor.execute("INSERT INTO customer (name, email) VALUES ('Jane Smith', 'jane@example.com')")

    # Insert sample data into department table
    cursor.execute("INSERT INTO department (name) VALUES ('Electronics')")
    cursor.execute("INSERT INTO department (name) VALUES ('Clothing')")

    # Insert sample data into sales_tran table
    cursor.execute("INSERT INTO sales_tran (customer_id, department_id, amount, date) VALUES (1, 1, 199.99, '2023-01-01')")
    cursor.execute("INSERT INTO sales_tran (customer_id, department_id, amount, date) VALUES (2, 2, 49.99, '2023-01-02')")

    # Commit changes and close the connection
    connection.commit()
    connection.close()

if __name__ == "__main__":
    create_sample_db()
    print("Sample database 'example.db' created successfully.")
