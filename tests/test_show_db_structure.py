import sys
import os
import pytest
from util.db_util import DBUtil  # Updated import

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_show_db_structure_with_samples():
    """Test to show the structure of the example.db database."""
    db_name = 'example.db'
    
    # Connect to the example.db database
    db_connection = DBUtil.connect_db(db_name)  # Updated usage
    assert db_connection is not None, "Failed to connect to the database."

    # Use the DBUtil method to get the structure and samples
    structure_with_samples = DBUtil.show_db_structure_with_samples(db_connection)  # Updated usage
    
    # Print the structure and samples for verification
    print(structure_with_samples)

    # Close the database connection
    db_connection.close()

if __name__ == "__main__":
    pytest.main()
