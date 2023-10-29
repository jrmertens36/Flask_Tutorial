import openai
from flask import current_app


def get_completion(prompt, model="gpt-3.5-turbo", temperature=0):

    openai.api_key = current_app.config.get('OPENAI_APIKEY')
    openai.org_key = current_app.config.get('OPENAI_ORGKEY')

    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


def check_comment(comment):
    prompt = f"""
    Du erhältst nachfolgenden Kommentar begrenzt mit dreifachen Anführungszeichen. 
    Sollte der Kommentar in einer anderen Sprache als deutsch sein, nenne die Originalsprache und übersetze ihn erst 
    in deutsch.
    Teile die Stimmungslage ein in 
    - positiv
    - neutral
    - negativ    
    Sind in dem Kommentar technische Fragen gestellt, extrahiere die Frage.
    Sind in dem Kommentar Fragen zur Lieferzeit, extrahiere die Frage.

    \"\"\"{comment}\"\"\"
    """

    return get_completion(prompt)
