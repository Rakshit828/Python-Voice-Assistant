from core.groq_assistant import groq_assistant_object

import json


def extract_info_from_command(prompt):
    extracted_info = groq_assistant_object.process_with_groq(prompt).lower().strip()
    try:
        dict_data = json.loads(extracted_info)
        return dict_data
    except Exception as e:
        return f'Erro at extracting information occurred: {e}'
    
