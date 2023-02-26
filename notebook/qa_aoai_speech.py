#!/usr/bin/env python
# coding: utf-8
import time
import openai

from azure.cognitiveservices.speech import SpeechConfig


# 请在这里设定您的环境
YOUR_SPEECH_KEY = "<YOUR_SPEECH_API_KEY>"
YOUR_SPEECH_REGION = "<YOUR_SPEECH_SERVICE_REGION>"
YOUR_OPENAI_KEY = "<YOUR_OPENAI_API_KEY>"
YOUR_OPENAI_BASE = "<YOUR_OPENAI_ENDPOINT>"
YOUR_OPENAI_ENGINE = "text-davinci-003"

try:
    import azure.cognitiveservices.speech as speechsdk
except ImportError:
    print("""
    Importing the Speech SDK for Python failed.
    Refer to
    https://docs.microsoft.com/azure/cognitive-services/speech-service/quickstart-python for
    installation instructions.
    """)
    import sys
    sys.exit(1)

# Set up the subscription info for the Speech Service:
# Replace with your own subscription key and service region (e.g., "westus").
speech_key, service_region = YOUR_SPEECH_KEY, YOUR_SPEECH_REGION

prompt_context = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n"

last_prompt = ""
bye = False

def callGPT3(prompt):
    openai.api_type = "azure"
    openai.api_base = YOUR_OPENAI_BASE
    openai.api_version = "2022-12-01"
    openai.api_key = YOUR_OPENAI_KEY
    
    

    # print(prompt)
    global prompt_with_context, last_prompt
    prompt_with_context = prompt_context + last_prompt + prompt + "\n"

    response = openai.Completion.create(
    engine=YOUR_OPENAI_ENGINE,
    prompt=prompt_with_context,
    temperature=0.9,
    max_tokens=400,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop=None
    )
    # print (response)

    gpt_resp = response.choices[0].text
    print("GPT: " + gpt_resp)
    last_prompt = prompt + "\n" + gpt_resp + "\n"
    # print(last_prompt)
    tts(gpt_resp)

    if prompt == "Goodbye.":
        exit()


def speech_recognize_once_from_mic():
    
    # <SpeechRecognitionWithMicrophone>
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region, speech_recognition_language="en-us")
    # Creates a speech recognizer using microphone as audio input.
    # The default language is "en-us".
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

    done = False

    # GPT-3 prompt
    myprompt = ""

    def stop_cb(evt):
        """callback that signals to stop continuous recognition upon receiving an event `evt`"""
        # print('CLOSING on {}'.format(evt))
        nonlocal done
        done = True

    def get_text(evt):
        #print('RECOGNIZED: {}'.format(evt))
        nonlocal myprompt
        myprompt = myprompt + evt.result.text
        print(myprompt)
        nonlocal done
        done = True   
              
    # Connect callbacks to the events fired by the speech recognizer
    #speech_recognizer.recognizing.connect(lambda evt: print('RECOGNIZING: {}'.format(evt)))
    #speech_recognizer.recognized.connect(lambda evt: print('RECOGNIZED: {}'.format(evt)))
    speech_recognizer.recognized.connect(lambda evt: get_text(evt))

    speech_recognizer.session_started.connect(lambda evt: print("Human:"))
    # speech_recognizer.session_stopped.connect(lambda evt: print('SESSION STOPPED {}'.format(evt)))
    speech_recognizer.canceled.connect(lambda evt: print('CANCELED {}'.format(evt)))
    # stop continuous recognition on either session stopped or canceled events
    speech_recognizer.session_stopped.connect(stop_cb)
    speech_recognizer.canceled.connect(stop_cb)

    # Start continuous speech recognition
    speech_recognizer.start_continuous_recognition()
    while not done:
        time.sleep(.1)

    speech_recognizer.stop_continuous_recognition()
    # </SpeechContinuousRecognitionWithFile>

    callGPT3(myprompt)




def tts(text):

    speech_config = SpeechConfig(subscription=speech_key, region=service_region)

    speech_config.speech_synthesis_language = "en-us" 
    speech_config.speech_synthesis_voice_name ="en-US-AriaNeural"

    # Creates a speech synthesizer for the specified language,
    # using the default speaker as audio output.
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

    # Receives a text from console input and synthesizes it to speaker.
    result = speech_synthesizer.speak_text_async(text).get()
    
    

while not bye:
    speech_recognize_once_from_mic()


