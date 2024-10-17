import json
import sqlite3
import yaml

class DBUtil:
    @staticmethod
    def parse_data_format(data, format_type='json'):
        """Parse data based on the specified format type."""
        if format_type == 'json':
            return json.loads(data)
        # Add more format types as needed
        raise ValueError(f"Unsupported format type: {format_type}")

    @staticmethod
    def connect_db(db_name):
        """Connect to a SQLite database."""
        try:
            connection = sqlite3.connect(db_name)
            return connection
        except sqlite3.Error as e:
            print(f"Database connection error: {e}")
            return None

    @staticmethod
    def export_db_structure(connection):
        """Export the database structure."""
        cursor = connection.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        structure = {}
        for table_name in tables:
            cursor.execute(f"PRAGMA table_info({table_name[0]});")
            columns = cursor.fetchall()
            structure[table_name[0]] = [column[1] for column in columns]
        return structure

    @staticmethod
    def show_db_structure_with_samples(connection):
        """Show the database structure and the first 3 records from each table."""
        cursor = connection.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        structure_with_samples = {}
        
        for table_name in tables:
            table_name_str = table_name[0]
            cursor.execute(f"PRAGMA table_info({table_name_str});")
            columns = cursor.fetchall()
            structure_with_samples[table_name_str] = {
                "columns": [column[1] for column in columns],
                "samples": []
            }
            
            # Fetch the first 3 records
            cursor.execute(f"SELECT * FROM {table_name_str} LIMIT 3;")
            samples = cursor.fetchall()
            structure_with_samples[table_name_str]["samples"] = samples
        
        return structure_with_samples

    @staticmethod
    def read_db_config(config_path='config/db_config.yaml'):
        """Read database configuration from a YAML file."""
        with open(config_path, 'r') as file:
            return yaml.safe_load(file)
