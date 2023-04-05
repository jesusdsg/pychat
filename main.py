import openai
import config
from halo import Halo

# config the api key
openai.api_key = config.api_key

# init the chat
started = True
while started:
    try:
        content = input('\033[92m' + 'AI: ' + '\033[0m' +
                        'Hello human, How can I help you?\n')
    except Exception:
        print('\033[91m' + 'Please, give me a valid question.' + '\033[0m')

    if content == 'exit':
        print('\033[94m' + 'Ok, I got it, so.. Goodbye.' + '\033[0m')
        break

    spinner = Halo(text='Let me see what I can do...',
                   spinner='dots', color='blue', animation='bounce')
    spinner.start()

    response = openai.ChatCompletion.create(model=config.model, messages=[
        {'role': 'user', 'content': content}])
    spinner.stop()
    print('\n' + '\033[92m' + 'AI: ' + '\033[0m' +
          response.choices[0].message.content + '\n')
