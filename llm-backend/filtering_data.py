import openai
from openai import OpenAI

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key="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",
)

def chat_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[
            {"role": "user", "content": prompt}]
    )
    generated_text = response.choices[0].message.content.strip()
    return generated_text

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break
        response = chat_gpt(user_input)
        print("\n")
        print("Bot:", response)
