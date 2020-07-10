"""Synthesizes speech from the input string of text or ssml.

Note: ssml must be well-formed according to:
    https://www.w3.org/TR/speech-synthesis/
"""
import os
import tkinter as tk
from tkinter import *
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="D:\google.json"
save_path = "D:\The Shop of ButterFly\Assets\Voices\\"
from google.cloud import texttospeech

window = tk.Tk()
window.title('Text to Speech Google')
names = [
    'ja-JP-Wavenet-A',
    'ja-JP-Wavenet-B',
    'ja-JP-Wavenet-C',
    'ja-JP-Wavenet-D'
    ]
def show_entry_fields():
    # Instantiates a client
    client = texttospeech.TextToSpeechClient()
    # Set the text input to be synthesized
    texts = str(e1.get())
    synthesis_input = texttospeech.SynthesisInput(text=texts)
    e1.delete(0, tk.END)
    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.VoiceSelectionParams(
        language_code="ja-JP", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL, name = variable.get()
    )

    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # The response's audio_content is binary.
    with open( os.path.join(save_path+ variable.get(),texts+".mp3"), "wb") as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print('Audio content written to file '+texts+'.mp3"')

tk.Label(window, text="Text:").grid(row=0,column=0)
e1 = tk.Entry(window, width=100)

e1.grid(row=0, column=1)
tk.Button(window,
          text='Generate MP3', command=show_entry_fields).grid(row=2,
                                                       column=1,
                                                       sticky=tk.W,
                                                       pady=4)
variable = StringVar(window)
variable.set(names[0]) # default value

w = OptionMenu(window, variable, *names)
w.grid(row=2, column=1)


window.mainloop()

