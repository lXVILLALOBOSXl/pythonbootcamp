import PyPDF2
import requests

with open("test.pdf", "rb") as file:
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()


API_KEY = ""
API_URL = "http://api.voicerss.org/"

params = {
    "key": API_KEY,
    "hl": "es-mx",
    "c": "MP3",
    "f": "16khz_16bit_stereo",
    "src": text 
}

response = requests.post(API_URL, params=params)

if response.status_code == 200:
    with open("output.mp3", "wb") as audio_file:
        audio_file.write(response.content)
    print("Audio created successfully!")
else:
    print("Error creating audio file", response.text)