# project 16 is a AI powered virtual assistant 

from openai import OpenAI

key = "api key here"

messages = []

client = OpenAI(
    api_key=key,  # This is the default and can be omitted
)

def completion(message):
    global messages
    messages.append(
        {
            "role": "user",
            "content": message
        }
    )

    chat_completion = client.chat.completions.create( messages=messages,
                        model="gpt-5o"
                        )
    
    # print(chat_completion)
    message = {
        "role": "assistant",
        "content": chat_completion.choices[0].message.content
    }
    messages.append(message)
    print(f"sam: {message["content"]}")

#main function
if __name__ == "__main__":
    print(f"sam: Hi I am sam, How may I help you\n")
    while True:
        user_question = input()
        print(f"User: {user_question}")
        completion(user_question)