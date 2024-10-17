import os
import logging
import yaml
from log_config import setup_logging
from util.db_util import DBUtil
from util.llm_util import LLMUtil


# Setup logging
setup_logging()
logger = logging.getLogger('my_logger')

# Load OpenAI configuration
def load_openai_config(config_path='config/openai_config.yaml'):
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)

openai_config = load_openai_config()
logger.info("OpenAI configuration loaded successfully.")

# Accessing the endpoint
openai_endpoint = openai_config['openai']['endpoint']
logger.info(f"OpenAI endpoint: {openai_endpoint}")

# Example usage of DBUtil class
data = '{"name": "John", "age": 30}'
parsed_data = DBUtil.parse_data_format(data)
print(parsed_data)

# Load database configuration
db_config = DBUtil.read_db_config()
db_name = db_config['database']['db_name']
logger.info(f"Database name: {db_name}")

db_connection = DBUtil.connect_db(db_name)
if db_connection:
    db_structure_with_samples = DBUtil.show_db_structure_with_samples(db_connection)
    print(db_structure_with_samples)  # Display the structure and samples
    db_connection.close()

# Example usage of LLMUtil class
context = LLMUtil.format_context()
user_question = "Write a program to select all the sales transaction records from database whose name is 'John'"
formatted_prompt = LLMUtil.format_prompt(context, user_question)

# Simulated history of messages
history = [
    "User: You are a SAP ABAP expert who has rich experience in ABAP programming, you are also a helpful assistant. You will be given a database structure and sample data, and a user question, you need to write a SQL query to answer the user question. You should respond with program codes directly because your response will be directly executed in the SAP system.",
    "Assistant: OK. I will write a SQL query to answer the user question, and the program will be executed in the SAP system."
]

# Call the LLM API with the prompt and history
response = LLMUtil.call_llm_api(formatted_prompt, history)
print(response)

# Save the response to pgm_out.txt in the pgmout folder
output_file_path = os.path.join('pgmout', 'pgm_out.txt')
with open(output_file_path, 'w') as output_file:
    output_file.write(response)

logger.info(f"Response saved to {output_file_path}.")

