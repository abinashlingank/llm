import openai
from api_key import API_KEY

openai.api_key = API_KEY

user_name = "user"
user_input = input("Enter your Question:")
conversation = ''''''
prompt = user_name + ": " + user_input + "\n"
conversation += prompt

response = openai.Completion.create(engine='text-davinci-001', prompt=conversation, max_tokens=100)

conversation += response + "\n"

print(response)