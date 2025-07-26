import random
import json

from utils.helpers import is_connected
from core.groq_assistant import groq_assistant_object

#plugins import
from plugins.jokes import initial_function_joke, joke_offline, joke_online, OFFLINE_CATEGORY_LIST
from plugins.weather import initial_function_weather, get_weather
from plugins.wikipedia_search import initial_function_wikipedia, get_page_summary, get_page_info
from plugins.open_features import open_app_or_web
from plugins.system_features import take_screenshot, search_in_google, tell_current_date, tell_current_time



def main_intent_handler(command):
    prompt = f"""
        You are given a user command enclosed in angle brackets:

        <{command}>

        Rewrite this command to be clear, specific, and suitable for a voice assistant. 
        Correct all spelling and grammar errors.

        Respond only with a JSON object in the following format. Thats it. No extra text. No explanation. Just JSON format output.
        {{"corrected_command": "<your corrected version here>"}}
    """
    
    #The logic will be set later
    if command is None:
        return 
    corrected_command = command 
    
    try:
        if 'joke' in corrected_command.lower():
            if is_connected():
                extracted_info = initial_function_joke(corrected_command)
                joke = joke_online(dict_info=extracted_info)
                return joke
            
            else:
                
                for category in OFFLINE_CATEGORY_LIST:
                    if category in corrected_command:
                        joke = joke_offline(category=category)
                        return joke
                    else:
                        joke = joke_offline(category=random.choice(OFFLINE_CATEGORY_LIST))
                        answer = (
                        'Sorry, you are offline and I could not get the joke from your category. I will tell you a random joke.'
                        f'..... {joke}'
                        )
                        return answer
                    
        
        elif 'weather' in corrected_command.lower():
            extracted_info = initial_function_weather(command)
            weather = get_weather(extracted_info)
            return weather
        

        elif "wikipedia" in corrected_command.lower():
            extracted_info = initial_function_wikipedia(corrected_command)
            print(extracted_info)

            if extracted_info['type'].lower() == 'summary':
                response = get_page_summary(
                    title=extracted_info['topic'], 
                    sentences= int(extracted_info['sentences']) if 'sentences' in extracted_info else 0, 
                    chars= int(extracted_info['chars']) if 'chars' in extracted_info else 0
                )
                return response
            else:
                response = get_page_info(
                    title=extracted_info['topic']
                )
                return response.content  #Sends the wikipedia page to speak the content
        

        elif 'open' in corrected_command.lower() or 'launch' in corrected_command.lower() or 'go to' in corrected_command.lower():
            to_open = corrected_command.split(" ")[-1].lower()
            print(f'[DEBUG] : {to_open}')
            response = open_app_or_web(to_open)
            return response
            

        elif 'screenshot' in corrected_command.lower():
            take_screenshot()
            return 'Screenshot taken'
        
        elif 'current date' in corrected_command.lower():
            response = tell_current_date()
            return response

        elif 'current time' in corrected_command.lower():
            response = tell_current_time()
            return response
        
        elif 'search' and 'google' in corrected_command.lower():
            search_in_google(corrected_command)

        else:
            response = groq_assistant_object.process_with_groq(prompt=corrected_command ,system_content='You are a virtual assistant. Talk to the user like a chatbot.')
            return response
        
    except AttributeError as e:
        print('DEBUG: Attribute error has occurred')
        pass

