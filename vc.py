import pyttsx3
import wikipedia

# Initialize the text-to-speech engine
voice = pyttsx3.init()

# Input from the user
In = input("Searching Wikipedia/Google: ")

# Search Wikipedia and get a summary
try:
    result = wikipedia.summary(In, sentences=3)
    print(result)

    # Speak the summary
    voice.say(result)
    voice.runAndWait()

except wikipedia.exceptions.DisambiguationError as e:
    print("It seems there are multiple possible results. Please be more specific in your search.")
except wikipedia.exceptions.PageError as e:
    print("Sorry, no matching page found on Wikipedia.")
except wikipedia.exceptions.WikipediaException as e:
    print("An error occurred while searching Wikipedia.")
except Exception as e:
    print("An unexpected error occurred:", str(e))
