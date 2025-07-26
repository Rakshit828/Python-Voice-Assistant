import wikipedia

#Local Modules
from core.command_utils import extract_info_from_command


def initial_function_wikipedia(command):
    prompt = (
        f"You are an intelligent parser designed to extract structured data from user voice commands.\n\n"
        f"The user's voice command is enclosed in angle brackets below:\n"
        f"<{command}>\n\n"

        "Your task is to analyze the command and return a structured JSON object based on the following criteria:\n\n"

        "1. Determine if the user is requesting a **Wikipedia summary** (e.g., 'summarize', 'give me a summary', 'brief info').\n"
        "   - If yes, extract the topic title.\n"
        "   - If the user explicitly mentions a number of sentences or a character limit for the summary, extract that as well.\n"
        "   - Return a JSON object in one of the following formats:\n"
        '     {"type": "summary", "topic": "Artificial Intelligence", "sentence": "5"}\n'
        '     {"type": "summary", "topic": "Artificial Intelligence", "chars": "180"}\n'
        '     {"type": "summary", "topic": "Data Science"}\n\n'

        "2. If the command is a general request to search or look up information on Wikipedia **without asking for a summary**,\n"
        "   extract only the topic title and return a simpler JSON object in the following format:\n"
        '     {"type": "search", "topic": "Python (programming language)"}\n'
        '     {"type": "search", "topic": "Mr Beast"}\n\n'

        "**Important Notes:**\n"
        "- Only return valid JSON — no explanations, extra text, or formatting outside of the JSON object.\n"
        "- Keys like 'sentence' or 'chars' should only appear if the user explicitly requested them.\n"
    )
    return extract_info_from_command(prompt)



def get_page_info(*, title):
    try:
        page = wikipedia.page(title=title)
        return page
    except wikipedia.exceptions.PageError:
        return ('[ERROR]: Couldnot find the padge for title: {title}')
    except wikipedia.exceptions.DisambiguationError:
        return (f'This might be more results reffering to the topin {title}. Try to be more specific')
    except wikipedia.exceptions.WikipediaException:
        return ('An unexpected error occurred')


def get_page_summary(*, title, sentences = 0, chars = 0):
    if not sentences and not chars:
        sentences = 5
    try:
        if chars:
            return wikipedia.summary(title, chars=chars)
        else:
            return wikipedia.summary(title, sentences=sentences)
        
    except wikipedia.exceptions.PageError:
        return ('[ERROR]: Couldnot find the padge for title: {title}')

    except wikipedia.exceptions.DisambiguationError:
        return (f'This might be more results reffering to the topin {title}. Try to be more specific')
    
    except wikipedia.exceptions.HTTPTimeoutError:
        return (f'Request failed. Check if your device is offline')
    
    except wikipedia.exceptions.WikipediaException:
        return ('An unexpected error occurred')



    
    
    

