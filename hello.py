from flask import Flask, redirect, url_for, request
app = Flask(__name__)

#from transcribe import transcribe_file

import io
import indicoio
import recorder
#record to file?
indicoio.config.api_key = "6e20bd4ee1b0be47f25d0f227578fd14"


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
    y=""
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        x = format(result.alternatives[0].transcript)

        y = y + x
        #get_text_sentiment()
    sentiment = indicoio.sentiment_hq(y)
    return y + " \n"+str(sentiment)

@app.route('/success/<name>')
def success(name):
   return 'Transcript: %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
    rec = recorder.Recorder(channels=1)
    with rec.open('blocking9.wav', 'wb') as recfile:
        recfile.record(duration=10.0)
    x = transcribe_file("/Users/brianha/hackbeanpot/blocking9.wav")



    if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = x))
    else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

if __name__ == '__main__':
   app.run(debug = True)
