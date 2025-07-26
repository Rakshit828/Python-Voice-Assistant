import subprocess
import sys
import webbrowser

#Importing the applications data
from data.system_data import application_mappings, website_mappings


def open_app_or_web(to_open):
    if to_open in website_mappings:
        open_websites(website_mappings[to_open])
    elif to_open in application_mappings:
        open_applications(application_mappings[to_open])
    else:
        pass
        #Logic to add unknown app or application to a data


def open_applications(value):
    subprocess.Popen([value])
    return 'Opened'
    

def open_websites(url):
    webbrowser.open(url)
    return 'Opened'