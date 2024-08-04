import openai

openai.api_key = "" #API KEY HERE


def chat_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4-1106-preview",
        messages=[{"role": "user", "content": prompt}]
    )
    # Correctly accessing the content of the response
    generated_text = response.choices[0].message.content.strip()
    return generated_text


def read_initial_input(file_path):
    """Reads the initial conversation input from a .txt file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        initial_input = file.read()
    return initial_input


if __name__ == "__main__":

    initial_file_path = '../output.txt'
    initial_input = read_initial_input(initial_file_path)
    
    # Print the initial response
    print("Bot:", chat_gpt(initial_input))
    print("\n")


    while True:
        user_input = input("You: ")
        print("\n")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break
        print("Bot:", chat_gpt(user_input))
        print("\n")

