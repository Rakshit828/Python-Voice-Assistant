from config.settings import GROQ_API_KEY
from groq import Groq


class GroqAssistant:
    def __init__(self):
        self.client = Groq(api_key=GROQ_API_KEY)
        self.system_prompts = {
            'default' : 'You are a bridge between the user and the voice assistant who cleans up and make commands clear for the voice assistant.'
        }
    
    def process_with_groq(self, prompt, system_content = None):
        try:
            response = self.client.chat.completions.create(
                messages=[
                    # Set an optional system message. This sets the behavior of the
                    # assistant and can be used to provide specific instructions for
                    # how it should behave throughout the conversation.
                    {
                        "role": "system",
                        "content": self.system_prompts['default'] if not system_content else system_content
                    },
                    # Set a user message for the assistant to respond to.
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],

                # The language model which will generate the completion.
                # mixtral-8x7b-32768
                # llama-3.3-70b-versatile
                
                model="llama-3.3-70b-versatile",

                temperature=0.5,
                max_completion_tokens=1024,
                top_p=1,
                stop=None,

                # If set, partial message deltas will be sent.
                # stream=True,   #It is like the flush parameter in print statement
            )
            return response.choices[0].message.content
        
        except Exception as e:
            print(f'[DEBUG]: Error occurred in the groq assistant during the processing {e}')


groq_assistant_object = GroqAssistant()