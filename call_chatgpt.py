import openai
import  os
from dotenv import load_dotenv
load_dotenv('.env')

KEY_CHATGPT =  os.environ.get('KEY_CHATGPT')
openai.api_key=KEY_CHATGPT

pregunta ="escribe los colores posible de los elefantes"
completion = openai.Completion.create(engine="text-davinci-003",
                                      prompt=pregunta,
                                      max_tokens=2048)

print(completion.choices[0].text)

