import os

class LLMUtil:
    @staticmethod
    def format_prompt(context, user_question):
        """Format the prompt for the LLM."""
        return f"{context}\nUser: {user_question}\nAssistant:"

    @staticmethod
    def format_context(input_folder='input'):
        """Read and format the contents of text files in the input folder."""
        context = ""
        for filename in os.listdir(input_folder):
            if filename.endswith('.txt'):
                file_path = os.path.join(input_folder, filename)
                with open(file_path, 'r') as file:
                    content = file.read()
                    context += f"{content}\n"  # Add content from each file
        return context.strip()  # Remove trailing newline

    @staticmethod
    def call_llm_api(prompt, history):
        """Simulate a call to the LLM API with the given prompt and history."""
        # Here you would typically make an API call to the LLM service.
        # For demonstration purposes, we'll just return a formatted string.
        formatted_history = "\n".join(history)
        return f"History:\n{formatted_history}\nPrompt:\n{prompt}\nResponse: [Simulated LLM Response]"
    
    