import openai
from concurrent.futures import ThreadPoolExecutor
import tiktoken

# Add your own OpenAI API key

openai.api_key = "sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

def load_text(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def save_to_file(responses, output_file):
    with open(output_file, 'w') as file:
        for response in responses:
            file.write(response + '\n')

# Change your OpenAI chat model accordingly

def call_openai_api(chunk):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "PASS IN ANY ARBITRARY SYSTEM VALUE TO GIVE THE AI AN IDENITY"},
            {"role": "user", "content": f"YOUR DATA TO PASS IN: {chunk}."},
        ],
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0]['message']['content'].strip()

def split_into_chunks(text, tokens=500):
    encoding = tiktoken.encoding_for_model('gpt-3.5-turbo')
    words = encoding.encode(text)
    chunks = []
    for i in range(0, len(words), tokens):
        chunks.append(' '.join(encoding.decode(words[i:i + tokens])))
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
    input_file = "test_input.txt"
    output_file = "output_og.txt"
    process_chunks(input_file, output_file)

# Can take up to a few minutes to run depending on the size of your data input
