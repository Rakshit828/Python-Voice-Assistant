import time
import random

#Local modules
from core.voice_assistant import VoiceAssistant
from core.intent_handler import main_intent_handler


main_assistant_object = VoiceAssistant(wake_word='siri')

def main():
    main_assistant_object.speech_engine.speak('Awake me')
    
    while True:
        listen_result = main_assistant_object.listen_to_wake_word()

        if isinstance(listen_result, Exception):
            main_assistant_object.speech_engine.speak(str(listen_result))
            listen_result = False

        if listen_result is True:
            main_assistant_object.greet_according_to_time()
            while True:
                text = main_assistant_object.speech_recognizer.recognize_speech()
                if isinstance(text, Exception):
                    main_assistant_object.speech_engine.speak(str(text))
                
                print(f'Unfiltered command: {text}')

                response = main_intent_handler(text)
                
                print(response)
                print('Assistant response to command: \n')
                main_assistant_object.speech_engine.speak(response)
                main_assistant_object.speech_engine.speak(random.choice(main_assistant_object.greetings_after_answer))

                time.sleep(0.5)


if __name__ == '__main__':
    main()





















    
# import threading
# import time
# import sys # Import sys for exiting the program

# #Local modules
# from core.voice_assistant import VoiceAssistant
# from core.intent_handler import handle_intent

# # Global flag to signal the main assistant to stop
# stop_assistant_event = threading.Event()


# def backgroundAssistant(stop_event: threading.Event):

#     backgroundAssistant = VoiceAssistant(wake_word='stop', id=2)
#     while not stop_event.is_set(): # Continue listening until stop_event is set
#         listen_result = backgroundAssistant.listen_to_wake_word()

#         if listen_result is True:
#             stop_event.set() # Set the event to signal main assistant to stop
#             return
        

# def mainAssistant(stop_event: threading.Event):
#     """
#     Main assistant logic. Continues until the stop_event is set.
#     """
#     mainAssistant = VoiceAssistant(wake_word='jarvis', id=1)

#     while not stop_event.is_set(): # Main loop condition
#         listen_result = mainAssistant.listen_to_wake_word()

#         if stop_event.is_set():
#             print("[DEBUG]: Main Assistant detected stop signal after wake word listen.")
#             break
    
#         if isinstance(listen_result, Exception):
#             mainAssistant.speech_engine.speak(str(listen_result))
#             listen_result = False

#         if listen_result is True:
#             print("Main Assistant: 'Jarvis' wake word detected.")
#             mainAssistant.speech_engine.speak('Yes Boss')
            
#             while not stop_event.is_set(): 

#                 if stop_event.is_set():
#                     print("[DEBUG]: Main Assistant detected stop signal within command loop.")
#                     break # Exit inner loop

#                 mainAssistant.speech_engine.speak('Give Command')
                
#                 if stop_event.is_set(): # Check again before listening for command
#                     print("[DEBUG]: Main Assistant detected stop signal before command listen.")
#                     break # Exit inner loop

#                 text = mainAssistant.speech_recognizer.recognize_speech()
                
#                 if stop_event.is_set(): # Check again after recognizing speech
#                     print("[DEBUG]: Main Assistant detected stop signal after command recognize.")
#                     break # Exit inner loop

#                 if isinstance(text, Exception):
#                     mainAssistant.speech_engine.speak(str(text))
#                 else:
#                     print(f"Main Assistant: Command received: {text}")
#                     response = handle_intent(text)

#                     # Break down long story into chunks to allow interruption
#                     words = response.split(" ")
    
#                     for i in range(0, len(words), 10): # Speak 10 words at a time
#                         if stop_event.is_set():
#                             print("Main Assistant: Stopping....")
#                             mainAssistant.speech_engine.speak('Stopping.....')
#                             mainAssistant.speech_engine.stop_speaking_if_possible() # Attempt to stop current speech
#                             break
#                         chunk = " ".join(words[i:i+10])
#                         mainAssistant.speech_engine.speak(chunk)
#                         time.sleep(0.1) # Small delay between chunks
#                     else:
#                         # Example of calling handle_intent
#                         # response = handle_intent(text)
#                         # mainAssistant.speech_engine.speak(response)
#                         mainAssistant.speech_engine.speak(f"You said: {text}. I'm processing that.")
                        
#                 time.sleep(0.5) # Small delay to prevent busy-waiting

#     print("Main Assistant: Loop terminated. Attempting to shut down speech engine.")
#     # Attempt to gracefully shut down speech engine if it has a specific method for it
#     if hasattr(mainAssistant.speech_engine, 'shutdown'):
#         mainAssistant.speech_engine.shutdown()
#     print("Main Assistant: Exiting.")


# if __name__ == '__main__':
#     # Initialize the shared event object
#     # This event will be used by both threads to communicate the stop signal
#     global stop_assistant_event 
#     stop_assistant_event = threading.Event() # Ensure it's initialized before threads start

#     mainAssistantThread = threading.Thread(target=mainAssistant, args=(stop_assistant_event,))
#     backgroundAssistantThread = threading.Thread(target=backgroundAssistant, args=(stop_assistant_event,))

#     # Set backgroundAssistant as a daemon thread. This allows the program to exit
#     # if the main thread (or all non-daemon threads) finishes.
#     backgroundAssistantThread.daemon = True 

#     mainAssistantThread.start()
#     backgroundAssistantThread.start()

#     # Wait for the main assistant thread to finish.
#     # The backgroundAssistantThread (daemon) will exit when mainAssistantThread finishes.
#     mainAssistantThread.join()

#     # Once mainAssistantThread has joined (meaning it exited its loop),
#     # ensure the stop_event is set to signal the background thread to also finish gracefully,
#     # even if it's a daemon (good practice for clarity and robustness, though daemon handles it).
#     stop_assistant_event.set()
#     backgroundAssistantThread.join(timeout=1) # Give it a moment to clean up

#     print("All assistant threads have stopped. Exiting program.")
#     sys.exit(0) # Explicitly exit the program