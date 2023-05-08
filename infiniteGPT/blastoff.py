import openai
import os
from concurrent.futures import ThreadPoolExecutor

# Add your own OpenAI API key
openai.api_key = os.environ.get("OPENAI_API_KEY")

if not openai.api_key:
    raise ValueError("The OPENAI_API_KEY environment variable is not set.")

def load_text(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def save_to_file(responses, output_file):
    with open(output_file, 'w') as file:
        for response in responses:
            file.write(response + '\n')

def call_openai_api(chunk):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Please summarize the following: {chunk}."},
            ],
            max_tokens=1750,
            n=1,
            stop=None,
            temperature=0.5,
        )
        return response.choices[0]['message']['content'].strip()
    except Exception as e:
        print(f"Error processing chunk: {e}")
        return ""

def split_into_chunks(text, tokens=1500):
    words = text.split()
    chunks = [' '.join(words[i:i + tokens]) for i in range(0, len(words), tokens)]
    return chunks

def process_chunks(input_file, output_file):
    text = load_text(input_file)
    chunks = split_into_chunks(text)
    
    # Processes chunks in parallel
    with ThreadPoolExecutor() as executor:
        responses = list(executor.map(call_openai_api, chunks))

    save_to_file(responses, output_file)

# Specify your input and output files
if __name__ == "__main__":
    input_file = "your_input_here.txt"
    output_file = "your_output_here.txt"
    process_chunks(input_file, output_file)

