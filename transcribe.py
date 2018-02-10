

"""What we are building:
Speech to text + sentiment analysis in Python

What we need:
1. Record the voice and save it into a .wav file
2. Transcribe the audio file into text via Google Cloud Platform
and Cloud speech API
3. Get the sentiment score of the transcribed text, Indico

HOW TO USE GOOGLE API's:
sign into google cloud  platform, create new project and enable api's
for cloud speech api, enable and follow instructions on page, make a service account api_key
have an api key, have a OAuth client ID
Create new service account keys for different team members
download JSON file

terminal
export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/service-account-file.json"

then make a speech API request, can either do it with curl, or use python code
"""

import io
import indicoio

#record to file?
indicoio.config.api_key = "6e20bd4ee1b0be47f25d0f227578fd14"

#live feed of audio
#doing on loop
#store on firebase for real time data, immediately record and put into firebase
#send to indico
#display to back

#record a video of the?
#mapping the progression

#the mood of someones speech can change mid sentence

#live status of peoples emotion


#transcribe_file()

def transcribe_file(speech_file):
    """Transcribe the given audio file."""
    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types
    client = speech.SpeechClient()

    with io.open(speech_file, 'rb') as audio_file:
        content = audio_file.read()

    audio = types.RecognitionAudio(content=content)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code='en-US')

    response = client.recognize(config, audio)
    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        x = format(result.alternatives[0].transcript)
        print('Transcript: '+x)
        #get_text_sentiment()
        sentiment = indicoio.sentiment_hq(x)

        print sentiment



transcribe_file("/Users/brianha/Documents/test4.wav")
