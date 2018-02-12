from flask import Flask, redirect, url_for, request, render_template
from flask_bootstrap import Bootstrap
app = Flask(__name__)
bootstrap=Bootstrap(app)
#from transcribe import transcribe_file
import io
import indicoio
import recorder
#record to file?
indicoio.config.api_key = "6e20bd4ee1b0be47f25d0f227578fd14"

def sentiment_analysis(text):
    sentiment = indicoio.sentiment(text)
    return sentiment

def keywords(text):
    return indicoio.keywords(text)

def emotion(text):
    return indicoio.emotion(text)

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
    return "Transcript: "+y + " \n Sentiment:"+str(sentiment)


@app.route('/success/')
@app.route('/success/<name>')
def success(name):
    return render_template('success.html', success_message=name)

@app.route('/login',methods = ['POST', 'GET'])
def login():
    rec = recorder.Recorder(channels=1)
    with rec.open('block.wav', 'wb') as recfile:
        recfile.record(duration=15.0)
    x = transcribe_file("/Users/brianha/hackbeanpot/block.wav")

    if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = x))
    else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

if __name__ == '__main__':
   app.run(debug = True)


#how do i make the text come out nicely
#include html and css in this file?
#what else can I do with this data or how can i add different bars?
