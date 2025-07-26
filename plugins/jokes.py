import pyjokes
import random
import requests


from core.groq_assistant import groq_assistant_object
from core.command_utils import extract_info_from_command

OFFLINE_CATEGORY_LIST = ['neutral', 'chuck', 'twister', 'all'] #pyjokes
ONLINE_JOKE_CATEGORY_LIST = ['Any', 'Programming', 'Misc', 'Dark', 'Pun', 'Spooky', 'Christmas']


joke_api_v2 = 'https://v2.jokeapi.dev/joke'
# joke_api_official = 'https://v2.jokeapi.dev/joke/Any'


def initial_function_joke(command):
    prompt = f"""
        The following sentence between <angle brackets> is a user command to a voice assistant:
        <{command}>

        Your task:

        Step 1: From the following list of joke categories, extract the word that best matches the user's intent:
        {ONLINE_JOKE_CATEGORY_LIST}

        Step 2: Identify if the user wants a 'single' or 'twopart' joke. If unclear, choose one at random.

        Output:
        Respond with a JSON object using lowercase strings and no extra text. The JSON must have exactly two keys. Just json. No explaination:
        - "category": the best-matching category from Step 1
        - "type": either "single" or "twopart", based on Step 2

        Examples:
        {{
            "category" : "programming",
            "type": "single"
        }}
        \n
        {{
            "category" : "neutral",
            "type": "twopart"
        }}
    """
    extracted_info =  extract_info_from_command(prompt)
    print(extracted_info)
    return extracted_info


def joke_offline(*, category ):
    joke = pyjokes.get_joke(language='en', category=category)
    return joke

def joke_online(*, dict_info):
    category = dict_info['category']
    type = dict_info['type']
    try:
        response = requests.get(f"{joke_api_v2}/{category}?type={type}")
        joke_data = response.json()
        if joke_data['type'] == 'single':
            return joke_data['joke']
        else:
            return f'{joke_data['setup']}. \n {joke_data['delivery']}'

    except requests.exceptions.RequestException:
        return 'Request Failed. Check if your device is offline'
    except Exception as e:
        return f'Some error occured: {e}'
        
        
