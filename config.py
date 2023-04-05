from dotenv import load_dotenv
import os
load_dotenv()
# custom config with the specific model of GPT-3 and the API key
api_key = os.environ.get('API_KEY')
model = 'gpt-3.5-turbo'
