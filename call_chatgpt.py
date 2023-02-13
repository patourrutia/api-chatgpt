import openai
import  os
from dotenv import load_dotenv
load_dotenv('.env')



def call_gpt(preg):
    KEY_CHATGPT =  os.environ.get('KEY_CHATGPT')
    openai.api_key=KEY_CHATGPT
    try:
        completion = openai.Completion.create(engine="text-davinci-003",
                                            prompt=preg,
                                            max_tokens=2048)
        respuesta = completion.choices[0].text
        return respuesta
    except:
        return "NO TENGO RESPUESTA"
    


pregunta ="traduce a idioma ingles la frase vamos para la playa"
print(call_gpt(pregunta))

