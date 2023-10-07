import openai
import dotenv

config = dotenv.dotenv_values(".env")
openai.api_key = config['API_KEY']

prompt = "Say something funny"

response = openai.Completion.create(engine="gpt-3.5-turbo-instruct", prompt=prompt, max_tokens=6, temperature=0.8)

print(response)