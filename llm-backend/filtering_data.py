import openai

openai.api_key = "" #API KEY HERE


def chat_gpt(prompt, chat_history=None):

    if chat_history is None:
        chat_history = []

  
    messages = chat_history + [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model="gpt-4-1106-preview",  
        messages=messages
    )
    generated_text = response.choices[0].message['content'].strip()
 
    chat_history.append({"role": "user", "content": prompt})
    chat_history.append({"role": "assistant", "content": generated_text})

    return generated_text, chat_history


def read_initial_input(file_path):
    """Reads the initial conversation input from a .txt file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        initial_input = file.read()
    return initial_input


if __name__ == "__main__":

    initial_file_path = '../output.txt'
    try:
        with open(initial_file_path, 'r', encoding='utf-8') as file:
            initial_input = file.read().strip()
    except FileNotFoundError:
        print(f"Error: The file {initial_file_path} was not found.")
        exit()

   
    chat_history = []
    response, chat_history = chat_gpt(initial_input, chat_history)
    
    print("Bot:", response)
    
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Exiting the chat.")
            print("\n")
            break
        
        response, chat_history = chat_gpt(user_input, chat_history)
        print("Bot:", response)
        print("\n")



