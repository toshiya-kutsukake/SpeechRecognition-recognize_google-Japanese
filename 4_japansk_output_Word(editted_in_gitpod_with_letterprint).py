# pip install SpeechRecognition
# pip install moviepy
# pip install python-docx


import speech_recognition as sr
r = sr.Recognizer()

from moviepy.editor import AudioFileClip

my_clip = AudioFileClip("cutwithsound.mp4")
audio = "sound.wav"
my_clip.write_audiofile(audio)

with sr.AudioFile(audio) as source:
    audio = r.record(source)
text= r.recognize_google(audio, language="ja-JP")


filename = "textfile.txt"
f = open(filename, "w+")


remainder = text.split()
while remainder:
    line, remainder = remainder[:10], remainder[10:]
    f.write(' '.join(line) + "\n")


from docx import Document
document = Document()

with open('textfile.txt') as f:
    for line in f:
        print(line)
        document.add_paragraph(line)
document.save('wordfile.docx')