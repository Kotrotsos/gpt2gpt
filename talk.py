import openai
import os
from collections import deque

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_gpt3_response(prompt, model="text-davinci-003"):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

def main():
    initial_message = "Hi there, I am Bob, it’s nice to finally meet you. How are you?"
    print(f"Bob: {initial_message}")

    conversation_history = deque(maxlen=10)
    conversation_history.append(initial_message)

    while True:
        # Instance 1 (Alice) response
        alice_prompt = "\n".join(conversation_history) + "\nAlice:"
        alice_response = get_gpt3_response(alice_prompt)
        print(f"Alice: {alice_response}")
        conversation_history.append(f"Alice: {alice_response}")

        # Instance 2 (Bob) response
        bob_prompt = "\n".join(conversation_history) + "\nBob:"
        bob_response = get_gpt3_response(bob_prompt)
        print(f"Bob: {bob_response}")
        conversation_history.append(f"Bob: {bob_response}")

if __name__ == "__main__":
    main()
