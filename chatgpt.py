import os

from flask import current_app
from openai import OpenAI

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=os.environ.get("OPENAI_API_KEY")
)

def get_completion(prompt, model="gpt-3.5-turbo", temperature=0):


    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        model=model,
        temperature=temperature,
    )

    return response.choices[0].message.content


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
