import openai
from api_key import API_KEY

# Set your OpenAI API key
openai.api_key = API_KEY

# Define the user's name
user_name = "user"

# Initialize the conversation with an empty string
conversation = ''

# Start a loop to have a back-and-forth conversation
while True:
    # Get user input
    user_input = input(f"{user_name}: ")
    
    # Append user's message to the conversation
    conversation += f"{user_name}: {user_input}\n"

    # Generate a response from OpenAI
    response = openai.Completion.create(
        engine='text-davinci-001',
        prompt=conversation,
        max_tokens=50  # Adjust the max_tokens as needed for the desired response length
    )

    # Extract the AI's reply from the response
    response_str = response.choices[0].text.strip()

    # Append AI's reply to the conversation
    conversation += f"AI: {response_str}\n"

    # Print the AI's reply
    print(f"AI: {response_str}")







# Completion.create (Text Generation):

# engine (str): Specifies the language model (engine) to use, such as "text-davinci-001" or "text-davinci-002".
# prompt (str): The input text or prompt that you want the model to continue or generate from.
# max_tokens (int): Limits the length of the generated output to a certain number of tokens.
# temperature (float): Controls the randomness of the output. Higher values make the output more random, while lower values make it more deterministic.
# stop (str or list of str): A list of tokens at which to stop generating text.
# temperature (float): Controls the randomness of the output. Higher values make the output more random, while lower values make it more deterministic.
# top_p (float): Filters the choices based on the cumulative probability of the next token. A higher value (e.g., 0.8) will result in more conservative output.
# Translation.create (Language Translation):

# engine (str): Specifies the language model (engine) to use, such as "text-davinci-001" or "text-davinci-002".
# text (str): The text you want to translate.
# target_language (str): The language code of the target language for translation.
# source_language (str, optional): The language code of the source language if not auto-detected.
# Summarization.create (Text Summarization):

# engine (str): Specifies the language model (engine) to use, such as "text-davinci-001" or "text-davinci-002".
# text (str): The text you want to summarize.
# max_tokens (int): Limits the length of the generated summary to a certain number of tokens.
# Classification.create (Text Classification):

# model (str): Specifies the text classification model to use.
# examples (list of dict): Training examples for the classification task, including "label" and "text" for each example.
# Answer.create (Question Answering):

# model (str): Specifies the question-answering model to use.
# question (str): The question you want to answer.
# context (str): The context or passage from which to extract the answer.
# Engine.list (List Available Engines):

# No additional arguments are required. This function lists available engines that you can use for various language tasks.
# FineTunes.create (Fine-tuning Models):

# model (str): The base model to use for fine-tuning.
# train_file (str): The training data in the form of a file ID or URL.
# name (str): A custom name for the fine-tuned model.
# Additional arguments for fine-tuning parameters, such as epochs, batch_size, and more.