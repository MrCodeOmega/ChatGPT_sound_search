import speech_recognition as sr
import openai
import os

# Set up the API key for OpenAI
openai.api_key = "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"

# Initialize the recognizer
r = sr.Recognizer()

# Define a function to handle the voice input and generate the response from ChatGPT


def chatbot_voice_input():
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

        try:
            # Use the Google Speech Recognition API to transcribe the voice input
            text = r.recognize_google(audio)
            print("You said: " + text)

            # Generate a response from ChatGPT
            response = openai.Completion.create(
                engine="davinci", prompt=text, max_tokens=60
            )

            # Print the response from ChatGPT
            print(response["choices"][0]["text"])

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(
                "Could not request results from Google Speech Recognition service; {0}".format(e))


# Call the chatbot_voice_input function
chatbot_voice_input()
