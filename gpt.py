import openai
from const import API_KEY

openai.api_key = API_KEY

def get_answer(question:str)->str:
    resp = openai.Completion.create(
        model='text-davinci-003',
        prompt=question,
        max_tokens=1000,  # prompt and answer together have 4096 tokens
    )
    answer = resp['choices'][0]['text']
    answer = answer.replace('?', '').strip()
    return answer

